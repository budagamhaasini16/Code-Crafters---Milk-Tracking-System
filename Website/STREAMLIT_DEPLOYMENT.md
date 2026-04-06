# Streamlit Deployment Guide - Milk Tracking System

## 🚀 Quick Start

### 1. **Local Installation & Testing**

```bash
# Navigate to project directory
cd milk-tracking-system

# Install Streamlit dependencies
pip install -r streamlit_requirements.txt

# Run the app locally
streamlit run streamlit_app.py
```

The app will be available at: **http://localhost:8501**

---

## 📝 Demo Credentials

### Farmer Account
- **Email:** farmer@milktrack.com
- **Password:** Demo@123
- **View:** Personal farm data, collections, payments, quality tests

### Staff Account
- **Email:** staff@milktrack.com
- **Password:** Demo@123
- **View:** Collection center operations, staff dashboard

### Admin Account
- **Email:** admin@milktrack.com
- **Password:** Demo@123
- **View:** System-wide analytics, all collections data

---

## 🌐 Deploy to Streamlit Cloud

### Option 1: Streamlit Cloud (Free & Easiest)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Streamlit deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `milk-tracking-system`
   - Main file path: `streamlit_app.py`
   - Click Deploy

3. **Your app will be live at:** `https://[username]-milk-tracking-system.streamlit.app`

---

## 🐳 Deploy with Docker

### Create Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY streamlit_requirements.txt .
RUN pip install -r streamlit_requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py"]
```

### Build & Run Docker Container

```bash
# Build image
docker build -t milk-tracking-app .

# Run container
docker run -p 8501:8501 milk-tracking-app
```

Access at: **http://localhost:8501**

---

## ☁️ Deploy to Cloud Platforms

### AWS Elastic Beanstalk

1. Create `.ebextensions/streamlit.config`:
   ```yaml
   option_settings:
     aws:elasticbeanstalk:container:python:
       WSGIPath: streamlit_app.py
   ```

2. Deploy:
   ```bash
   eb init -p python-3.10
   eb create milk-tracking-prod
   eb deploy
   ```

### Heroku

1. Create `Procfile`:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. Deploy:
   ```bash
   heroku create milk-tracking-system
   git push heroku main
   ```

### Google Cloud Run

1. Build image:
   ```bash
   gcloud builds submit --tag gcr.io/[PROJECT-ID]/milk-tracking-system
   ```

2. Deploy:
   ```bash
   gcloud run deploy milk-tracking-system \
     --image gcr.io/[PROJECT-ID]/milk-tracking-system \
     --platform managed \
     --port 8501
   ```

### Azure App Service

1. Connect repository
2. Set startup command: `streamlit run streamlit_app.py --server.port=8000`
3. Deploy via GitHub Actions

---

## 🔒 Security for Production

### 1. Environment Variables
Create `.streamlit/secrets.toml`:
```toml
[auth]
admin_password = "your_secure_password_here"
api_key = "your_api_key"
```

Access in code:
```python
password = st.secrets["auth"]["admin_password"]
```

### 2. HTTPS/SSL
- Streamlit Cloud: ✅ Automatic
- Heroku: ✅ Automatic
- AWS/Azure/GCP: Configure SSL certificate

### 3. Rate Limiting
Add to `streamlit_app.py`:
```python
from streamlit_throttler import throttle

@throttle(calls=100, period=60)
def api_call():
    pass
```

---

## 📊 Features Available in Streamlit Version

✅ **Authentication System**
- Login with 3 demo credentials
- Role-based access control (Farmer, Staff, Admin)

✅ **Farmer Dashboard**
- Personal statistics (deliveries, milk supplied, earnings)
- Animal inventory
- Recent collections

✅ **Staff Dashboard**
- Collection center overview
- Daily statistics
- Collections at center

✅ **Admin Dashboard**
- System-wide metrics
- Quality distribution charts
- Center performance
- All collections data

✅ **Collections Page**
- Search & filtering
- Date range filtering
- Quality grade filtering
- Detailed collection records

✅ **Payments Page**
- Payment history
- Status tracking (Paid/Pending)
- Amount summaries

✅ **Quality Tests Page**
- Quality test records
- Fat, SNF, acidity measurements
- Quality grades

---

## 🎨 Customization

### Update Theme
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#10b981"  # Green for Gujarat theme
backgroundColor = "#ffffff"
```

### Add Features
Modify `streamlit_app.py`:
- Add new pages in navigation buttons
- Create new functions like `page_analytics()`
- Update mock data in MOCK_* dictionaries

---

## 🔧 Troubleshooting

### App Not Loading
```bash
# Clear cache
streamlit cache clear

# Check logs
streamlit run streamlit_app.py --logger.level=debug
```

### Memory Issues
Streamlit Cloud free tier: 1GB RAM
- Optimize data filtering
- Use lazy loading for large datasets
- Implement pagination

### Performance Tuning
```python
@st.cache_data
def load_data():
    return MOCK_COLLECTIONS  # Cache expensive operations

@st.cache_resource
def init_connection():
    return create_db_connection()
```

---

## 📈 Next Steps

1. **Backend Integration**: Connect to Flask/Django API instead of mock data
2. **Database**: Replace mock data with PostgreSQL/MySQL
3. **Real-time Updates**: Add WebSocket support for live notifications
4. **Analytics**: Add Plotly/Altair charts for advanced analytics
5. **Export**: Add PDF/Excel export functionality

---

## 📞 Support

For Streamlit documentation: https://docs.streamlit.io
For deployment help: https://docs.streamlit.io/knowledge-base/deploy

---

**Last Updated:** April 6, 2026
**Version:** 1.0
