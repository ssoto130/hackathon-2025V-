# SIMPLE 3-STEP DEPLOYMENT

## Step 1: Enable GitHub Pages (30 seconds)

1. Go to: https://github.com/ssoto130/hackathon-2025V-/settings/pages
2. Under "Source", select: **GitHub Actions** (not "Deploy from a branch")
3. Click Save

That's it! No other settings needed.

---

## Step 2: Deploy Backend on Render (4 minutes)

### A. Create Database
1. Go to: https://dashboard.render.com/new/database
2. Sign up/login with GitHub
3. Settings:
   - **Name**: `hackathon-db`
   - **Plan**: Free
4. Click **Create Database**
5. Wait ~2 minutes
6. **Copy the "Internal Database URL"** (starts with `postgresql://`)

### B. Create Web Service
1. Go to: https://dashboard.render.com/create?type=web
2. Click **Connect account** and authorize GitHub
3. Select repository: **hackathon-2025V-**
4. Settings:
   - **Name**: `hackathon-backend`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

5. **Environment Variables** - Click "Add Environment Variable" for each:
   ```
   SECRET_KEY = (paste this: 12b3ffaf8dc898158dc1d1e991f35bdad8d7512ac17cd4f9a981b24c4bb19dfb)
   DATABASE_URL = (paste your Internal Database URL from step A)
   FRONTEND_ORIGIN = https://ssoto130.github.io
   FLASK_DEBUG = False
   PORT = 10000
   ```

6. Click **Create Web Service**
7. Wait ~5 minutes for deployment
8. **Copy your backend URL** (e.g., `https://hackathon-backend-xxxx.onrender.com`)

### C. Initialize Database
1. In Render dashboard, click your web service
2. Click **Shell** tab (top right)
3. Type these commands one at a time:
   ```bash
   flask init-db
   python load_db_from_json.py
   ```
4. Close the shell

---

## Step 3: Connect Frontend to Backend (1 minute)

1. Go to: https://github.com/ssoto130/hackathon-2025V-/settings/secrets/actions/new
2. Add a new secret:
   - **Name**: `BACKEND_URL`
   - **Value**: Your Render backend URL from Step 2B
3. Click **Add secret**

4. Go to: https://github.com/ssoto130/hackathon-2025V-/actions
5. Click **Deploy to GitHub Pages** workflow
6. Click **Run workflow** (button on right)
7. Click green **Run workflow** button

---

## Done!

Wait ~2 minutes, then visit:
**https://ssoto130.github.io/hackathon-2025V-/**

---

## Troubleshooting

### "Build failed" in GitHub Actions
- Check that `BACKEND_URL` secret is set correctly
- Make sure it starts with `https://`

### Frontend loads but can't connect to backend
- Verify backend is running on Render (should show "Live")
- Check you ran `flask init-db` in the Shell
- Verify `FRONTEND_ORIGIN` in Render is `https://ssoto130.github.io`

### Backend shows errors
- Check all 5 environment variables are set in Render
- Verify `DATABASE_URL` is the Internal URL (not External)
- Restart the service in Render

---

## Quick Links

- GitHub Pages: https://github.com/ssoto130/hackathon-2025V-/settings/pages
- Render Dashboard: https://dashboard.render.com
- GitHub Actions: https://github.com/ssoto130/hackathon-2025V-/actions
- GitHub Secrets: https://github.com/ssoto130/hackathon-2025V-/settings/secrets/actions
- Your Site: https://ssoto130.github.io/hackathon-2025V-/
