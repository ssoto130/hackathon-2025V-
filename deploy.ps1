# Automated GitHub Pages Setup Script
# Run this to automate the deployment process

Write-Host "GitHub Pages Automated Setup" -ForegroundColor Green
Write-Host "==============================" -ForegroundColor Green
Write-Host ""

$owner = "ssoto130"
$repo = "hackathon-2025V-"
$siteUrl = "https://ssoto130.github.io/hackathon-2025V-/"

# Check for GitHub CLI
$hasGHCLI = $false
try {
    gh --version | Out-Null
    $hasGHCLI = $true
    Write-Host "GitHub CLI detected" -ForegroundColor Green
} catch {
    Write-Host "GitHub CLI not installed (optional)" -ForegroundColor Yellow
}

# Step 1: Enable GitHub Pages
Write-Host "`nStep 1: Enable GitHub Pages" -ForegroundColor Cyan
Write-Host "Opening GitHub Pages settings..." -ForegroundColor Yellow
Start-Process "https://github.com/$owner/$repo/settings/pages"
Write-Host "Please set Source to 'GitHub Actions' and click Save" -ForegroundColor Yellow
Read-Host "`nPress Enter when done"

# Step 2: Setup Render
Write-Host "`nStep 2: Setup Render Backend" -ForegroundColor Cyan
Write-Host "Opening Render signup..." -ForegroundColor Yellow
Start-Sleep -Seconds 1
Start-Process "https://dashboard.render.com/register"
Read-Host "`nPress Enter when logged into Render"

# Step 2A: Create Database
Write-Host "`nStep 2A: Create PostgreSQL Database" -ForegroundColor Cyan
Start-Process "https://dashboard.render.com/new/database"
Write-Host "Name: hackathon-db" -ForegroundColor Yellow
Write-Host "Plan: Free" -ForegroundColor Yellow
Write-Host "Click Create Database and copy Internal Database URL" -ForegroundColor Yellow
$databaseUrl = Read-Host "`nPaste Internal Database URL"

# Generate secret key
$secretKey = -join ((48..57) + (97..102) | Get-Random -Count 64 | ForEach-Object {[char]$_})
Write-Host "`nGenerated SECRET_KEY: $secretKey" -ForegroundColor Green

# Step 2B: Create Web Service
Write-Host "`nStep 2B: Create Web Service" -ForegroundColor Cyan
Start-Process "https://dashboard.render.com/create?type=web"
Write-Host "`nConnect repo: $repo" -ForegroundColor Yellow
Write-Host "Name: hackathon-backend" -ForegroundColor Yellow
Write-Host "Root Directory: backend" -ForegroundColor Yellow
Write-Host "Build: pip install -r requirements.txt" -ForegroundColor Yellow
Write-Host "Start: gunicorn app:app" -ForegroundColor Yellow
Write-Host "Plan: Free" -ForegroundColor Yellow
Write-Host "`nEnvironment Variables:" -ForegroundColor Yellow
Write-Host "SECRET_KEY=$secretKey" -ForegroundColor Green
Write-Host "DATABASE_URL=$databaseUrl" -ForegroundColor Green
Write-Host "FRONTEND_ORIGIN=https://ssoto130.github.io" -ForegroundColor Green
Write-Host "FLASK_DEBUG=False" -ForegroundColor Green
Write-Host "PORT=10000" -ForegroundColor Green
Read-Host "`nPress Enter when backend is deployed"

$backendUrl = Read-Host "Enter Render backend URL"

# Step 2C: Initialize Database
Write-Host "`nStep 2C: Initialize Database" -ForegroundColor Cyan
Write-Host "In Render Shell tab, run:" -ForegroundColor Yellow
Write-Host "flask init-db" -ForegroundColor Green
Write-Host "python load_db_from_json.py" -ForegroundColor Green
Read-Host "`nPress Enter when done"

# Step 3: Add GitHub Secret
Write-Host "`nStep 3: Add GitHub Secret" -ForegroundColor Cyan
if ($hasGHCLI) {
    Write-Host "Adding BACKEND_URL secret..." -ForegroundColor Yellow
    try {
        echo $backendUrl | gh secret set BACKEND_URL --repo "$owner/$repo"
        Write-Host "Secret added!" -ForegroundColor Green
    } catch {
        Write-Host "Failed. Add manually:" -ForegroundColor Yellow
        Start-Process "https://github.com/$owner/$repo/settings/secrets/actions/new"
        Write-Host "Name: BACKEND_URL" -ForegroundColor Yellow
        Write-Host "Value: $backendUrl" -ForegroundColor Yellow
        Read-Host "`nPress Enter when done"
    }
} else {
    Start-Process "https://github.com/$owner/$repo/settings/secrets/actions/new"
    Write-Host "Name: BACKEND_URL" -ForegroundColor Yellow
    Write-Host "Value: $backendUrl" -ForegroundColor Yellow
    Read-Host "`nPress Enter when done"
}

# Step 4: Trigger Deployment
Write-Host "`nStep 4: Trigger Deployment" -ForegroundColor Cyan
if ($hasGHCLI) {
    try {
        gh workflow run "deploy.yml" --repo "$owner/$repo"
        Write-Host "Workflow triggered!" -ForegroundColor Green
    } catch {
        Start-Process "https://github.com/$owner/$repo/actions"
        Write-Host "Manually run Deploy to GitHub Pages workflow" -ForegroundColor Yellow
    }
} else {
    Start-Process "https://github.com/$owner/$repo/actions"
    Write-Host "Click Deploy to GitHub Pages > Run workflow" -ForegroundColor Yellow
}

Write-Host "`nSetup Complete!" -ForegroundColor Green
Write-Host "Your site: $siteUrl" -ForegroundColor Green
Write-Host "Backend: $backendUrl" -ForegroundColor Green
Write-Host "`nWait 2 minutes for deployment" -ForegroundColor Yellow
Read-Host "`nPress Enter to open site"
Start-Process $siteUrl
