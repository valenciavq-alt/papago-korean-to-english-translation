"""
Papago Translation Module
Transcribes Korean video and creates bilingual subtitles using Whisper and Papago API.
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import time
from typing import List, Dict, Any


class PapagoTranslator:
    """Handles translation using Papago API."""
    
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.url = "https://papago.apigw.ntruss.com/nmt/v1/translation"
    
    def translate_ko_to_en(self, text: str, timeout: int = 30) -> str:
        """Translate Korean text to English using Papago API.
        
        Args:
            text: Korean text to translate
            timeout: Request timeout in seconds
            
        Returns:
            Translated English text, or error message if translation fails
        """
        if not text.strip():
            return ""
        
        enc_text = urllib.parse.quote(text)
        data = f"source=ko&target=en&text={enc_text}"
        
        req = urllib.request.Request(self.url)
        req.add_header("X-NCP-APIGW-API-KEY-ID", self.client_id)
        req.add_header("X-NCP-APIGW-API-KEY", self.client_secret)
        
        try:
            with urllib.request.urlopen(req, data=data.encode("utf-8"), timeout=timeout) as res:
                response = json.loads(res.read().decode("utf-8"))
                if "message" in response and "result" in response["message"]:
                    return response["message"]["result"]["translatedText"]
                else:
                    return f"[Translation error: Unexpected response format]"
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8") if hasattr(e, 'read') else str(e)
            return f"[Translation error: HTTP {e.code} - {error_body}]"
        except Exception as e:
            return f"[Translation error: {str(e)}]"


def timestamp_to_srt(seconds: float) -> str:
    """Convert seconds to SRT timestamp format.
    
    Args:
        seconds: Time in seconds
        
    Returns:
        SRT timestamp string (HH:MM:SS,mmm)
    """
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds * 1000) % 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def segments_to_srt(
    segments: List[Dict[str, Any]],
    translator: PapagoTranslator,
    show_progress: bool = False,
    progress_callback=None,
) -> str:
    """Convert Whisper segments to bilingual SRT format with styling.

    Styling (as requested):
    - Font: NanumGothic for both languages
    - Korean: 16pt, color #A7C1E8 (top line)
    - English: 15pt, color #FFFFFF (bottom line)
    - One \\N between KR and EN; double line break between segments
    """

    lines: List[str] = []
    start_time = time.time()
    total_segments = len(segments)
    
    for i, seg in enumerate(segments):
        start = seg["start"]
        end = seg["end"]
        text_ko_plain = seg["text"].strip()
        
        try:
            en_plain = translator.translate_ko_to_en(text_ko_plain)
            if en_plain.startswith("[Translation error"):
                en_plain = "[Translation failed]"
        except Exception as e:
            en_plain = f"[Translation error: {str(e)}]"

        # Apply exact styling using SSA tags inside SRT lines
        # Note: many players/editors respect these inline tags
        # CapCut-compatible SRT: plain text (no styling tags), KR above EN, real line break
        ko_line = text_ko_plain
        en_line = en_plain

        # SRT requires a blank line between entries; emit Unix LF line endings
        lines.append(
            f"{i+1}\n{timestamp_to_srt(start)} --> {timestamp_to_srt(end)}\n{ko_line}\n{en_line}\n\n"
        )

        # Safe progress updates (avoid evaluating Progress object)
        if total_segments > 0:
            try:
                if progress_callback is not None:
                    progress_value = 0.6 + (0.2 * (i + 1) / total_segments)
                    progress_callback(progress_value, desc=f"Translating segment {i+1}/{total_segments}...")
            except (AttributeError, IndexError, TypeError):
                pass
        
        if show_progress and (i + 1) % max(1, total_segments // 10 or 1) == 0:
            elapsed = time.time() - start_time
            per_seg = elapsed / (i + 1)
            remaining = (total_segments - (i + 1)) * per_seg
            print(f"⏳ {i+1}/{total_segments} done — ~{remaining/60:.1f} min left")
    
    content = "".join(lines)
    # Normalize spacing: exactly one blank line between cues and a trailing blank line
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    while "\n\n\n" in content:
        content = content.replace("\n\n\n", "\n\n")
    if not content.endswith("\n\n"):
        content = content.rstrip("\n") + "\n\n"
    return content

