# 🚀 Quick Deployment Guide

## Automated Setup Checklist

### ✅ Completed
- [x] Frontend configured for GitHub Pages
- [x] GitHub Actions workflow created
- [x] Backend configured with Gunicorn and PostgreSQL support
- [x] CORS configured for production
- [x] Code pushed to GitHub

### 📋 Next Steps (5 minutes)

#### 1. Enable GitHub Pages
Visit: https://github.com/ssoto130/hackathon-2025V-/settings/pages
- **Source**: Select "GitHub Actions"
- Click Save

#### 2. Deploy Backend on Render (Free)

**A. Create Database:**
1. Go to: https://dashboard.render.com/new/database
2. Settings:
   - Name: `hackathon-db`
   - Plan: Free
3. Wait 2 minutes, then **copy Internal Database URL**

**B. Create Web Service:**
1. Go to: https://dashboard.render.com/create?type=web
2. Connect GitHub: `hackathon-2025V-`
3. Settings:
   - Name: `hackathon-backend`
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: Free

4. Add Environment Variables:
```
SECRET_KEY=12b3ffaf8dc898158dc1d1e991f35bdad8d7512ac17cd4f9a981b24c4bb19dfb
DATABASE_URL=[paste Internal Database URL from step A]
FRONTEND_ORIGIN=https://ssoto130.github.io
FLASK_DEBUG=False
PORT=10000
```

5. Click **Create Web Service** (wait ~5 minutes)

**C. Initialize Database:**
1. In Render dashboard, click **Shell**
2. Run:
```bash
flask init-db
python load_db_from_json.py
```

**D. Copy Backend URL** (e.g., `https://hackathon-backend-xxxx.onrender.com`)

#### 3. Add Backend URL to GitHub
Visit: https://github.com/ssoto130/hackathon-2025V-/settings/secrets/actions/new
- **Name**: `BACKEND_URL`
- **Value**: Your Render URL from step 2D

#### 4. Deploy Frontend
Visit: https://github.com/ssoto130/hackathon-2025V-/actions
- Click **Deploy to GitHub Pages**
- Click **Run workflow** → **Run workflow**
- Wait ~2 minutes

### 🎉 Done!
Your site will be live at: **https://ssoto130.github.io/hackathon-2025V-/**

---

## Troubleshooting

### Frontend 404 Error
- Verify GitHub Pages is enabled and set to "GitHub Actions"
- Check base path in `svelte.config.js` matches repo name

### Backend Connection Failed
- Verify `BACKEND_URL` secret is set in GitHub
- Check backend is running on Render
- Verify CORS settings allow `https://ssoto130.github.io`

### Database Errors
- Make sure you ran `flask init-db` and `python load_db_from_json.py`
- Check DATABASE_URL is the Internal URL (not External)

---

## Local Development

### Run Frontend:
```powershell
cd "frontend/coding-practice"
npm install
npm run dev
```
Visit: http://localhost:5173

### Run Backend:
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Create .env file with local settings
python app.py
```
Visit: http://localhost:5000

---

## Estimated Costs
- **GitHub Pages**: Free
- **Render Free Tier**: Free (backend sleeps after 15 min inactivity)
- **Total**: $0/month

**Note**: Render free tier spins down after inactivity. First request after sleeping takes ~30 seconds to wake up.
