# PRD: Papago KR→EN Transcription & Subtitles

## Goals
- Upload audio/video
- Transcribe Korean with Whisper large-v3
- Translate to English via Papago API
- Output bilingual SRT (KR top 16pt #A7C1E8, EN bottom 15pt #FFFFFF)
- Burn subtitles into video with ASS + FFmpeg
- Use Space Secrets for Papago creds

## Non-Goals
- Multi-user auth
- Model fine-tuning

## Acceptance Criteria
- Given an MP4, when processed, then SRT downloads and a subtitled MP4 is produced.
- Korean text renders (no tofu) using NanumGothic.
- Korean above English; colors/sizes match spec.
- Errors surface in UI when FFmpeg or API fails.

## Risks
- FFmpeg filter/quoting issues
- Font availability in runtime
- Papago API reliability


