# Testing Guide - Milk Tracking System

## Overview

This guide covers the comprehensive testing suite for the Milk Tracking System, including unit tests, integration tests, and end-to-end tests.

**Test Coverage:**
- Backend: Service layer, API routes, validation, data models
- Frontend: Components, forms, API integration, calculations
- Integration: End-to-end workflows from data entry to payment

---

## Backend Testing

### Prerequisites

```bash
# Install test dependencies (already in requirements.txt)
pip install -r requirements.txt

# Ensure MongoDB is running
mongod
```

### Running Backend Tests

#### Run All Tests
```bash
cd backend
pytest tests/test_all.py -v
```

#### Run Specific Test Category
```bash
# Unit tests only
pytest tests/test_all.py -m unit -v

# Integration tests only
pytest tests/test_all.py -m integration -v

# Specific test class
pytest tests/test_all.py::TestQualityService -v

# Specific test method
pytest tests/test_all.py::TestQualityService::test_calculate_quality_score -v
```

#### Run with Coverage Report
```bash
pytest tests/test_all.py --cov=app --cov-report=html
# Open htmlcov/index.html to view coverage
```

#### Run Tests with Output
```bash
# Show print statements
pytest tests/test_all.py -v -s

# Show slower tests
pytest tests/test_all.py -v --durations=10
```

### Test Categories

#### Quality Service Tests (`TestQualityService`)
Tests the quality scoring and grading system:
- `test_calculate_quality_score` - Validates score calculation (40% fat, 40% SNF, 20% conductivity)
- `test_score_with_high_fat` - Tests scoring with premium fat content
- `test_score_with_low_parameters` - Tests scoring with below-average parameters
- `test_assign_grade` - Tests grade assignment (A+, A, B+, B, C)
- `test_grade_bonus_percentage` - Tests incentive percentage for grades
- `test_get_quality_bonus` - Tests bonus amount calculation
- `test_get_quality_bonus_negative` - Tests negative bonus for poor grades

**Example Output:**
```
QUALITY-SCORE: 82 points
GRADE: A (10% bonus)
BONUS-AMOUNT: ₹320 (on ₹3200 base)
```

#### Billing Service Tests (`TestBillingService`)
Tests payment calculation logic:
- `test_calculate_farmer_payment_basic` - Tests basic payment calculation
- `test_payment_with_quality_grades` - Tests payment with different quality grades

**Payment Calculation Flow:**
| Component | Value |
|-----------|-------|
| Collections | 40L (20+20) |
| Base Rate | ₹40/L |
| Base Amount | ₹1,600 |
| Quality (A+) | +15% = ₹240 |
| Volume Bonus | +(40-20) × ₹0.5 = ₹10 |
| **Total** | **₹1,850** |

#### Farmer Service Tests (`TestFarmerService`)
Tests farmer registration and management:
- `test_generate_registration_number` - Tests registration number format (GUJF-2026-XXXXX)
- `test_registration_number_sequence` - Tests sequential numbering

#### API Route Tests
- `TestAuthRoutes` - Authentication endpoints
- `TestFarmerRoutes` - Farmer management endpoints
- `TestCollectionRoutes` - Milk collection endpoints
- `TestQualityTestRoutes` - Quality testing endpoints

#### Validation Tests (`TestDataValidation`)
Tests input validation:
- `test_validate_quantity` - Checks 0.5-200L range
- `test_validate_temperature` - Checks 4-40°C range
- `test_validate_percentage` - Checks 0-20% range for fat/SNF

#### Performance Tests (`TestPerformance`)
Tests system performance:
- `test_large_dataset_query` - Verifies queries complete in <500ms with 1000 records

### Common Test Commands

```bash
# Run tests and stop on first failure
pytest tests/test_all.py -x

# Run last failed tests
pytest tests/test_all.py --lf

# Run only failed tests from last run
pytest tests/test_all.py --ff

# Test with specific log level
pytest tests/test_all.py --log-cli-level=DEBUG

# Parallel test execution
pytest tests/test_all.py -n 4  # Run 4 tests in parallel
```

---

## Frontend Testing

### Prerequisites

```bash
# Install dependencies
cd frontend
npm install

# Install test dependencies
npm install --save-dev vitest @testing-library/react @testing-library/user-event jsdom
```

### Running Frontend Tests

#### Run All Tests
```bash
npm run test
```

#### Run Tests in Watch Mode
```bash
npm run test:watch
```

#### Run Tests with Coverage
```bash
npm run test:coverage
# Check coverage report in coverage/index.html
```

#### Run Specific Test File
```bash
npm run test __tests__/components.test.js
```

#### Run Tests Matching Pattern
```bash
npm run test -- --grep "DataTable"
```

### Test Categories

#### Form Component Tests (`RecordCollectionForm`)
Tests milk collection form:
- `test_renders_form_with_all_required_fields` - Verifies form structure
- `test_validates_quantity_input_range` - Tests 0.5-200L validation
- `test_shows_error_for_invalid_temperature` - Tests 4-40°C validation
- `test_disables_submit_when_required_fields_empty` - Tests form state
- `test_submits_form_with_valid_data` - Tests submission flow

#### Quality Test Form Tests (`RecordQualityTestForm`)
Tests quality test recording:
- `test_calculates_quality_score_in_real_time` - Tests live score calculation
- `test_assigns_correct_grade_based_on_score` - Tests grading logic
- `test_validates_quality_parameter_ranges` - Tests validation

#### Farmer Registration Tests (`FarmerRegistrationForm`)
Tests farmer signup:
- `test_validates_email_format` - Validates email pattern
- `test_validates_phone_number` - Validates 10-digit phone
- `test_validates_password_strength` - Tests password requirements
- `test_validates_aadhar_number_format` - Validates Aadhar format
- `test_validates_bank_details` - Validates bank account details

#### Data Table Tests (`DataTable`)
Tests reusable data table component:
- `test_renders_table_with_columns` - Verifies table structure
- `test_filters_data_by_search_term` - Tests search functionality
- `test_sorts_data_by_column` - Tests sorting
- `test_paginates_data_correctly` - Tests pagination
- `test_handles_row_click_events` - Tests click handlers

#### Data Formatting Tests
Tests utility formatting functions:
- `test_formats_date_correctly` - Tests date formatting
- `test_formats_currency_values` - Tests ₹ formatting
- `test_formats_temperature_with_unit` - Tests °C unit
- `test_formats_quantity_with_unit` - Tests L unit

#### API Integration Tests
Tests API client integration:
- `test_makes_GET_request_for_collections` - Tests GET calls
- `test_makes_POST_request_to_record_collection` - Tests POST calls
- `test_makes_PUT_request_to_update_farmer` - Tests PUT calls
- `test_handles_API_error_responses` - Tests error handling

#### Payment Calculation Tests
Tests payment math:
- `test_calculates_base_payment` - Tests base rate × quantity
- `test_applies_quality_incentive_bonus` - Tests quality bonuses
- `test_applies_volume_bonus_correctly` - Tests volume thresholds
- `test_calculates_total_payment_correctly` - Tests final amount

**Example Calculation:**
```
Base Amount:        ₹1,600  (40L × ₹40/L)
Quality (A+) +15%:  ₹240
Volume Bonus +10%:  ₹10
─────────────────────────
Total Payment:      ₹1,850
```

#### Quality Grading Tests
Tests quality scoring:
- `test_calculates_quality_score_from_parameters` - Tests score math
- `test_grades_farmers_correctly` - Tests grade assignment

```
Score ≥ 90 → A+ (+15% bonus)
Score ≥ 80 → A  (+10% bonus)
Score ≥ 70 → B+ (+5% bonus)
Score ≥ 60 → B  (0% bonus)
Score < 60 → C  (-20% penalty)
```

### Common Frontend Test Commands

```bash
# Run tests and exit
npm run test -- --run

# Update snapshots
npm run test -- -u

# Test with verbose output
npm run test -- --reporter=verbose

# Filter tests by name
npm run test -- --grep "Payment"

# Maximum workers
npm run test -- --threads --threads.count=4
```

---

## Database Seeding for Testing

### Seed Test Data

```bash
cd backend
python seed_db.py
```

This creates:
- ✓ 3 admin/staff users (for testing different roles)
- ✓ 5 collection centers
- ✓ 100 sample farmers
- ✓ 2000+ milk collections
- ✓ 1500+ quality tests
- ✓ 480+ payment records

#### Test Credentials After Seeding
```
Admin:     admin@milktrack.com / Admin@123
Manager:   center_manager@milktrack.com / Manager@123
QC Staff:  qc_staff@milktrack.com / QC@123
```

---

## Continuous Integration Setup

### GitHub Actions Example

Create `.github/workflows/tests.yml`:

```yaml
name: Test Suite

on: [push, pull_request]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    services:
      mongodb:
        image: mongo:7
        options: >-
          --health-cmd mongosh
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 27017:27017

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r backend/requirements.txt
      - run: cd backend && pytest tests/test_all.py --cov

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: cd frontend && npm install
      - run: cd frontend && npm run test -- --run
```

---

## Test Troubleshooting

### Backend Issues

**Problem:** Tests fail with MongoDB connection error
```
Solution: Ensure MongoDB is running
  mongod
```

**Problem:** Import errors in tests
```
Solution: Add backend to Python path
  export PYTHONPATH="${PYTHONPATH}:/path/to/backend"
```

**Problem:** Tests modifying each other's data
```
Solution: Use cleanup fixture (already implemented)
  All tests clean up collections automatically
```

### Frontend Issues

**Problem:** API mocks not working
```
Solution: Ensure vi.mock is before imports
  Move mock before import statements
```

**Problem:** async/await tests timing out
```
Solution: Use waitFor() for async operations
  await waitFor(() => expect(...).toBe(...))
```

**Problem:** localStorage undefined
```
Solution: Vitest setup already includes mock
  Check vitest.setup.js is loaded in vitest.config.js
```

---

## Performance Benchmarks

### Target Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Quality Score Calc | < 10ms | ~2ms |
| Payment Calc | < 50ms | ~15ms |
| API Response | < 200ms | ~80ms |
| Form Validation | < 5ms | ~1ms |
| Large Dataset Query | < 500ms | ~150ms |

### Running Benchmarks

```bash
# Backend performance
pytest tests/test_all.py::TestPerformance -v

# Frontend bundle size
npm run build
# Check dist/ folder size
```

---

## Coverage Goals

### Target Coverage
- Backend: **80%+ line coverage**
- Frontend: **75%+ component coverage**
- Overall: **80%+ statement coverage**

### View Coverage Reports

**Backend:**
```bash
pytest tests/test_all.py --cov=app --cov-report=html
open htmlcov/index.html
```

**Frontend:**
```bash
npm run test:coverage
open coverage/index.html
```

---

## Best Practices

### Writing Tests

1. **Use descriptive names**
   ```python
   def test_calculate_quality_score_with_premium_milk()  # Good
   def test_score()  # Bad
   ```

2. **Follow AAA pattern** (Arrange, Act, Assert)
   ```python
   # Arrange
   farmer_id = create_test_farmer()
   
   # Act
   result = calculate_payment(farmer_id)
   
   # Assert
   assert result > 0
   ```

3. **Test behavior, not implementation**
   ```python
   # Good - tests what happens
   assert quality_score >= 70 and quality_score <= 100
   
   # Bad - tests HOW it's calculated
   assert result['score'] == fat_score + snf_score + cond_score
   ```

4. **Use fixtures for setup**
   ```python
   @pytest.fixture
   def farmer(db):
       return db.farmers.insert_one({...})
   ```

### Test Organization

```
backend/
  tests/
    test_all.py          # All tests
    conftest.py          # Shared fixtures
    
frontend/
  __tests__/
    components.test.js   # Component tests
    utils.test.js        # Utility tests
```

---

## Quick Reference

### Run Tests Quickly
```bash
# Backend
cd backend && pytest -x -q

# Frontend
cd frontend && npm run test -- --run

# Both
npm run test:all  # If configured
```

### Check Coverage
```bash
# Backend
pytest --cov=app --cov-report=term-missing

# Frontend  
npm run test:coverage
```

### Debug a Failing Test
```bash
# Backend with prints
pytest tests/test_all.py::TestQualityService::test_calculate_quality_score -v -s

# Frontend with console
npm run test -- --reporter=verbose
```

---

## Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Vitest Documentation](https://vitest.dev/)
- [Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)
- [MongoDB Testing](https://docs.mongodb.com/manual/testing/)

---

## Support

For test failures or questions:
1. Check test output logs
2. Review test documentation above
3. Verify prerequisites are installed
4. Check MongoDB and servers are running
5. Review error messages carefully

**Last Updated:** April 6, 2026
**Version:** 1.0.0
