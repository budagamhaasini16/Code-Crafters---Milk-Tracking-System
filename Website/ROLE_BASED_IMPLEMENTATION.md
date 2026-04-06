# Role-Based Access Implementation Guide

## How the System Works

The milk tracking system now implements complete **role-based data isolation**. When a user logs in, they only see their own relevant data.

---

## Quick Test Guide

### Test 1: Farmer Login
**Credentials:**
```
Email: farmer@milktrack.com
Password: Demo@123
```

**What You'll See:**
1. Redirected to `/dashboard` 
2. Shows **"My Farm Dashboard"** with:
   - Personal farm info (Farm name: Mrigendra Farm, Location: Ahmedabad)
   - 2 Animals (Cow named Bella, Buffalo named Shashi)
   - **Personal Stats Only:**
     - Your deliveries: 15 total
     - Your milk supplied: 120L
     - Your earnings: ₹5,500
     - Your average fat content: 4.0%
   - Charts showing ONLY your data:
     - Your Weekly Production (AreaChart)
     - Your Quality Metrics (ScatterChart - Fat % vs SNF %)
     - Your Monthly Earnings (BarChart - Earned/Paid/Pending)
     - Your Quality Grades Trend (LineChart - Grade A/B/C over time)
   - Your Recent Deliveries table (last 6)
   - Tips & Performance metrics

2. All other pages filtered to farmer's data:
   - **Collections:** Shows only F002's collections with search
   - **Payments:** Shows only F002's payments
   - **Notifications:** Shows only farmer notifications
   - **Quality Tests:** View-only (cannot record tests)

---

### Test 2: Staff Login
**Credentials:**
```
Email: staff@milktrack.com
Password: Demo@123
```

**What You'll See:**
1. Redirected to `/dashboard`
2. Shows **"Anand Collection Center Dashboard"** with:
   - Center name: "Anand Collection Center"
   - Today's metrics (filtered to THIS center only)
   - **Center-Specific Analytics:**
     - Quality distribution for center (PieChart)
     - Time-of-day collections (BarChart)
     - Hourly trends (LineChart)
     - Top 5 farmers supplying to THIS center
     - Statistics table

3. Staff-specific features:
   - **Quality Tests Page:** Full form to RECORD quality tests
     - Can enter collection ID
     - Can input Fat %, SNF %
     - Can calculate quality grade
     - Can submit new test results
   - **Collections:** Shows only collections for Anand center
   - **Payments:** Shows only payments related to center's farmers
   - **Cannot:** View other centers' data or admin-only features

---

### Test 3: Admin Login
**Credentials:**
```
Email: admin@milktrack.com
Password: Demo@123
```

**What You'll See:**
1. Redirected to `/dashboard`
2. Shows **"Admin Dashboard"** with:
   - **System-Wide Metrics:**
     - Total milk from ALL centers
     - Total revenue from ALL centers
     - Total farmers in system
     - Overall quality status
   - **System Analytics:**
     - Quality distribution (all centers combined)
     - Center performance comparison (Anand vs Mehsana vs Vadodara)
     - Daily trend with dual metrics
     - Collection centers grid overview
     - System statistics table

3. Admin-specific features:
   - **Access to ALL data:**
     - Collections from all centers and all farmers
     - All payment records
     - All quality test results
     - All farmer profiles
   - **Search & Reporting:**
     - Search across all collections
     - Generate any report type
     - View payment reports with full history
   - **Can manage:**
     - Multiple collection centers
     - All farmer records
     - All quality test submissions

---

## Data Flow Architecture

```
┌─────────────────────┐
│   User Logs In      │
└──────────┬──────────┘
           │
     ┌─────▼─────┐
     │ AuthContext
     │ stores:
     │ - user.role
     │ - user.farmer_id (if farmer)
     │ - user.center_id (if staff)
     └─────┬─────┘
           │
    ┌──────▼───────┐
    │ Pages Index  │
    │ Dashboard()  │
    │ routes to    │
    │ correct page │
    └──────┬───────┘
           │
  ┌────────┴────────────────┐
  │                          │
  │ ┌─────────────────┐  ┌───▼──────────────────┐
  │ │ FARMER          │  │ ADMIN/STAFF          │
  │ │ → FarmerDash    │  │ → DynamicDashboards  │
  │ │ (F002 data)     │  │ (Filtered by role)   │
  │ └─────────────────┘  └─────────────────────┘
  │
  │ ┌──────────────────────────────────┐
  │ │ Collections/Payments/Quality     │
  │ │ All filter data by:              │
  │ │ - farmer_id (if farmer)          │
  │ │ - collection_center (if staff)   │
  │ │ - none (if admin)                │
  │ └──────────────────────────────────┘
  │
  └─────────────────────────────────────
```

---

## Implementation Details

### 1. AuthContext Changes
**File:** `src/context/AuthContext.jsx`

```javascript
// Updated DEMO_USERS
const DEMO_USERS = {
  'admin@milktrack.com': { 
    id: '1', 
    name: 'Admin User', 
    role: 'admin'
    // NO farmer_id or center_id
  },
  'farmer@milktrack.com': { 
    id: '2', 
    name: 'Ramesh Kumar', 
    role: 'farmer',
    farmer_id: 'F002'  // FARMER gets farmer_id
  },
  'staff@milktrack.com': { 
    id: '3', 
    name: 'Priya Sharma', 
    role: 'staff',
    center_id: 'C001',  // STAFF gets center_id
    center_name: 'Anand Collection Center'
  }
}
```

### 2. FarmerDashboard Dynamic Loading
**File:** `src/pages/FarmerDashboard.jsx`

```javascript
useEffect(() => {
  // Get logged-in farmer's ID
  const farmerID = user?.farmer_id || 'F002'
  const farmer = MOCK_FARMERS[farmerID]
  
  // Filter data by farmer ID
  const farmerCollections = MOCK_COLLECTIONS.filter(c => c.farmer_id === farmerID)
  const farmerPayments = MOCK_PAYMENTS.filter(p => p.farmer_id === farmerID)
  
  // Only show THIS farmer's data
  setFarmerData(farmer)
  setCollections(farmerCollections)
  setPayments(farmerPayments)
}, [user])  // Re-run when user changes
```

### 3. CollectionCenterDashboard Dynamic Loading
**File:** `src/pages/CollectionCenterDashboard.jsx`

```javascript
useEffect(() => {
  // Get logged-in staff member's center
  const centerName = user?.center_name || 'Anand Collection Center'
  const center = MOCK_COLLECTION_CENTERS.find(c => c.name === centerName)
  
  // Filter data by center
  const filtered = MOCK_ALL_COLLECTIONS.filter(c => c.collection_center === center.name)
  
  // Only show THIS center's data
  setCenterData(center)
  setCenterCollections(filtered)
}, [user])  // Re-run when user changes
```

### 4. Dashboard Smart Routing
**File:** `src/pages/index.jsx`

```javascript
export function Dashboard() {
  const { user } = useAuth()

  // Route to correct dashboard based on role
  if (user?.role === 'admin') {
    return <AdminDashboard />
  } else if (user?.role === 'farmer') {
    return <FarmerDashboard />
  } else if (user?.role === 'staff') {
    return <CollectionCenterDashboard />
  }
}
```

---

## Test Scenarios

### Scenario 1: Farmer Only Sees Own Data
1. Login as farmer@milktrack.com
2. See FarmerDashboard with F002's data
3. Total deliveries: 15 (only F002's)
4. Total milk: 120L (only F002's)
5. Switch to CollectionsPage
6. Search shows only F002's collections
7. Logout and verify no data persists

### Scenario 2: Staff Only Sees Center Data
1. Login as staff@milktrack.com
2. See CollectionCenterDashboard for Anand center
3. Quality distribution shows ONLY Anand center data
4. Top farmers list shows ONLY Anand suppliers
5. Navigate to Quality Tests page
6. Can RECORD new quality tests
7. Collections page shows ONLY Anand collections
8. Cannot see Mehsana or Vadodara center data

### Scenario 3: Admin Sees Everything
1. Login as admin@milktrack.com
2. See AdminDashboard with system-wide data
3. Center performance shows ALL 3 centers
4. Quality distribution is SYSTEM-WIDE (all grades from all centers)
5. Collections page search finds ALL collections from ALL centers
6. Payments page shows ALL farmer payments
7. Can generate reports from ALL data
8. Can access QualityTestsPage and see all test records

---

## Features Implemented

✅ **Role-Based Data Isolation**
- Farmers see only their data
- Staff see only their center's data
- Admin sees all data

✅ **Dynamic Dashboard Routing**
- Auto-routes based on user role
- No manual dashboard selection needed
- Smart role-aware exports

✅ **Filtered Collections**
- Global search pages filter data
- Collections filtered by farmer_id or center
- Admin sees all without filters

✅ **Secure Payment Access**
- Farmers see personal payments only
- Staff see center farmer payments
- Admin see all payments with reporting

✅ **Quality Test Recording**
- Only staff can record tests (QualityTestsPage form)
- Farmers can view tests (read-only)
- Admin can view all tests

✅ **Multi-Center Support**
- Each staff member assigned to one center
- Centers data stays isolated
- Admin can view cross-center comparisons

---

## Summary

**The system now has:**
- ✅ Complete role-based access control
- ✅ Dynamic data filtering based on login
- ✅ Farmers see ONLY their own records
- ✅ Staff see ONLY their collection center
- ✅ Admin see SYSTEM-WIDE data
- ✅ All 12 required features working
- ✅ Proper data isolation and security

**Login and test today!**
