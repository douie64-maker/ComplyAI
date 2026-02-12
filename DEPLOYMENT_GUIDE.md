# ComplyAI Cloud Deployment - Step-by-Step Guides

## 🎯 Pick Your Platform

### ⚡ Render.com (Recommended - Free with auto-sleep)

**Time:** 5 minutes

1. **Prepare your repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Blueprint"
   - Connect your GitHub account
   - Select this repository
   - Click "Deploy"

3. **Monitor deployment:**
   - Render automatically pulls `render.yaml`
   - Builds all 3 services (backend, frontend, worker)
   - Assigns public URLs in ~3-5 minutes

4. **Access application:**
   - Render dashboard shows frontend URL
   - Frontend auto-configured to use backend URL
   - Share frontend URL with team

**Free tier:** One free instance (sleeps after 15 min inactivity, wakes on visit)

---

### 🚂 Railway.app (Simplest - Pay-as-you-go)

**Time:** 5 minutes

1. **Push to GitHub:**
   ```bash
   git push origin main
   ```

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "GitHub Repo"
   - Choose this repository
   - Railway auto-runs `railway.json` config

3. **Auto-deployment:**
   - Any `git push` triggers automatic redeploy
   - View logs in dashboard
   - Services start within seconds

4. **Get your URLs:**
   - Dashboard shows each service URL
   - Frontend automatically finds backend
   - Share with team

**Free tier:** $5/month credit, then pay-as-you-go (~$0.001/hour)

---

### 🔵 Google Cloud Run (Production-Grade)

**Time:** 15 minutes

1. **Install Google Cloud CLI:**
   ```bash
   # Mac
   brew install --cask google-cloud-sdk
   
   # Linux
   sudo apt install google-cloud-sdk
   
   # Windows - Download from: cloud.google.com/sdk/docs/install-options
   ```

2. **Setup Google Cloud:**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

3. **Deploy backend:**
   ```bash
   cd backend
   gcloud run deploy complyai-backend --source . --port 8000 --allow-unauthenticated
   ```
   - Copy the service URL

4. **Deploy frontend:**
   ```bash
   cd frontend
   gcloud run deploy complyai-frontend --source . \
     --port 3000 \
     --allow-unauthenticated \
     --set-env-vars NEXT_PUBLIC_BACKEND_URL=BACKEND_URL
   ```
   - Replace `BACKEND_URL` with URL from step 3

5. **Access:**
   - Use frontend URL from Cloud Run console
   - Already configured to connect to backend

**Free tier:** 2 million requests/month, auto-scales

---

### ☁️ AWS Lightsail (Simple AWS)

**Time:** 20 minutes

1. **Create Lightsail container service:**
   - Go to [lightsail.aws.amazon.com](https://lightsail.aws.amazon.com)
   - Click "Containers" → "Create container service"
   - Choose plan ($5+/month)

2. **Upload Docker images:**
   ```bash
   # Build locally
   docker build -t complyai-backend:latest ./backend
   docker build -t complyai-frontend:latest ./frontend
   
   # Push to AWS container registry
   aws lightsail push-container-image \
     --service-name complyai \
     --label complyai-backend \
     --image complyai-backend:latest
   
   aws lightsail push-container-image \
     --service-name complyai \
     --label complyai-frontend \
     --image complyai-frontend:latest
   ```

3. **Create container deployment:**
   - Use Lightsail console to configure containers
   - Set environment variables
   - Enable public endpoint

4. **Access:**
   - Lightsail provides public URL
   - Auto-scales based on traffic

---

### 🟣 Azure Container Instances (Production)

**Time:** 15 minutes

1. **Install Azure CLI:**
   ```bash
   # Mac
   brew install azure-cli
   
   # Linux
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   
   # Windows
   # Download from: aka.ms/azure-cli
   ```

2. **Login and setup:**
   ```bash
   az login
   az group create --name complyai --location eastus
   az acr create --resource-group complyai --name complyairegistry --sku Basic
   ```

3. **Build and push images:**
   ```bash
   az acr build --registry complyairegistry --image complyai-backend:latest ./backend
   az acr build --registry complyairegistry --image complyai-frontend:latest ./frontend
   ```

4. **Deploy containers:**
   ```bash
   az container create \
     --resource-group complyai \
     --name complyai-app \
     --image complyairegistry.azurecr.io/complyai-frontend:latest \
     --ports 80 3000 \
     --environment-variables NEXT_PUBLIC_BACKEND_URL="https://your-backend-url"
   ```

5. **Get public IP:**
   ```bash
   az container show --resource-group complyai --name complyai-app --query ipAddress.ip
   ```

---

## 🔑 Environment Variables (All Platforms)

Set these in your cloud platform's dashboard:

```
NEXT_PUBLIC_BACKEND_URL        [Auto-set by platform or set manually]
ENABLE_AI_WORKER               true
ENABLE_EMAIL                   true
ENABLE_AUTH                    true
AUTH_TOKEN                     [Generate random string]
ENABLE_REDIS                   true
ENABLE_SMS                      true
```

---

## 📊 Platform Comparison

| Platform | Setup Time | Cost | Auto-Deploy | Scale |
|----------|-----------|------|------------|-------|
| **Render** | 5 min | Free (limits) | ✅ GitHub | ⭐⭐⭐ |
| **Railway** | 5 min | $5/mo + pay-go | ✅ GitHub | ⭐⭐⭐ |
| **Google Cloud Run** | 15 min | Free tier large | ✅ CLI | ⭐⭐⭐⭐ |
| **AWS Lightsail** | 20 min | $5+/mo | ❌ Manual | ⭐⭐⭐ |
| **Azure** | 20 min | $10+/mo | ❌ Manual | ⭐⭐⭐⭐ |
| **Heroku** | 10 min | $7+/mo | ✅ GitHub | ⭐⭐ |

---

## 🎯 My Recommendation

**For fastest deployment:**
→ Use **Railway.app** (most automated, easiest GitHub sync)

**For completely free:**
→ Use **Render.com** (free tier works, sleeps on inactivity)

**For production use:**
→ Use **Google Cloud Run** or **AWS** (auto-scale, pay per use)

---

## ✅ Verification After Deployment

1. **Frontend loads?**
   - Visit the frontend URL
   - Page should load without errors

2. **Backend connected?**
   - Open browser console (F12)
   - Should see no API errors
   - Data operations should work

3. **Check logs:**
   - View platform logs for any errors
   - Debug environment variable issues

---

## 🚀 Going Live

1. Add custom domain (domain registrar settings)
2. Enable HTTPS (cloud platforms do this automatically)
3. Add team email to platform notifications
4. Set up backups (optional, for production)
5. Share frontend URL with users

---

## 💡 Pro Tips

- **Domain:** Route your domain to cloud provider URL
- **Monitoring:** Enable logs/alerts in cloud dashboard
- **Updates:** Push code changes to auto-redeploy
- **Secrets:** Use platform's secret manager, never commit `.env`
- **Database:** If needed, cloud providers offer managed databases

---

## ❓ Troubleshooting

**"Port already in use"?**
- Cloud platforms assign ports automatically, this shouldn't happen

**"CORS errors"?**
- Backend has CORS configured for all origins
- If still failing, check `NEXT_PUBLIC_BACKEND_URL` env var

**"Backend not found"?**
- Verify backend service is running in platform dashboard
- Check port is exposed (usually 8000)
- Verify environment variables are set

**"Can't connect from outside"?**
- Most free platforms have IP restrictions
- Upgrade to production tier if needed
- Or use VPN-allowed URLs

---

## 📞 Need More Help?

Check platform documentation:
- [Render Docs](https://render.com/docs)
- [Railway Docs](https://docs.railway.app)
- [Google Cloud Run Docs](https://cloud.google.com/run/docs)
- [AWS Lightsail Docs](https://docs.aws.amazon.com/lightsail)
