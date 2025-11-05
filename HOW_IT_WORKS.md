# How The System Works

## Overview

You have **one project** but **two separate Git repositories** that serve different purposes:

```
┌─────────────────────────────────────────────────────────────┐
│  YOUR COMPUTER                                              │
│  /Users/valencia/papago-translation/                       │
│                                                             │
│  ┌───────────────────────────────────────────────────┐    │
│  │  MAIN REPOSITORY (GitHub)                         │    │
│  │  - All your code files                             │    │
│  │  - Documentation                                    │    │
│  │  - Scripts                                          │    │
│  │  - Connected to: github.com                         │    │
│  └───────────────────────────────────────────────────┘    │
│                          │                                 │
│                          │ copy files                      │
│                          ▼                                 │
│  ┌───────────────────────────────────────────────────┐    │
│  │  hf-space/ FOLDER                                  │    │
│  │  (Cloned Hugging Face Space repo)                 │    │
│  │  - Only Space files                                │    │
│  │  - Connected to: huggingface.co                   │    │
│  └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                          │
                          │ git push
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  HUGGING FACE SPACES                                        │
│  - Automatically builds your app                            │
│  - Hosts it at: huggingface.co/spaces/zxc1232/...          │
│  - Users can access it via web browser                      │
└─────────────────────────────────────────────────────────────┘
                          │
                          │ git push
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  GITHUB                                                     │
│  - Stores your code                                         │
│  - Version control                                          │
│  - At: github.com/valenciavq-alt/papago-translation         │
└─────────────────────────────────────────────────────────────┘
```

## How It Works - Step by Step

### 1. **You Edit Files**
```
Location: /Users/valencia/papago-translation/
Action: Edit app.py, papago_translation.py, etc.
```

### 2. **Sync to Hugging Face Space**
```
Run: ./sync_to_hf.sh

What happens:
  1. Copies files from main repo → hf-space/
  2. Commits changes in hf-space/
  3. Pushes to Hugging Face Spaces
  4. Hugging Face rebuilds your app automatically
```

### 3. **Push to GitHub (Optional)**
```
Run: git push origin main

What happens:
  1. Pushes your main repo to GitHub
  2. All your code, docs, scripts saved
```

## Why Two Repositories?

### Main Repo (GitHub)
- ✅ Stores everything
- ✅ Version control
- ✅ Documentation
- ✅ Scripts and helpers
- ✅ Share code with others

### HF Space Repo
- ✅ Only files needed to run the app
- ✅ Hugging Face builds from this
- ✅ Separate from GitHub (different purpose)

## Workflow Example

```bash
# 1. Edit your code
vim app.py

# 2. Sync to Hugging Face (app goes live)
./sync_to_hf.sh "Add new feature"

# 3. (Optional) Push to GitHub (backup/share code)
git add .
git commit -m "Add new feature"
git push origin main
```

## Key Points

1. **Main repo** = Your working directory (everything)
2. **hf-space/** = Deployment directory (only Space files)
3. **They're separate** = Can update independently
4. **Sync script** = Automates copying and pushing

## What Gets Synced?

**To Hugging Face Space:**
- `app.py` → `app.py`
- `papago_translation.py` → `papago_translation.py`
- `requirements_hf.txt` → `requirements.txt`
- `README_HF.md` → `README.md`

**To GitHub:**
- Everything in main repo (all files)

## The Magic

When you push to Hugging Face Spaces:
1. They detect the push
2. Read `requirements.txt` → Install dependencies
3. Run `app.py` → Start your Gradio app
4. Make it accessible → Users can use it!

Your app is live at: https://huggingface.co/spaces/zxc1232/koreantoenglish


