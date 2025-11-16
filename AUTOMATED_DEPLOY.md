# 🤖 Automated Deployment Script

This script automates as much of the deployment process as possible.

## Prerequisites

**Optional but Recommended:**
- Install GitHub CLI for automated secret management:
  ```powershell
  winget install GitHub.cli
  ```
  Or download from: https://cli.github.com/

## Usage

Run the automation script:

```powershell
cd "c:\Users\Skele\Downloads\hackathon-2025-main (2)\hackathon-2025-main"
.\deploy-setup.ps1
```

## What the Script Does

### ✅ Fully Automated:
- Opens all necessary web pages
- Generates secure SECRET_KEY
- Configures GitHub CLI (if installed)
- Adds GitHub secrets automatically (if GitHub CLI is installed)
- Triggers deployment workflow (if GitHub CLI is installed)

### ⚠️ Requires Manual Steps:
- Creating Render account (one-time)
- Enabling GitHub Pages source
- Creating Render database and web service
- Copying database URL and backend URL

## Without the Script

If you prefer manual setup, follow `QUICK_DEPLOY.md` instead.

## Troubleshooting

### Script won't run
If you get "execution policy" error, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\deploy-setup.ps1
```

### GitHub CLI not working
The script works without GitHub CLI, but you'll need to:
- Manually add the `BACKEND_URL` secret
- Manually trigger the deployment workflow

Install GitHub CLI for better automation:
```powershell
winget install GitHub.cli
```

## Time Estimate

- **With script**: ~5-7 minutes (mostly waiting for Render)
- **Without script**: ~10-15 minutes

## What Happens After

Once complete, your site will be live at:
- **Frontend**: https://ssoto130.github.io/hackathon-2025V-/
- **Backend**: Your Render URL

Every push to `main` automatically redeploys the frontend!
