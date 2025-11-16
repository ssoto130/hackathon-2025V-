# Deployment Guide

## Overview
This project is split into two parts:
- **Frontend**: SvelteKit app deployed on GitHub Pages
- **Backend**: Flask API deployed on Render/Railway/PythonAnywhere

## Frontend Deployment (GitHub Pages)

### Prerequisites
- GitHub account
- Repository pushed to GitHub

### Steps

1. **Update the base path in `svelte.config.js`**:
   - If deploying to `https://username.github.io/repo-name`, change:
     ```javascript
     base: process.env.NODE_ENV === 'production' ? '/your-repo-name' : ''
     ```
   - If deploying to `https://username.github.io`, leave it empty:
     ```javascript
     base: ''
     ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Settings → Pages
   - Source: GitHub Actions

3. **Add Backend URL Secret**:
   - Settings → Secrets and variables → Actions
   - New repository secret
   - Name: `BACKEND_URL`
   - Value: Your backend URL (e.g., `https://your-app.onrender.com`)

4. **Push to main branch**:
   ```bash
   git add .
   git commit -m "Configure for GitHub Pages deployment"
   git push origin main
   ```

5. **Monitor deployment**:
   - Go to Actions tab in your repository
   - Watch the deployment workflow

## Backend Deployment (Render)

### Option 1: Render (Recommended - Free tier available)

1. **Create account** at [render.com](https://render.com)

2. **Create PostgreSQL Database**:
   - Dashboard → New → PostgreSQL
   - Name: `hackathon-db`
   - Free tier is fine for testing
   - Copy the Internal Database URL

3. **Create Web Service**:
   - Dashboard → New → Web Service
   - Connect your GitHub repository
   - Settings:
     - **Name**: `hackathon-backend`
     - **Root Directory**: `backend`
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`

4. **Add Environment Variables**:
   ```
   SECRET_KEY=<generate-a-random-secret>
   DATABASE_URL=<your-postgres-internal-url>
   FRONTEND_ORIGIN=https://yourusername.github.io
   FLASK_DEBUG=False
   PORT=10000
   ```

5. **Initialize Database**:
   - After first deployment, open Shell in Render dashboard
   - Run:
     ```bash
     flask init-db
     python load_db_from_json.py
     ```

6. **Copy your backend URL** (e.g., `https://hackathon-backend.onrender.com`)

### Option 2: Railway

1. **Create account** at [railway.app](https://railway.app)
2. **New Project** → Deploy from GitHub repo
3. **Add PostgreSQL** plugin
4. **Configure environment variables** (same as above)
5. **Deploy automatically** on push

### Option 3: PythonAnywhere (Free tier)

1. **Create account** at [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Upload code** via Git or file upload
3. **Create virtual environment** and install requirements
4. **Configure WSGI file** for Flask
5. **Set up MySQL database** (free tier includes MySQL)

## Local Development

### Frontend
```bash
cd frontend/coding-practice
npm install
cp .env.example .env
# Edit .env with your local backend URL (http://localhost:5000)
npm run dev
```

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your local settings
flask init-db
python load_db_from_json.py
python app.py
```

## Troubleshooting

### GitHub Pages shows 404
- Check that base path in `svelte.config.js` matches your repo name
- Ensure GitHub Pages is enabled and set to GitHub Actions

### Backend won't start
- Check environment variables are set correctly
- Ensure DATABASE_URL points to PostgreSQL (not SQLite)
- Check Render/Railway logs for errors

### Frontend can't connect to backend
- Verify BACKEND_URL secret in GitHub Actions
- Check CORS settings in backend allow your GitHub Pages domain
- Ensure backend is running and accessible

### Database errors
- Make sure you've run `flask init-db`
- Check DATABASE_URL format for PostgreSQL
- Verify database credentials

## Cost Estimates
- **GitHub Pages**: Free
- **Render Free Tier**: Free (spins down after 15 min inactivity)
- **Railway Free Tier**: $5 free credit monthly
- **PythonAnywhere Free**: Free (limited resources)

## Updating Content
To update the content (questions, courses, etc.):
1. Edit JSON files in `backend/config/`
2. Deploy backend changes
3. Run `python load_db_from_json.py` in backend shell
