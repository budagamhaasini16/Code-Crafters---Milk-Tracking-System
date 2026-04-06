# Comprehensive Testing Guide - Milk Tracking System

## Current System Status
- **Frontend:** Running on http://localhost:5175
- **Backend:** Running on http://localhost:5000 (ensure running)
- **MultiLanguage:** Gujarati, Hindi, Telugu, English fully supported
- **Role-Based Access:** ✅ Implemented and tested
- **Notifications:** ✅ Enhanced with 11 demo notifications
- **Notification Badge:** ✅ Added to header with unread count

---

## Demo User Accounts

### 1. Farmer Account
```
Email: farmer@milktrack.com
Password: Demo@123
Role: farmer
Farmer ID: F002
Expected Unread Notifications: 3 (NOTIF001, NOTIF002, NOTIF008)
```

### 2. Staff Account
```
Email: staff@milktrack.com
Password: Demo@123
Role: staff
Center ID: C001
Center Name: Anand Collection Center
Expected Unread Notifications: 2 (NOTIF003, NOTIF005)
```

### 3. Admin Account
```
Email: admin@milktrack.com
Password: Demo@123
Role: admin
Expected Unread Notifications: 1 (NOTIF011)
```

---

## Test Case 1: Farmer Login & Notifications

### Steps:
1. Navigate to http://localhost:5175
2. Login with farmer@milktrack.com / Demo@123
3. **Check Header:**
   - ✅ Should see notification bell 🔔
   - ✅ Badge should show "3" (unread notifications)
   - ✅ Bell should be clickable

### Expected Notifications for Farmer (6 total, 3 unread):
| ID | Type | Title | Status | Priority |
|----|------|-------|--------|----------|
| NOTIF001 | Payment | Payment Processed Successfully | ❌ Unread | High |
| NOTIF002 | Quality | Quality Alert - Low Fat Content | ❌ Unread | High |
| NOTIF004 | Announcement | New Quality Standards | ✅ Read | Medium |
| NOTIF006 | Collection | Collection Received - Confirmed | ✅ Read | Normal |
| NOTIF007 | Payment | Payment Pending Review | ✅ Read | Medium |
| NOTIF008 | Collection | Collection Received - Evening | ❌ Unread | Normal |

### Verification Points:
- [ ] Header shows correct unread count (3)
- [ ] All 6 notifications appear in NotificationsPage
- [ ] Unread notifications highlighted
- [ ] Only farmer's notifications shown (no staff/admin notifs)

---

## Test Case 2: Staff Login & Notifications

### Steps:
1. Logout from farmer account (click profile → Logout)
2. Login with staff@milktrack.com / Demo@123
3. **Check Header:**
   - ✅ Should see notification bell 🔔
   - ✅ Badge should show "2" (unread notifications)

### Expected Notifications for Staff (4 total, 2 unread):
| ID | Type | Title | Status | Priority |
|----|------|-------|--------|----------|
| NOTIF003 | Collection | Daily Collection Target Update | ❌ Unread | Medium |
| NOTIF005 | Payment | Batch Payment Approved | ❌ Unread | High |
| NOTIF009 | Quality | Quality Standards Update | ✅ Read | High |
| NOTIF010 | Collection | Weekly Report Due | ✅ Read | Medium |

### Verification Points:
- [ ] Header shows correct unread count (2)
- [ ] All 4 notifications appear in NotificationsPage
- [ ] Only staff's notifications shown
- [ ] No farmer/farmer-only notifications shown

---

## Test Case 3: Admin Login & Notifications

### Steps:
1. Logout from staff account
2. Login with admin@milktrack.com / Demo@123
3. **Check Header:**
   - ✅ Should see notification bell 🔔
   - ✅ Badge should show "1" (unread notifications)

### Expected Notifications for Admin (1 total, 1 unread):
| ID | Type | Title | Status | Priority |
|----|------|-------|--------|----------|
| NOTIF011 | Announcement | System Performance Report | ❌ Unread | Normal |

### Verification Points:
- [ ] Header shows correct unread count (1)
- [ ] Notification appears in NotificationsPage
- [ ] Can mark as read/unread
- [ ] Can delete notification

---

## Test Case 4: Notification Interactions

### Sub-Test 4A: Mark All as Read
1. Login as Farmer
2. Go to /notifications
3. Click "Mark All as Read"
4. **Verify:**
   - [ ] All notifications marked as read
   - [ ] Badge disappears from header
   - [ ] All notifications lose "Unread" styling

### Sub-Test 4B: Mark Individual as Unread
1. Click unread button on NOTIF004 (read notification)
2. **Verify:**
   - [ ] Notification shows "Unread" styling
   - [ ] Header badge updates to show new count
   - [ ] Notification moves to top

### Sub-Test 4C: Delete Notification
1. Click delete button on a notification
2. **Verify:**
   - [ ] Notification disappears from list
   - [ ] Unread count updates if it was unread

### Sub-Test 4D: Filters
Switch between filter tabs:
1. "All" - shows all notifications
2. "Unread" - shows only unread
3. "Payment" - shows only payment type
4. "Quality" - shows only quality type
5. "Collection" - shows only collection type
6. **Verify:** Each filter works correctly

---

## Test Case 5: Dashboard Differentiation

### Farmer Dashboard (Role: farmer)
**Expected:**
- [ ] Welcome message for farmer
- [ ] 4 metric cards (collections, payments, etc.)
- [ ] Animal section with farmer's animals
- [ ] Performance charts specific to farmer
- [ ] Only F002 farmer data shown

### Staff Dashboard (Role: staff)
**Expected:**
- [ ] Page redirects to CollectionCenterDashboard
- [ ] Center-specific data for Anand center
- [ ] Center metrics and visualizations
- [ ] Only C001 center data shown

### Admin Dashboard (Role: admin)
**Expected:**
- [ ] System-wide analytics
- [ ] All centers data visible
- [ ] System performance metrics
- [ ] All farmers/collections visible

---

## Test Case 6: Demo Data Across All Pages

### Collections Page
1. **As Farmer:** Should see only F002's collections
2. **As Staff:** Should see Anand center collections only
3. **As Admin:** Should see all collections

### Payments Page
1. **As Farmer:** Should see only F002's payments
2. **As Staff:** Should see Anand center's payments
3. **As Admin:** Should see all payments

### Quality Tests Page
1. **As Farmer:** Should see only F002's tests
2. **As Staff:** Should see Anand center's tests
3. **As Admin:** Should see all tests

### Reports Page
1. **As Farmer:** Should generate farmer-specific reports
2. **As Staff:** Should generate center-specific reports
3. **As Admin:** Should generate system-wide reports

---

## Test Case 7: Multi-Language Support

1. Use Language Switcher in header
2. **Test These Languages:**
   - [ ] English (EN)
   - [ ] Gujarati (GU)
   - [ ] Hindi (HI)
   - [ ] Telugu (TE)

3. **Verify:**
   - [ ] All page titles translated
   - [ ] All navigation labels translated
   - [ ] All button labels translated
   - [ ] Language persists on page refresh

---

## Test Case 8: Login Page

### Visual Verification:
- [ ] gujaratmilk1.jpg background visible
- [ ] Dark overlay applied (35% opacity)
- [ ] Login form centered
- [ ] Form has glassmorphic effect
- [ ] Form responsive on different screen sizes

### Authentication Flow:
- [ ] Valid credentials → Dashboard
- [ ] Invalid credentials → Error message
- [ ] Remember me working (optional)
- [ ] Forgot password link present

---

## Test Case 9: Notification Bell Interaction

### Navigation:
1. Anywhere on the site, click notification bell 🔔
2. **Verify:**
   - [ ] Redirects to /notifications page
   - [ ] Correct notifications shown for logged-in user

### Badge Display:
1. After marking all as read
   - [ ] Badge disappears
2. After marking one as unread
   - [ ] Badge shows "1"
3. Delete notification
   - [ ] Badge count updates if applicable

---

## Test Case 10: Complete User Flow

### Farmer Complete Journey:
```
Login (farmer)
  ↓
FarmerDashboard (see farmers chart)
  ↓
Collections (see F002 collections)
  ↓
Payments (see F002 payments)
  ↓
Quality Tests (see F002 tests)
  ↓
Notifications (see 6 farmer notifs)
  ↓
Mark some as read
  ↓
Switch language to Gujarati
  ↓
View profile
  ↓
Logout
```

### Staff Complete Journey:
```
Login (staff)
  ↓
CollectionCenterDashboard (see Anand center)
  ↓
Collections (see Anand collections)
  ↓
Payments (see Anand payments)
  ↓
Quality Tests (see Anand tests)
  ↓
Reports (center-specific)
  ↓
Notifications (see 4 staff notifs)
  ↓
Logout
```

### Admin Complete Journey:
```
Login (admin)
  ↓
AdminDashboard (see all-system view)
  ↓
Collections (see all collections)
  ↓
Payments (see all payments)
  ↓
Quality Tests (see all tests)
  ↓
Reports (system-wide)
  ↓
Notifications (see 1 admin notif)
  ↓
Logout
```

---

## Test Case 11: No Console Errors

Open browser DevTools (F12) and check:
- [ ] No JavaScript errors
- [ ] No 404 errors
- [ ] No network errors
- [ ] All assets load correctly
- [ ] LocalStorage working (auth persistence)

---

## Success Criteria Checklist

### Must Pass:
- [ ] All 3 demo users can login
- [ ] Notification badge shows correct count for each role
- [ ] Each role sees only their notifications
- [ ] Mark as read/unread works
- [ ] Delete notification works
- [ ] Filters work correctly
- [ ] Dashboard shows correct data per role
- [ ] All pages show role-specific data
- [ ] Multi-language switching works
- [ ] No console errors
- [ ] Responsive design works

### Nice to Have:
- [ ] Notification sound on new notification (could add)
- [ ] Real-time notification updates (currently static)
- [ ] Notification history archive (could add)
- [ ] Export notifications as CSV (could add)

---

## Backend Integration Testing

### API Endpoints to Test (when backend running):

1. **Authentication:**
   - POST /auth/login
   - POST /auth/logout
   - GET /auth/verify

2. **Collections:**
   - GET /collections
   - POST /collections
   - GET /collections/:id

3. **Payments:**
   - GET /payments
   - GET /payments/:id

4. **Quality Tests:**
   - GET /quality-tests
   - POST /quality-tests

5. **Reports:**
   - GET /reports

---

## Known Limitations & Future Scope

1. **Notifications are static demo data** - Not from Backend
2. **No real-time updates** - Page refresh required to see new data
3. **localStorage only** - No database persistence for mark as read status
4. **Mock images** - Using ASCII art instead of real photos
5. **No push notifications** - No browser/mobile notifications

---

## How to Report Issues

If you find any:

1. **Screenshot the issue**
2. **Note the role (farmer/staff/admin)**
3. **Note the page/feature**
4. **Open Browser DevTools (F12) and check console**
5. **Describe exact steps to reproduce**

---

## Quick Debug Commands

### Clear localStorage (if stuck):
```javascript
// Run in browser console (F12)
localStorage.clear()
location.reload()
```

### Check Notifications in Console:
```javascript
// Run in browser console
const MOCK_NOTIFICATIONS = /* copy from mockData.js */
const farmer = MOCK_NOTIFICATIONS.filter(n => n.toRole === 'farmer')
const staff = MOCK_NOTIFICATIONS.filter(n => n.toRole === 'staff')
const admin = MOCK_NOTIFICATIONS.filter(n => n.toRole === 'admin')
console.table({farmer: farmer.length, staff: staff.length, admin: admin.length})
```

---

**Last Updated:** April 6, 2026
**System Version:** 1.0.0
**Test Duration:** ~30-45 minutes for full coverage
