# Milk Collection and Quality Tracking System - Gujarat

A comprehensive digital solution for managing milk collection, quality tracking, and farmer payments across multiple dairy collection centers in Gujarat villages.

## Overview

This system addresses the challenges faced by dairy cooperatives and farmers in Gujarat by digitizing the milk collection process, ensuring transparency, reducing errors, and enabling real-time tracking of milk quality and payments.

## Features

### Farmer Management
- Farmer registration and profile management
- Authentication and authorization
- Personal dashboard for viewing milk submissions and payments
- Digital records accessible anytime, anywhere

### Milk Collection
- Daily milk quantity recording
- Multiple collection center support
- Batch collection data entry
- Real-time collection tracking
- Collection history and analytics

### Quality Testing
- Milk quality test result recording
- Fat, SNF (Solids-Not-Fat), and conductivity tests
- Quality grading system (A, B, C grades)
- Test result history per farmer
- Quality trend analysis

### Payment Management
- Automated payment calculation based on quantity and quality
- Transparent payment structure
- Payment history and detailed reports
- Farmer notifications about payments
- Seasonal price adjustment support

### Reporting & Analytics
- Daily collection reports
- Quality analysis reports
- Payment summary reports
- Farmer-wise performance tracking
- Center-wise collection statistics
- Export reports to PDF/Excel

### Admin & Cooperative Management
- Cooperative staff account management
- Collection center management
- Data verification and correction
- Batch operations
- System configuration

## Tech Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: MongoDB
- **Authentication**: JWT tokens
- **API Documentation**: OpenAPI/Swagger
- **Testing**: pytest

### Frontend
- **Framework**: React 18+
- **UI Library**: Material-UI / Custom Gujarat-style components
- **State Management**: Context API / Redux
- **Styling**: CSS-in-JS / Tailwind CSS
- **Charts**: Chart.js / Recharts
- **Forms**: React Hook Form with validation

## Project Structure

```
milk-tracking-system/
├── backend/                    # Flask API backend
│   ├── app/
│   │   ├── models/            # Data models
│   │   ├── routes/            # API endpoints
│   │   ├── services/          # Business logic
│   │   ├── utils/             # Helper functions
│   │   └── __init__.py
│   ├── tests/                 # Unit tests
│   ├── config.py              # Configuration
│   ├── requirements.txt        # Python dependencies
│   └── run.py                 # Entry point
├── frontend/                   # React application
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── pages/             # Page components
│   │   ├── assets/            # Images, fonts
│   │   ├── styles/            # Global styles
│   │   ├── App.jsx            # Main app component
│   │   └── index.jsx          # React DOM render
│   ├── package.json           # Dependencies
│   └── vite.config.js         # Build config
├── docs/                       # Documentation
│   ├── PROBLEM_UNDERSTANDING.md
│   ├── SYSTEM_DESIGN.md
│   ├── API_DOCUMENTATION.md
│   ├── SETUP_GUIDE.md
│   ├── LIMITATIONS_FUTURE_SCOPE.md
│   └── architecture/           # Diagrams
└── README.md                   # This file
```

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- MongoDB 4.4+
- Git

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run on `http://localhost:5173`

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new farmer/staff
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/refresh` - Refresh token

### Farmers
- `GET /api/farmers` - List all farmers
- `GET /api/farmers/<id>` - Get farmer details
- `POST /api/farmers` - Create new farmer
- `PUT /api/farmers/<id>` - Update farmer
- `DELETE /api/farmers/<id>` - Delete farmer

### Milk Collection
- `GET /api/collections` - List collections
- `POST /api/collections` - Record milk collection
- `GET /api/collections/<id>` - Get collection details
- `PUT /api/collections/<id>` - Update collection
- `GET /api/collections/farmer/<farmer_id>` - Get farmer's collections

### Quality Tests
- `GET /api/quality-tests` - List all tests
- `POST /api/quality-tests` - Record quality test
- `GET /api/quality-tests/farmer/<farmer_id>` - Get farmer's test results
- `PUT /api/quality-tests/<id>` - Update test result

### Payments
- `GET /api/payments` - List payments
- `POST /api/payments/calculate` - Calculate farmer payment
- `GET /api/payments/farmer/<farmer_id>` - Get farmer's payment history
- `GET /api/payments/report` - Generate payment report

### Reports
- `GET /api/reports/daily-collection` - Daily collection report
- `GET /api/reports/quality-analysis` - Quality analysis report
- `GET /api/reports/payment-summary` - Payment summary report
- `GET /api/reports/farmer-performance` - Farmer performance report
- `GET /api/reports/export` - Export report (PDF/Excel)

### Collection Centers
- `GET /api/centers` - List all centers
- `POST /api/centers` - Create center
- `PUT /api/centers/<id>` - Update center
- `DELETE /api/centers/<id>` - Delete center

## Documentation

- **[Problem Understanding](docs/PROBLEM_UNDERSTANDING.md)** - Detailed problem analysis
- **[System Design](docs/SYSTEM_DESIGN.md)** - Architecture and design decisions
- **[API Documentation](docs/API_DOCUMENTATION.md)** - Complete API reference
- **[Setup Guide](docs/SETUP_GUIDE.md)** - Installation and configuration
- **[Limitations & Future Scope](docs/LIMITATIONS_FUTURE_SCOPE.md)** - Known issues and enhancements

## Key Design Decisions

1. **MongoDB for Data Storage**: Flexible schema for handling various data types and future extensions
2. **JWT Authentication**: Stateless, scalable authentication mechanism
3. **Microservices-ready Architecture**: Services layer separates business logic from routes
4. **RESTful API Design**: Standard HTTP methods for easy integration
5. **React Frontend**: Single-page application for responsive user experience
6. **Gujarat-inspired UI**: Local language support and culturally relevant design

## Database Schema

### Collections
- **farmers**: Farmer registration and profile data
- **milk_collections**: Daily milk collection records
- **quality_tests**: Milk quality test results
- **payments**: Payment records and calculations
- **centers**: Milk collection center information
- **prices**: Daily/seasonal price information
- **users**: System users (staff, admins)

## Security Features

- JWT-based authentication
- Role-based access control (RBAC)
- Input validation and sanitization
- Password hashing with bcrypt
- CORS protection
- Rate limiting on API endpoints
- Audit logging for critical operations

## Testing

Run tests with:

```bash
cd backend
pytest
```

## Deployment

### Docker Support
```bash
docker-compose up -d
```

### Cloud Deployment
- Backend: AWS Lambda, Heroku, or Railway
- Frontend: Vercel, Netlify, or AWS S3 + CloudFront
- Database: MongoDB Atlas

## Performance Considerations

- Indexed MongoDB queries for fast lookups
- Pagination for large datasets
- Caching strategies for frequently accessed data
- Database connection pooling
- Optimized React component rendering

## Limitations

- Single-language support (Gujarati UI planned)
- Batch processing for reports may have latency
- Mobile app not yet developed
- Advanced analytics features limited
- Offline functionality not implemented

## Future Enhancements

- Mobile app (React Native/Flutter)
- Gujarati language support
- SMS/WhatsApp notifications
- Advanced analytics and ML predictions
- Blockchain integration for transparency
- IoT sensor integration for automated quality testing
- Voice-based data entry for farmers
- Integration with cooperative network
- Payment gateway integration
- Weather impact analysis on milk quality

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit pull request

## License

This project is open-source and available under the MIT License.

## Contact

For questions, issues, or contributions, please open an issue in the GitHub repository.

## Team Members

- Problem Understanding & Analysis: [Your Name]
- Backend Development: [Your Name]
- Frontend Development: [Your Name]
- Documentation: [Your Name]
- Architecture Design: [Your Name]

---

**Last Updated**: April 2026
**Status**: Development
**Version**: 1.0.0-beta
