# English to Kannada Translator - Deployment Guide

## Deploying to Render

This project is configured for easy deployment on Render.com. 

### Prerequisites
- A Render.com account
- GitHub repository linked to Render

### Deployment Steps

1. **Connect Repository to Render**
   - Go to https://render.com
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

2. **Configuration**
   The following files are automatically detected:
   - `runtime.txt` - Specifies Python 3.11
   - `Procfile` - For Heroku-style deployment (fallback)
   - `render.yaml` - Main Render configuration
   - `requirements.txt` - Python dependencies

3. **Deploy**
   - Click "Deploy"
   - Render will:
     - Detect this as a Python project
     - Install dependencies from requirements.txt
     - Start the app with Gunicorn

### Environment Variables (if needed)
- `PORT` - Automatically set by Render (default: 3000)
- Add any custom variables in Render dashboard

### Important Notes
- The app runs on `0.0.0.0` to work with Render's port binding
- Gunicorn is used as the production WSGI server
- Deep-translator requires internet access for Google Translate API

### Local Development
```bash
# Create virtual environment
python -m venv env

# Activate environment
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

Visit `http://localhost:5000` to test locally.
