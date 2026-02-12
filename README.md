# ComplyAI - Cloud Deployment Guide

Deploy ComplyAI to the cloud and access it from any browser on any device.

---

## 🚀 Quick Cloud Deployment (Recommended)

### Option 1: Render.com (Easiest - 5 minutes)

**Best for:** Quick deployment, free tier with auto-Sleep

1. **Create account** at [render.com](https://render.com)
2. **Connect GitHub:**
   - Push this repo to GitHub
   - Go to Render Dashboard → New → Blueprint
   - Select your GitHub repo
3. **Deploy:** Click "Deploy" and wait ~3-5 minutes
4. **Access:** Render provides your public URLs automatically

**Cost:** Free tier available ($7-10/month for production)

---

### Option 2: Railway.app (Easiest Alternative - 5 minutes)

**Best for:** Simple, pay-as-you-go, GitHub auto-sync

1. **Create account** at [railway.app](https://railway.app)
2. **Connect GitHub:**
   - Login with GitHub
   - Select "New Project" → "Deploy from GitHub"
   - Choose this repository
3. **Deploy:** Railway auto-deploys on git push
4. **Access:** Get URLs from Railway dashboard

**Cost:** Free $5/month credit, then pay-as-you-go

---

### Option 3: Heroku (Traditional - 5 minutes)

**Note:** Heroku discontinued free tier, but still simple

1. **Install Heroku CLI:** [heroku.com/apps](https://www.heroku.com/apps)
2. **Setup:**
   ```
   heroku login
   heroku create complyai-yourname
   git push heroku main
   ```
3. **Access:** `https://complyai-yourname.herokuapp.com`

**Cost:** $7+/month

---

### Option 4: AWS/Google Cloud/Azure (Production-Grade)

Use Docker directly with container services:
- **AWS:** AWS ECS + CloudFront CDN
- **Google Cloud:** Cloud Run (runs containers serverless)
- **Azure:** Container Instances + App Service

These are more powerful but require more setup.

---

## 📋 Pre-Deployment Checklist

Before deploying anywhere:

- [ ] Push code to GitHub
- [ ] Update auth tokens in environment variables
- [ ] Test locally: `docker-compose up`

---

## 🔧 Environment Variables

These are set automatically by deployment platforms, but you can customize:

```
NEXT_PUBLIC_BACKEND_URL    # Frontend knows where backend is
ENABLE_AI_WORKER           # Enable background processing
ENABLE_EMAIL               # Email notifications
ENABLE_AUTH                # Authentication
AUTH_TOKEN                 # Secret token (auto-generated)
ENABLE_REDIS               # Caching (optional)
ENABLE_SMS                 # SMS notifications
```

---

## 📱 Access Anywhere

Once deployed:
- ✅ Works on Mac, Windows, Linux
- ✅ Works on iPhone, Android
- ✅ Works on any browser (Chrome, Safari, Firefox, Edge)
- ✅ Get public URL from cloud provider
- ✅ Share with team via link

---

## 🏠 Local Development (Mac/Linux/Windows)

### With Docker:
```bash
docker-compose up
```
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Docs: http://localhost:8000/docs

### Without Docker (Mac/Linux):
```bash
# Terminal 1 - Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend
npm install
npm run dev

# Terminal 3 - Worker
cd worker
pip install -r requirements.txt
python worker.py
```

---

## 🔍 Deployment Status

Check deployment logs:
- **Render:** Dashboard → Logs tab
- **Railway:** Dashboard → Logs
- **Heroku:** `heroku logs --tail`

---

## 📞 Support

If deployment fails:
1. Check cloud provider logs for error messages
2. Verify GitHub repo is public (for free deployments)
3. Ensure `.env` variables are properly set in cloud UI
4. Check that `docker-compose.yml` and Dockerfiles are in repo root

---

## 🎯 Next Steps

After deployment:
1. Share public URL with team
2. Monitor usage in cloud dashboard
3. Add custom domain (optional, through cloud provider)
4. Set up auto-backups if needed
