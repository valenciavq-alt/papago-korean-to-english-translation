# Hugging Face Space Deployment Checklist

## Files Ready for Upload ✅

### Required Files:
- [x] `app.py` - Main Gradio application (configured for HF Spaces)
- [x] `papago_translation.py` - Core translation module
- [x] `requirements_hf.txt` - Clean dependencies (copy to `requirements.txt` for Space)
- [x] `README_HF.md` - Space description with YAML frontmatter

### Optional Files:
- [x] `.gitignore` - Excludes unnecessary files

## Quick Upload Steps

### Method 1: Using Git (Recommended)
```bash
# 1. Create Space on Hugging Face website first
# 2. Clone your Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME

# 3. Copy files
cp ../papago-translation/app.py .
cp ../papago-translation/papago_translation.py .
cp ../papago-translation/requirements_hf.txt requirements.txt
cp ../papago-translation/README_HF.md README.md

# 4. Commit and push
git add .
git commit -m "Initial commit: Papago Korean Translation"
git push
```

### Method 2: Using Web Interface
1. Go to your Space page on Hugging Face
2. Click **"Files"** tab → **"Add file"** → **"Upload file"**
3. Upload these files:
   - `app.py`
   - `papago_translation.py`
   - `requirements.txt` (use content from `requirements_hf.txt`)
   - `README.md` (use content from `README_HF.md`)

## File Contents to Copy

### requirements.txt (for Space)
```
openai-whisper>=20231117
ffmpeg-python>=0.2.0
tqdm>=4.66.0
gradio>=4.0.0
```

### README.md (for Space)
Copy entire content from `README_HF.md`

## Important Notes

1. **requirements.txt**: Use `requirements_hf.txt` content (without pytest dependencies)
2. **README.md**: Use `README_HF.md` content (includes YAML frontmatter)
3. **app.py**: Already configured correctly for Spaces
4. **Hardware**: Choose CPU Basic (free) or GPU (if needed, requires credits)

## After Upload

1. Wait 5-10 minutes for build to complete
2. Check **Logs** tab for any errors
3. Test your Space once it's live
4. Share the Space URL with others!

## Space URL
Your Space will be available at:
`https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`


