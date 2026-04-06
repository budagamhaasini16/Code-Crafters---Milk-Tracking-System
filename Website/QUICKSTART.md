# Quick Start Guide

## 5-Minute Setup

### Step 1: Prerequisites
- Python 3.9+
- Node.js 16+
- MongoDB (local or MongoDB Atlas)
- Git

### Step 2: Run Setup Script

**Windows:**
```bash
setup.bat
```

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Step 3: Start Services

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python run.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Terminal 3 - MongoDB (if not running):**
```bash
mongod
```

### Step 4: Access Application
Open: http://localhost:5173

### Step 5: Test Login
- Email: any email
- Password: Any strong password (uppercase, lowercase, numbers, special chars)
- Click Register first, then Login

---

## Project Structure at a Glance

```
🎯 Milk Tracking System
├── 📂 backend/          ← Flask REST API
├── 📂 frontend/         ← React Web App
├── 📂 docs/             ← Documentation
├── docker-compose.yml   ← Docker setup (optional)
└── README.md           ← Full documentation
```

---

## Key Features

### Farmer Portal
- ✅ Register and manage profile
- ✅ View milk collection history
- ✅ Check quality test results
- ✅ Track payment history
- ✅ Real-time notifications

### Staff Dashboard
- ✅ Record milk collections
- ✅ Perform quality tests
- ✅ Generate daily reports
- ✅ Manage farmer information
- ✅ Print payment slips

### Admin Panel
- ✅ Collection center management
- ✅ User account management
- ✅ Price rate configuration
- ✅ System-wide reports
- ✅ Data management

---

## API Base URL
```
http://localhost:5000/api/v1
```

---

## Database Seeding (For Demo/Testing)

### Populate with Sample Data
```bash
cd backend
python seed_db.py
```

This creates:
- 3 test staff users with different roles
- 5 collection centers
- 100+ sample farmers
- 2000+ milk collection records
- 1500+ quality test results
- 480+ payment records

**Test Credentials:**
- Admin: `admin@milktrack.com` / `Admin@123`
- Manager: `center_manager@milktrack.com` / `Manager@123`
- QC Staff: `qc_staff@milktrack.com` / `QC@123`

---

## Testing

### Run Backend Tests
```bash
cd backend
pytest tests/test_all.py -v          # Run all tests
pytest tests/test_all.py -m unit     # Unit tests only
pytest tests/test_all.py --cov       # With coverage report
```

### Run Frontend Tests
```bash
cd frontend
npm run test                          # Run all tests
npm run test:watch                    # Watch mode
npm run test:coverage                 # Coverage report
```

**For detailed testing information, see [TESTING_GUIDE.md](TESTING_GUIDE.md)**

---

## Useful Links

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Full project overview |
| [SETUP_GUIDE.md](docs/SETUP_GUIDE.md) | Detailed installation |
| [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) | API reference |
| [SYSTEM_DESIGN.md](docs/SYSTEM_DESIGN.md) | Technical architecture |
| [PROBLEM_UNDERSTANDING.md](docs/PROBLEM_UNDERSTANDING.md) | Problem analysis |
| [TESTING_GUIDE.md](TESTING_GUIDE.md) | Testing documentation |
| [LIMITATIONS & FUTURE](docs/LIMITATIONS_FUTURE_SCOPE.md) | Known issues & enhancements |

---

## Common Issues & Solutions

### "MongoDB connection refused"
```bash
# Start MongoDB
# Windows: mongod.exe
# macOS: brew services start mongodb-community
# Linux: sudo systemctl start mongod
```

### "Port 5000/5173 already in use"
```bash
# Kill process on port
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :5000
kill -9 <PID>
```

### "npm install fails"
```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

---

## Development Commands

### Backend
```bash
cd backend
source venv/bin/activate      # Activate virtual environment
python run.py                 # Start development server
pytest                        # Run tests
python -c "from app import init_app; app = init_app()"  # Verify setup
```

### Frontend
```bash
cd frontend
npm run dev                   # Start development server
npm run build                 # Build for production
npm run lint                  # Check code style
npm run test                  # Run tests
npm run preview              # Preview production build
```

---

## Database

### MongoDB Local
```bash
# Start
mongod

# Connect
mongosh

# Check database
use milk_tracking_system
db.users.find()
```

### MongoDB Atlas (Cloud)
1. Create account: https://www.mongodb.com/cloud/atlas
2. Create a cluster
3. Get connection string
4. Update `MONGODB_URI` in `.env`

---

## Docker Setup (Alternative)

```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Services will be available at:
- Frontend: http://localhost:5173
- Backend: http://localhost:5000
- MongoDB: localhost:27017

---

## Configuration Files

### Backend (.env)
```ini
FLASK_ENV=development
MONGODB_URI=mongodb://localhost:27017/milk_tracking_system
JWT_SECRET_KEY=your-secret-key
CORS_ORIGINS=http://localhost:5173
```

### Frontend (.env)
```ini
VITE_API_URL=http://localhost:5000/api/v1
```

---

## File Key Files

| File | Purpose |
|------|---------|
| `backend/run.py` | Entry point for API server |
| `backend/config.py` | Configuration management |
| `backend/app/__init__.py` | Flask app initialization |
| `backend/app/models/__init__.py` | Data models |
| `backend/app/routes/auth.py` | Authentication endpoints |
| `frontend/src/App.jsx` | Main React component |
| `frontend/src/pages/` | Page components |
| `frontend/src/utils/api.js` | API client |
| `frontend/tailwind.config.js` | Tailwind CSS config |

---

## Next Steps

1. **Review Documentation**
   - Read [PROBLEM_UNDERSTANDING.md](docs/PROBLEM_UNDERSTANDING.md)
   - Review [SYSTEM_DESIGN.md](docs/SYSTEM_DESIGN.md)

2. **Test API Endpoints**
   - Use Postman or curl
   - Check [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)

3. **Explore Code**
   - Check backend routes in `backend/app/routes/`
   - Review frontend components in `frontend/src/`

4. **Start Development**
   - Create feature branches: `git checkout -b feature/your-feature`
   - Follow the code structure
   - Write tests for new features

---

## Contact & Support

- 📚 Full documentation in `/docs` folder
- 💬 Check code comments
- 🐛 Debug using browser DevTools and Flask debug mode
- 📖 Review examples in documentation

---

## Performance Tips

### Frontend
- Use React DevTools extension
- Check Network tab for API calls
- Use Lighthouse for performance audit

### Backend
- Enable debug logging: `FLASK_DEBUG=1`
- Monitor API response times
- Check MongoDB query performance

---

## Deployment

### Quick Deploy (Docker)
```bash
docker-compose -f docker-compose.yml up -d
```

### Manual Deploy
- Backend: Use Gunicorn
- Frontend: Build and deploy to CDN
- Database: Use MongoDB Atlas

See [SETUP_GUIDE.md](docs/SETUP_GUIDE.md) for detailed deployment instructions.

---

**Happy Coding! 🚀**

**Last Updated**: April 2026  
**Version**: 1.0.0-beta
