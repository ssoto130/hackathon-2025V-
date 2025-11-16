"""
Automated GitHub Pages + Render Deployment Script
Run: python automate_deploy.py
"""

import webbrowser
import secrets
import time
import subprocess
import sys

print("=" * 60)
print("🚀 AUTOMATED DEPLOYMENT SCRIPT")
print("=" * 60)
print()

OWNER = "ssoto130"
REPO = "hackathon-2025V-"
SITE_URL = f"https://{OWNER}.github.io/{REPO}/"

# Check if gh CLI is available
has_gh_cli = False
try:
    subprocess.run(["gh", "--version"], capture_output=True, check=True)
    has_gh_cli = True
    print("✓ GitHub CLI detected")
except:
    print("⚠ GitHub CLI not found (will use browser)")

print()

# Step 1: Enable GitHub Pages
print("📄 STEP 1: Enable GitHub Pages")
print("-" * 60)
pages_url = f"https://github.com/{OWNER}/{REPO}/settings/pages"
print(f"Opening: {pages_url}")
webbrowser.open(pages_url)
print()
print("In the browser:")
print("  1. Set 'Source' to: GitHub Actions")
print("  2. Click 'Save'")
input("\n✓ Press Enter when GitHub Pages is enabled...")
print()

# Step 2: Render Setup
print("🔧 STEP 2: Deploy Backend on Render")
print("-" * 60)

# Step 2A: Create Database
print("\n📊 Step 2A: Create Database")
db_url = "https://dashboard.render.com/new/database"
print(f"Opening: {db_url}")
webbrowser.open(db_url)
time.sleep(1)
print()
print("In the browser:")
print("  1. Sign up/login with GitHub")
print("  2. Name: hackathon-db")
print("  3. Plan: Free")
print("  4. Click 'Create Database'")
print("  5. Wait ~2 minutes for provisioning")
print("  6. Copy the 'Internal Database URL'")
print()
database_url = input("Paste Internal Database URL here: ").strip()
print()

# Generate SECRET_KEY
secret_key = secrets.token_hex(32)
print(f"✓ Generated SECRET_KEY: {secret_key}")
print()

# Step 2B: Create Web Service
print("🌐 Step 2B: Create Web Service")
service_url = "https://dashboard.render.com/create?type=web"
print(f"Opening: {service_url}")
webbrowser.open(service_url)
time.sleep(1)
print()
print("In the browser:")
print(f"  1. Connect repository: {REPO}")
print("  2. Name: hackathon-backend")
print("  3. Root Directory: backend")
print("  4. Build Command: pip install -r requirements.txt")
print("  5. Start Command: gunicorn app:app")
print("  6. Plan: Free")
print()
print("Add these Environment Variables:")
print(f"  SECRET_KEY = {secret_key}")
print(f"  DATABASE_URL = {database_url}")
print(f"  FRONTEND_ORIGIN = https://{OWNER}.github.io")
print("  FLASK_DEBUG = False")
print("  PORT = 10000")
print()
input("✓ Press Enter when backend is deployed (~5 min)...")
print()
backend_url = input("Enter your Render backend URL (e.g., https://hackathon-backend-xxxx.onrender.com): ").strip()
print()

# Step 2C: Initialize Database
print("🗄️ Step 2C: Initialize Database")
print()
print("In Render dashboard:")
print("  1. Click your web service")
print("  2. Click 'Shell' tab (top right)")
print("  3. Run: flask init-db")
print("  4. Run: python load_db_from_json.py")
input("\n✓ Press Enter when database is initialized...")
print()

# Step 3: Add GitHub Secret
print("🔐 STEP 3: Add GitHub Secret")
print("-" * 60)

if has_gh_cli:
    print("Attempting to add secret via GitHub CLI...")
    try:
        result = subprocess.run(
            ["gh", "secret", "set", "BACKEND_URL", "--body", backend_url, "--repo", f"{OWNER}/{REPO}"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✓ Secret added successfully!")
    except subprocess.CalledProcessError as e:
        print("⚠ Failed to add secret via CLI")
        print(f"Error: {e.stderr}")
        secrets_url = f"https://github.com/{OWNER}/{REPO}/settings/secrets/actions/new"
        print(f"\nOpening: {secrets_url}")
        webbrowser.open(secrets_url)
        print()
        print("Add manually:")
        print("  Name: BACKEND_URL")
        print(f"  Value: {backend_url}")
        input("\n✓ Press Enter when secret is added...")
else:
    secrets_url = f"https://github.com/{OWNER}/{REPO}/settings/secrets/actions/new"
    print(f"Opening: {secrets_url}")
    webbrowser.open(secrets_url)
    time.sleep(1)
    print()
    print("Add this secret:")
    print("  Name: BACKEND_URL")
    print(f"  Value: {backend_url}")
    input("\n✓ Press Enter when secret is added...")

print()

# Step 4: Trigger Deployment
print("🚀 STEP 4: Trigger Deployment")
print("-" * 60)

if has_gh_cli:
    print("Triggering workflow via GitHub CLI...")
    try:
        subprocess.run(
            ["gh", "workflow", "run", "deploy.yml", "--repo", f"{OWNER}/{REPO}"],
            check=True
        )
        print("✓ Workflow triggered!")
    except subprocess.CalledProcessError:
        print("⚠ Failed to trigger automatically")
        actions_url = f"https://github.com/{OWNER}/{REPO}/actions"
        print(f"Opening: {actions_url}")
        webbrowser.open(actions_url)
        print()
        print("Manually trigger:")
        print("  1. Click 'Deploy to GitHub Pages'")
        print("  2. Click 'Run workflow' > 'Run workflow'")
else:
    actions_url = f"https://github.com/{OWNER}/{REPO}/actions"
    print(f"Opening: {actions_url}")
    webbrowser.open(actions_url)
    time.sleep(1)
    print()
    print("Manually trigger:")
    print("  1. Click 'Deploy to GitHub Pages'")
    print("  2. Click 'Run workflow' > 'Run workflow'")

print()
print("=" * 60)
print("🎉 SETUP COMPLETE!")
print("=" * 60)
print()
print(f"Frontend: {SITE_URL}")
print(f"Backend:  {backend_url}")
print()
print("Wait ~2 minutes for deployment to complete.")
print()

input("Press Enter to open your site...")
webbrowser.open(SITE_URL)

print()
print("✓ Done! Your site should be loading now.")
print()
