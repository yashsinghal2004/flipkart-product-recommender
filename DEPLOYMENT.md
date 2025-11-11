# Deployment Guide for Flipkart Product Assistant

## Overview
This is a Flask application that requires:
- Python 3.10+
- Environment variables (AstraDB, Groq API)
- Vector database connection
- AI model access

## Deployment Options

### Option 1: Render (Recommended) ⭐

**Steps:**
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name:** flipkart-product-assistant
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
5. Add Environment Variables:
   - `ASTRA_DB_API_ENDPOINT`
   - `ASTRA_DB_APPLICATION_TOKEN`
   - `ASTRA_DB_KEYSPACE`
   - `GROQ_API_KEY`
6. Click "Create Web Service"

**Pros:**
- Free tier available
- Easy Flask deployment
- Automatic HTTPS
- Good for Python apps

---

### Option 2: Railway

**Steps:**
1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Python and installs dependencies
5. Add environment variables in the "Variables" tab
6. Deploy!

**Pros:**
- Very easy setup
- Free tier with $5 credit
- Auto-deploys on git push

---

### Option 3: Vercel ⚠️ (Not Recommended for Flask)

**Note:** Vercel is designed for static sites and serverless functions. Flask apps require significant modifications.

**Limitations:**
- Flask needs to be converted to serverless functions
- Cold starts may cause delays
- Complex setup with state management
- Not ideal for long-running processes

**Better Alternatives:** Use Render or Railway instead for Flask apps.

---

### Option 4: Heroku

**Steps:**
1. Install Heroku CLI
2. Run: `heroku create your-app-name`
3. Add environment variables: `heroku config:set KEY=value`
4. Deploy: `git push heroku main`

**Note:** Heroku free tier is no longer available.

---

### Option 5: Docker + Cloud Provider

Deploy using the existing Dockerfile to:
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform

---

## Environment Variables Required

Make sure to set these in your deployment platform:

```
ASTRA_DB_API_ENDPOINT=your_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_token
ASTRA_DB_KEYSPACE=your_keyspace
GROQ_API_KEY=your_groq_key
```

---

## Important Notes

1. **Vector Database:** Ensure your AstraDB instance is accessible from the deployment platform
2. **API Keys:** Never commit API keys to Git - use environment variables
3. **Dependencies:** All Python packages in `requirements.txt` will be installed
4. **Port:** The app runs on port 5000 by default (most platforms auto-detect)

---

## Quick Deploy Commands

### Render
```bash
# Just push to GitHub and connect to Render
git push origin main
```

### Railway
```bash
railway login
railway init
railway up
```

### Vercel
```bash
vercel
```

---

## Testing Locally Before Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export ASTRA_DB_API_ENDPOINT=your_value
export ASTRA_DB_APPLICATION_TOKEN=your_value
export ASTRA_DB_KEYSPACE=your_value
export GROQ_API_KEY=your_value

# Run the app
python app.py
```

