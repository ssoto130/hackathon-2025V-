# Automated Deployment

## Quick Start

Run the automation script:

```bash
python automate_deploy.py
```

The script will:
- ✅ Open all necessary web pages automatically
- ✅ Generate secure SECRET_KEY
- ✅ Guide you through each step
- ✅ Add GitHub secrets (if GitHub CLI installed)
- ✅ Trigger deployment workflow
- ✅ Open your live site

## Installation (Optional)

For better automation, install GitHub CLI:

```powershell
winget install GitHub.cli
```

Or download from: https://cli.github.com/

## What You Need to Do

The script automates opening pages, but you'll need to:
1. Click buttons in Render to create database/service
2. Copy/paste the database URL and backend URL when prompted
3. Click buttons in GitHub to enable Pages and add secrets

Total time: ~5-7 minutes

## Without Python

If Python isn't working, follow the manual guide in `SIMPLE_DEPLOY.md`

## Your Site

Once complete: https://ssoto130.github.io/hackathon-2025V-/
