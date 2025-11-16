#!/usr/bin/env pwsh
# Automated GitHub Pages Setup Script

Write-Host "🚀 GitHub Pages Automated Setup" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""

$owner = "ssoto130"
$repo = "hackathon-2025V-"

# Function to check if gh CLI is installed
function Test-GitHubCLI {
    try {
        gh --version | Out-Null
        return $true
    } catch {
        return $false
    }
}

# Step 1: Enable GitHub Pages
Write-Host "📄 Step 1: Enabling GitHub Pages..." -ForegroundColor Cyan

if (Test-GitHubCLI) {
    Write-Host "✓ GitHub CLI detected" -ForegroundColor Green
    
    # Check if authenticated
    $authStatus = gh auth status 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠ Not authenticated. Logging in..." -ForegroundColor Yellow
        gh auth login
    }
    
    Write-Host "✓ Opening GitHub Pages settings..." -ForegroundColor Green
    Start-Process "https://github.com/$owner/$repo/settings/pages"
    Write-Host ""
    Write-Host "Please manually:" -ForegroundColor Yellow
    Write-Host "  1. Set Source to 'GitHub Actions'" -ForegroundColor Yellow
    Write-Host "  2. Click Save" -ForegroundColor Yellow
    
} else {
    Write-Host "⚠ GitHub CLI not installed" -ForegroundColor Yellow
    Write-Host "Opening browser manually..." -ForegroundColor Yellow
    Start-Process "https://github.com/$owner/$repo/settings/pages"
    Write-Host ""
    Write-Host "Please manually:" -ForegroundColor Yellow
    Write-Host "  1. Set Source to 'GitHub Actions'" -ForegroundColor Yellow
    Write-Host "  2. Click Save" -ForegroundColor Yellow
}

Read-Host "`nPress Enter when GitHub Pages is enabled"

# Step 2: Setup Render
Write-Host "`n🔧 Step 2: Setting up Render..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Opening Render signup/login..." -ForegroundColor Yellow
Start-Sleep -Seconds 1
Start-Process "https://dashboard.render.com/register"

Read-Host "`nPress Enter when you're logged into Render"

# Step 2A: Create Database
Write-Host "`n📊 Step 2A: Creating PostgreSQL Database..." -ForegroundColor Cyan
Start-Process "https://dashboard.render.com/new/database"
Write-Host ""
Write-Host "In the browser:" -ForegroundColor Yellow
Write-Host "  1. Name: hackathon-db" -ForegroundColor Yellow
Write-Host "  2. Plan: Free" -ForegroundColor Yellow
Write-Host "  3. Click 'Create Database'" -ForegroundColor Yellow
Write-Host "  4. Wait for it to provision (~2 min)" -ForegroundColor Yellow
Write-Host "  5. Copy the 'Internal Database URL'" -ForegroundColor Yellow

$databaseUrl = Read-Host "`nPaste the Internal Database URL here"

# Generate secret key
$secretKey = -join ((48..57) + (97..102) | Get-Random -Count 64 | ForEach-Object {[char]$_})
Write-Host "`n✓ Generated SECRET_KEY: $secretKey" -ForegroundColor Green

# Step 2B: Create Web Service
Write-Host "`n🌐 Step 2B: Creating Web Service..." -ForegroundColor Cyan
Start-Process "https://dashboard.render.com/create?type=web"
Write-Host ""
Write-Host "In the browser:" -ForegroundColor Yellow
Write-Host "  1. Connect GitHub repository: $repo" -ForegroundColor Yellow
Write-Host "  2. Name: hackathon-backend" -ForegroundColor Yellow
Write-Host "  3. Root Directory: backend" -ForegroundColor Yellow
Write-Host "  4. Build Command: pip install -r requirements.txt" -ForegroundColor Yellow
Write-Host "  5. Start Command: gunicorn app:app" -ForegroundColor Yellow
Write-Host "  6. Plan: Free" -ForegroundColor Yellow
Write-Host ""
Write-Host "Environment Variables to add:" -ForegroundColor Yellow
Write-Host "  SECRET_KEY=$secretKey" -ForegroundColor Green
Write-Host "  DATABASE_URL=$databaseUrl" -ForegroundColor Green
Write-Host "  FRONTEND_ORIGIN=https://ssoto130.github.io" -ForegroundColor Green
Write-Host "  FLASK_DEBUG=False" -ForegroundColor Green
Write-Host "  PORT=10000" -ForegroundColor Green
Write-Host ""
Write-Host "Click 'Create Web Service' and wait for deployment (~5 min)" -ForegroundColor Yellow

Read-Host "`nPress Enter when backend is deployed"

$backendUrl = Read-Host "Enter your Render backend URL (e.g., https://hackathon-backend-xxxx.onrender.com)"

# Step 2C: Initialize Database
Write-Host "`n🗄️ Step 2C: Initializing Database..." -ForegroundColor Cyan
Write-Host ""
Write-Host "In Render dashboard:" -ForegroundColor Yellow
Write-Host "  1. Click your web service" -ForegroundColor Yellow
Write-Host "  2. Click 'Shell' tab (top right)" -ForegroundColor Yellow
Write-Host "  3. Run these commands:" -ForegroundColor Yellow
Write-Host "     flask init-db" -ForegroundColor Green
Write-Host "     python load_db_from_json.py" -ForegroundColor Green

Read-Host "`nPress Enter when database is initialized"

# Step 3: Add GitHub Secret
Write-Host "`n🔐 Step 3: Adding GitHub Secret..." -ForegroundColor Cyan

if (Test-GitHubCLI) {
    Write-Host "Adding BACKEND_URL secret via GitHub CLI..." -ForegroundColor Yellow
    try {
        echo $backendUrl | gh secret set BACKEND_URL --repo "$owner/$repo"
        Write-Host "✓ Secret added successfully!" -ForegroundColor Green
    } catch {
        Write-Host "⚠ Failed to add secret automatically" -ForegroundColor Yellow
        Write-Host "Please add manually:" -ForegroundColor Yellow
        Start-Process "https://github.com/$owner/$repo/settings/secrets/actions/new"
        Write-Host "  Name: BACKEND_URL" -ForegroundColor Yellow
        Write-Host "  Value: $backendUrl" -ForegroundColor Yellow
        Read-Host "`nPress Enter when secret is added"
    }
} else {
    Write-Host "Opening GitHub secrets page..." -ForegroundColor Yellow
    Start-Process "https://github.com/$owner/$repo/settings/secrets/actions/new"
    Write-Host ""
    Write-Host "Add this secret:" -ForegroundColor Yellow
    Write-Host "  Name: BACKEND_URL" -ForegroundColor Yellow
    Write-Host "  Value: $backendUrl" -ForegroundColor Yellow
    Read-Host "`nPress Enter when secret is added"
}

# Step 4: Trigger Deployment
Write-Host "`n🚀 Step 4: Triggering Deployment..." -ForegroundColor Cyan

if (Test-GitHubCLI) {
    Write-Host "Triggering workflow via GitHub CLI..." -ForegroundColor Yellow
    try {
        gh workflow run "deploy.yml" --repo "$owner/$repo"
        Write-Host "✓ Workflow triggered!" -ForegroundColor Green
        Write-Host "✓ Opening Actions page..." -ForegroundColor Green
        Start-Process "https://github.com/$owner/$repo/actions"
    } catch {
        Write-Host "⚠ Failed to trigger automatically" -ForegroundColor Yellow
        Start-Process "https://github.com/$owner/$repo/actions"
        Write-Host "Please manually click 'Deploy to GitHub Pages' → 'Run workflow'" -ForegroundColor Yellow
    }
} else {
    Start-Process "https://github.com/$owner/$repo/actions"
    Write-Host "Please manually:" -ForegroundColor Yellow
    Write-Host "  1. Click 'Deploy to GitHub Pages'" -ForegroundColor Yellow
    Write-Host "  2. Click 'Run workflow' then 'Run workflow'" -ForegroundColor Yellow
}

Write-Host "`n" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════" -ForegroundColor Green
Write-Host "🎉 Setup Complete!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "Your site will be live at:" -ForegroundColor Cyan
Write-Host "  https://ssoto130.github.io/hackathon-2025V-/" -ForegroundColor Green
Write-Host ""
Write-Host "Backend URL:" -ForegroundColor Cyan
Write-Host "  $backendUrl" -ForegroundColor Green
Write-Host ""
Write-Host "Wait ~2 minutes for deployment to complete." -ForegroundColor Yellow
Write-Host ""

Read-Host "Press Enter to open your site"
$finalUrl = "https://ssoto130.github.io/hackathon-2025V-/"
Start-Process $finalUrl
