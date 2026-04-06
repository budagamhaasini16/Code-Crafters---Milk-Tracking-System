import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Milk Collection and Quality Tracking System – Gujarat",
    page_icon="🥛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom colorful CSS styling
st.markdown("""
    <style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #f0fdf4 0%, #e0f7f4 100%);
        padding: 2rem;
    }
    
    /* Login form styling */
    .login-container {
        background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
        border-radius: 20px;
        padding: 2rem;
        border: 3px solid #10b981;
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.2);
    }
    
    /* Title styling */
    .title-main {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 6px rgba(16, 185, 129, 0.1);
    }
    
    /* Subtitle styling */
    .subtitle {
        background: linear-gradient(135deg, #f59e0b 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 2rem;
    }
    
    /* Divider */
    .divider {
        height: 4px;
        background: linear-gradient(90deg, #10b981 0%, #f59e0b 50%, #ec4899 100%);
        border-radius: 2px;
        margin: 2rem 0;
    }
    
    /* Demo credentials cards */
    .demo-card {
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        border: 3px solid;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .demo-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
    }
    
    .farmer-card {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        border-color: #1e40af;
    }
    
    .staff-card {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        border-color: #b45309;
    }
    
    .admin-card {
        background: linear-gradient(135deg, #a855f7 0%, #7c3aed 100%);
        border-color: #5b21b6;
    }
    
    .demo-card h3 {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .demo-card p {
        font-size: 0.95rem;
        line-height: 1.6;
        margin: 0.3rem 0;
    }
    
    /* Form inputs */
    .stTextInput > div > div > input {
        border: 2px solid #10b981 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #059669 !important;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1) !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4) !important;
    }
    
    /* Metric cards */
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #dcfce7 !important;
        color: #166534 !important;
        border-left: 5px solid #22c55e !important;
        border-radius: 8px !important;
    }
    
    /* Error messages */
    .stError {
        background-color: #fee2e2 !important;
        color: #991b1b !important;
        border-left: 5px solid #ef4444 !important;
        border-radius: 8px !important;
    }
    
    /* Info messages */
    .stInfo {
        background-color: #e0f2fe !important;
        color: #0c2d48 !important;
        border-left: 5px solid #0ea5e9 !important;
        border-radius: 8px !important;
    }
    
    /* Dashboard header */
    .dashboard-header {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.2);
    }
    
    /* Sidebar */
    .stSidebar {
        background: linear-gradient(180deg, #f0fdf4 0%, #e0f7f4 100%);
    }
    
    .stSidebar > div:first-child {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Mock Data
MOCK_FARMERS = {
    'F002': {
        'id': 'F002',
        'name': 'Ramesh Kumar',
        'email': 'farmer@milktrack.com',
        'farmer_id': 'F002',
        'farm_name': 'Kumar Premium Dairy',
        'farm_address': 'Village: Anand, Taluka: Anand, District: Anand, State: Gujarat',
        'animals': [
            {'id': 'ANM001', 'type': 'Cow', 'breed': 'Holstein', 'age': 5, 'milk_capacity': 22},
            {'id': 'ANM002', 'type': 'Buffalo', 'breed': 'Murrah', 'age': 7, 'milk_capacity': 28},
            {'id': 'ANM003', 'type': 'Cow', 'breed': 'Jersey', 'age': 3, 'milk_capacity': 20}
        ]
    },
    'F001': {
        'id': 'F001',
        'name': 'Rajesh Patel',
        'email': 'rajesh@milktrack.com',
        'farmer_id': 'F001',
        'farm_name': 'Patel Premium Dairy',
        'farm_address': 'Village: Dharod, Taluka: Anand, District: Anand, State: Gujarat',
        'animals': [
            {'id': 'ANM004', 'type': 'Buffalo', 'breed': 'Murrah', 'age': 6, 'milk_capacity': 19}
        ]
    },
    'F003': {
        'id': 'F003',
        'name': 'Vikram Singh',
        'email': 'vikram@milktrack.com',
        'farmer_id': 'F003',
        'farm_name': 'Singh Dairy Farm',
        'farm_address': 'Village: Kheda, Taluka: Kheda, District: Kheda, State: Gujarat',
        'animals': []
    }
}

MOCK_COLLECTIONS = [
    {
        'id': 'COL001', 'farmer_id': 'F002', 'farmer_name': 'Ramesh Kumar',
        'date': datetime(2026, 4, 6), 'time': '06:30 AM', 'quantity': 15.5,
        'fat_percentage': 6.2, 'snf_percentage': 8.3, 'quality': 'A', 'amount': 775,
        'center_name': 'Anand Collection Center'
    },
    {
        'id': 'COL002', 'farmer_id': 'F002', 'farmer_name': 'Ramesh Kumar',
        'date': datetime(2026, 4, 6), 'time': '06:00 PM', 'quantity': 12,
        'fat_percentage': 5.8, 'snf_percentage': 8.1, 'quality': 'A', 'amount': 555,
        'center_name': 'Anand Collection Center'
    },
    {
        'id': 'COL003', 'farmer_id': 'F002', 'farmer_name': 'Ramesh Kumar',
        'date': datetime(2026, 4, 5), 'time': '06:30 AM', 'quantity': 14,
        'fat_percentage': 6.0, 'snf_percentage': 8.2, 'quality': 'A', 'amount': 700,
        'center_name': 'Anand Collection Center'
    },
    {
        'id': 'COL004', 'farmer_id': 'F001', 'farmer_name': 'Rajesh Patel',
        'date': datetime(2026, 4, 6), 'time': '06:30 AM', 'quantity': 18.5,
        'fat_percentage': 6.5, 'snf_percentage': 8.5, 'quality': 'A', 'amount': 950,
        'center_name': 'Dharod Collection Center'
    },
    {
        'id': 'COL005', 'farmer_id': 'F003', 'farmer_name': 'Vikram Singh',
        'date': datetime(2026, 4, 6), 'time': '07:00 AM', 'quantity': 10.2,
        'fat_percentage': 5.5, 'snf_percentage': 7.9, 'quality': 'B', 'amount': 450,
        'center_name': 'Kheda Collection Center'
    }
]

MOCK_PAYMENTS = [
    {
        'id': 'PAY001', 'farmer_id': 'F002', 'farmer_name': 'Ramesh Kumar',
        'date': datetime(2026, 4, 1), 'total_quantity': 89.5, 'total_amount': 4550,
        'payment_method': 'Bank Transfer', 'status': 'paid'
    },
    {
        'id': 'PAY002', 'farmer_id': 'F002', 'farmer_name': 'Ramesh Kumar',
        'date': datetime(2026, 3, 25), 'total_quantity': 85.0, 'total_amount': 4350,
        'payment_method': 'Bank Transfer', 'status': 'paid'
    }
]

MOCK_QUALITY_TESTS = [
    {
        'id': 'QT001', 'farmer_id': 'F002', 'collection_id': 'COL001',
        'date': datetime(2026, 4, 6), 'time': '07:00 AM',
        'fat_content': 6.2, 'snf_content': 8.3, 'acidity': 0.14,
        'density': 1.028, 'cleanliness': 'A', 'quality': 'A', 'tested_by': 'Lab Tech 1'
    },
    {
        'id': 'QT002', 'farmer_id': 'F001', 'collection_id': 'COL004',
        'date': datetime(2026, 4, 6), 'time': '07:30 AM',
        'fat_content': 6.5, 'snf_content': 8.5, 'acidity': 0.13,
        'density': 1.029, 'cleanliness': 'A', 'quality': 'A', 'tested_by': 'Lab Tech 2'
    }
]

COLLECTION_CENTERS = [
    {'id': 'CC001', 'name': 'Anand Collection Center', 'location': 'Anand, Gujarat'},
    {'id': 'CC002', 'name': 'Dharod Collection Center', 'location': 'Dharod, Gujarat'},
    {'id': 'CC003', 'name': 'Kheda Collection Center', 'location': 'Kheda, Gujarat'}
]

DEMO_USERS = {
    'farmer@milktrack.com': {'password': 'Demo@123', 'role': 'farmer', 'farmer_id': 'F002', 'name': 'Ramesh Kumar'},
    'staff@milktrack.com': {'password': 'Demo@123', 'role': 'staff', 'center_name': 'Anand Collection Center', 'name': 'Anand Staff'},
    'admin@milktrack.com': {'password': 'Demo@123', 'role': 'admin', 'name': 'System Admin'}
}

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'

def login_user(email, password):
    """Authenticate user with demo credentials"""
    if email in DEMO_USERS and DEMO_USERS[email]['password'] == password:
        st.session_state.user = {
            'email': email,
            'role': DEMO_USERS[email]['role'],
            'name': DEMO_USERS[email]['name'],
            'farmer_id': DEMO_USERS[email].get('farmer_id'),
            'center_name': DEMO_USERS[email].get('center_name')
        }
        st.success(f"✅ Welcome, {st.session_state.user['name']}!")
        st.rerun()
    else:
        st.error("❌ Invalid credentials. Try Demo@123")

def logout_user():
    """Logout current user"""
    st.session_state.user = None
    st.session_state.page = 'dashboard'
    st.rerun()

# Login Page
def page_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='color: #10b981; font-size: 2.5rem;'>🥛 Milk Collection and Quality Tracking</h1>
            <h2 style='color: #059669; font-size: 1.3rem;'>Gujarat Dairy Cooperative – System</h2>
            <hr style='border: 2px solid #10b981;'>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            st.markdown("### 🔐 Login to Your Account")
            email = st.text_input("📧 Email", placeholder="farmer@milktrack.com")
            password = st.text_input("🔑 Password", type="password", placeholder="Demo@123")
            
            col_login, col_guest = st.columns(2)
            with col_login:
                if st.form_submit_button("🚪 Login", use_container_width=True):
                    if email and password:
                        login_user(email, password)
                    else:
                        st.error("Please enter both email and password")
        
        st.markdown("---")
        
        with st.expander("📝 Demo Credentials - Click to Expand"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div style='background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 1.5rem; border-radius: 10px; color: white;'>
                <h4>👨‍🌾 Farmer</h4>
                <p><strong>Email:</strong></p>
                <code>farmer@milktrack.com</code>
                <p><strong>Password:</strong></p>
                <code>Demo@123</code>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 1.5rem; border-radius: 10px; color: white;'>
                <h4>👔 Staff</h4>
                <p><strong>Email:</strong></p>
                <code>staff@milktrack.com</code>
                <p><strong>Password:</strong></p>
                <code>Demo@123</code>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div style='background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); padding: 1.5rem; border-radius: 10px; color: white;'>
                <h4>👨‍💼 Admin</h4>
                <p><strong>Email:</strong></p>
                <code>admin@milktrack.com</code>
                <p><strong>Password:</strong></p>
                <code>Demo@123</code>
                </div>
                """, unsafe_allow_html=True)

# Farmer Dashboard
def page_farmer_dashboard():
    user = st.session_state.user
    farmer = MOCK_FARMERS.get(user['farmer_id'])
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
    <h1 style='margin: 0; font-size: 2.5rem;'>🚜 Welcome, {farmer['name']}!</h1>
    <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'><strong>Farm:</strong> {farmer['farm_name']}</p>
    <p style='margin: 0.5rem 0 0 0; font-size: 1rem;'><strong>Location:</strong> {farmer['farm_address'].split(',')[0]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # My Collections
    collections = [c for c in MOCK_COLLECTIONS if c['farmer_id'] == user['farmer_id']]
    payments = [p for p in MOCK_PAYMENTS if p['farmer_id'] == user['farmer_id']]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>Total Deliveries</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>""" + str(len(collections)) + """</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        total_qty = sum(c['quantity'] for c in collections)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>Total Supply</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>{total_qty:.1f}L</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total_earnings = sum(c['amount'] for c in collections)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>Total Earnings</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>₹{total_earnings:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_fat = (sum(c['fat_percentage'] for c in collections) / len(collections)) if collections else 0
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #ec4899 0%, #be185d 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>Avg Fat Content</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>{avg_fat:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #10b981;'>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("### 📋 Recent Collections")
        
        if collections:
            df = pd.DataFrame(collections)
            df['date'] = df['date'].dt.strftime('%d-%m-%Y')
            df = df[['id', 'date', 'time', 'quantity', 'fat_percentage', 'snf_percentage', 'quality', 'amount']]
            df.columns = ['ID', 'Date', 'Time', 'Qty (L)', 'Fat %', 'SNF %', 'Grade', 'Amount (₹)']
            
            for idx, row in df.iterrows():
                color = '#10b981' if row['Grade'] == 'A' else '#f59e0b' if row['Grade'] == 'B' else '#ef4444'
                st.markdown(f"""
                <div style='background: #f8f9fa; border-left: 4px solid {color}; padding: 1rem; margin: 0.5rem 0; border-radius: 5px;'>
                <div style='display: flex; justify-content: space-between;'>
                <strong>{row['Date']} {row['Time']}</strong>
                <span style='background: {color}; color: white; padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.85rem;'>{row['Grade']}</span>
                </div>
                <p style='margin: 0.5rem 0; font-size: 0.95rem;'>{row['Qty (L)']}L • Fat: {row['Fat %']}% • Amount: ₹{row['Amount (₹)']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No collections found")
    
    with col_right:
        st.markdown("### 🐄 My Animals")
        if farmer['animals']:
            for idx, animal in enumerate(farmer['animals']):
                emoji = '🐄' if animal['type'] == 'Cow' else '🐃'
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); padding: 1.5rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #3b82f6;'>
                <h4 style='margin: 0; color: #1e40af;'>{emoji} {animal['breed']}</h4>
                <p style='margin: 0.5rem 0 0 0; font-size: 0.95rem;'><strong>Type:</strong> {animal['type']} | <strong>Age:</strong> {animal['age']} years</p>
                <p style='margin: 0 0 0 0; font-size: 0.95rem;'><strong>Capacity:</strong> {animal['milk_capacity']}L/day</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No animals registered")

# Staff Dashboard
def page_staff_dashboard():
    user = st.session_state.user
    center_collections = [c for c in MOCK_COLLECTIONS if c['center_name'] == user['center_name']]
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
    <h1 style='margin: 0; font-size: 2.5rem;'>📍 {user['center_name']}</h1>
    <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>Staff Dashboard • Today's Operations</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem;'>Collections</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>{len(center_collections)}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        total_qty = sum(c['quantity'] for c in center_collections)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem;'>Total Qty</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>{total_qty:.1f}L</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total_amount = sum(c['amount'] for c in center_collections)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem;'>Total Value</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>₹{total_amount:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        farmers = len(set(c['farmer_id'] for c in center_collections))
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='margin: 0; font-size: 0.9rem;'>Farmers</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: bold;'>{farmers}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #f59e0b;'>", unsafe_allow_html=True)
    st.markdown("### 🥛 Collections at Center")
    
    if center_collections:
        df = pd.DataFrame(center_collections)
        df['date'] = df['date'].dt.strftime('%d-%m-%Y')
        df = df[['id', 'farmer_name', 'date', 'time', 'quantity', 'fat_percentage', 'quality', 'amount']]
        df.columns = ['Collection ID', 'Farmer', 'Date', 'Time', 'Qty (L)', 'Fat %', 'Grade', 'Amount (₹)']
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No collections at this center")

# Admin Dashboard
def page_admin_dashboard():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
    <h1 style='margin: 0; font-size: 2.5rem;'>📊 System Overview</h1>
    <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>Complete system analytics and management</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Collections</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{len(MOCK_COLLECTIONS)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        total_qty = sum(c['quantity'] for c in MOCK_COLLECTIONS)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Quantity</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{total_qty:.1f}L</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        total_amount = sum(c['amount'] for c in MOCK_COLLECTIONS)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Revenue</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>₹{total_amount/1000:.0f}K</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        farmers = len(set(c['farmer_id'] for c in MOCK_COLLECTIONS))
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #ec4899 0%, #be185d 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Farmers</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{farmers}</p>
        </div>
        """, unsafe_allow_html=True)
    with col5:
        centers = len(set(c['center_name'] for c in MOCK_COLLECTIONS))
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Centers</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{centers}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #8b5cf6;'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Quality Distribution")
        quality_counts = {
            '🟢 Grade A': len([c for c in MOCK_COLLECTIONS if c['quality'] == 'A']),
            '🟡 Grade B': len([c for c in MOCK_COLLECTIONS if c['quality'] == 'B']),
            '🔴 Grade C': len([c for c in MOCK_COLLECTIONS if c['quality'] == 'C'])
        }
        st.bar_chart(quality_counts)
    
    with col2:
        st.markdown("### 📍 Collections by Center")
        center_counts = {}
        for c in MOCK_COLLECTIONS:
            center_name = c['center_name'].split()[0]
            center_counts[center_name] = center_counts.get(center_name, 0) + 1
        st.bar_chart(center_counts)
    
    st.markdown("<hr style='border: 2px solid #8b5cf6;'>", unsafe_allow_html=True)
    st.markdown("### 📋 All Collections")
    df = pd.DataFrame(MOCK_COLLECTIONS)
    df['date'] = df['date'].dt.strftime('%d-%m-%Y')
    df = df[['id', 'farmer_name', 'center_name', 'date', 'quantity', 'amount', 'quality']]
    df.columns = ['ID', 'Farmer', 'Center', 'Date', 'Qty (L)', 'Amount (₹)', 'Grade']
    st.dataframe(df, use_container_width=True, hide_index=True)

# Collections Page
def page_collections():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
    <h1 style='margin: 0; font-size: 2.5rem;'>🥛 Milk Collections</h1>
    <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>Browse and filter all milk collections</p>
    </div>
    """, unsafe_allow_html=True)
    
    user = st.session_state.user
    
    # Filter based on role
    if user['role'] == 'farmer':
        collections = [c for c in MOCK_COLLECTIONS if c['farmer_id'] == user['farmer_id']]
    elif user['role'] == 'staff':
        collections = [c for c in MOCK_COLLECTIONS if c['center_name'] == user['center_name']]
    else:
        collections = MOCK_COLLECTIONS
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        quality_filter = st.selectbox("🎯 Quality Grade", ["All", "A", "B", "C"])
    with col2:
        date_from = st.date_input("📅 From Date", pd.Timestamp(2026, 4, 1))
    with col3:
        date_to = st.date_input("📅 To Date", pd.Timestamp(2026, 4, 6))
    
    # Apply filters
    if quality_filter != "All":
        collections = [c for c in collections if c['quality'] == quality_filter]
    
    collections = [c for c in collections if date_from <= c['date'].date() <= date_to]
    
    # Display stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Collections</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{len(collections)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        total_qty = sum(c['quantity'] for c in collections)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Quantity</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{total_qty:.1f}L</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        avg_fat = (sum(c['fat_percentage'] for c in collections) / len(collections)) if collections else 0
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Avg Fat %</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{avg_fat:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        total_amount = sum(c['amount'] for c in collections)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #ec4899 0%, #be185d 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Total Value</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>₹{total_amount:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #10b981;'>", unsafe_allow_html=True)
    
    if collections:
        df = pd.DataFrame(collections)
        df['date'] = df['date'].dt.strftime('%d-%m-%Y')
        df = df[['id', 'farmer_name', 'center_name', 'date', 'time', 'quantity', 'fat_percentage', 'snf_percentage', 'quality', 'amount']]
        df.columns = ['ID', 'Farmer', 'Center', 'Date', 'Time', 'Qty (L)', 'Fat %', 'SNF %', 'Grade', 'Amount (₹)']
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No collections found for the selected filters")

# Payments Page
def page_payments():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
    <h1 style='margin: 0; font-size: 2.5rem;'>💳 Payments & Transactions</h1>
    <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>Payment history and settlement status</p>
    </div>
    """, unsafe_allow_html=True)
    
    user = st.session_state.user
    
    if user['role'] == 'farmer':
        payments = [p for p in MOCK_PAYMENTS if p['farmer_id'] == user['farmer_id']]
    else:
        payments = MOCK_PAYMENTS
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Total Payments</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{len(payments)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        total_amount = sum(p['total_amount'] for p in payments)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Total Amount</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>₹{total_amount:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        paid = len([p for p in payments if p['status'] == 'paid'])
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #ec4899 0%, #be185d 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Paid ✓</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{paid}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #f59e0b;'>", unsafe_allow_html=True)
    
    if payments:
        df = pd.DataFrame(payments)
        df['date'] = df['date'].dt.strftime('%d-%m-%Y')
        df['status'] = df['status'].str.upper()
        df = df[['id', 'farmer_name', 'date', 'total_quantity', 'total_amount', 'payment_method', 'status']]
        df.columns = ['Payment ID', 'Farmer', 'Date', 'Quantity (L)', 'Amount (₹)', 'Method', 'Status']
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No payments found")

# Quality Tests Page
def page_quality_tests():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%); padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
    <h1 style='margin: 0; font-size: 2.5rem;'>🧪 Quality Tests</h1>
    <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>Milk quality analysis and testing</p>
    </div>
    """, unsafe_allow_html=True)
    
    user = st.session_state.user
    
    if user['role'] == 'farmer':
        tests = [t for t in MOCK_QUALITY_TESTS if t['farmer_id'] == user['farmer_id']]
    else:
        tests = MOCK_QUALITY_TESTS
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Total Tests</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{len(tests)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        grade_a = len([t for t in tests if t['quality'] == 'A'])
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Grade A 🟢</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{grade_a}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        avg_fat = (sum(t['fat_content'] for t in tests) / len(tests)) if tests else 0
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 1.2rem; border-radius: 10px; color: white; text-align: center;'>
        <h4 style='margin: 0; font-size: 0.8rem;'>Avg Fat %</h4>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: bold;'>{avg_fat:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #06b6d4;'>", unsafe_allow_html=True)
    
    if tests:
        df = pd.DataFrame(tests)
        df['date'] = df['date'].dt.strftime('%d-%m-%Y')
        df = df[['id', 'collection_id', 'date', 'time', 'fat_content', 'snf_content', 'acidity', 'density', 'quality', 'tested_by']]
        df.columns = ['Test ID', 'Collection ID', 'Date', 'Time', 'Fat %', 'SNF %', 'Acidity', 'Density', 'Grade', 'Tested By']
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No quality tests found")

# Main App
def main():
    if st.session_state.user is None:
        page_login()
    else:
        # Sidebar
        with st.sidebar:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.5rem; border-radius: 10px; color: white; margin-bottom: 1.5rem;'>
            <h3 style='margin: 0; font-size: 1.2rem;'>👤 """ + st.session_state.user['name'] + """</h3>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.95rem;'><strong>Role:</strong> """ + st.session_state.user['role'].upper() + """</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Navigation
            if st.session_state.user['role'] == 'farmer':
                pages = {
                    '🏠 Dashboard': 'dashboard',
                    '🥛 Collections': 'collections',
                    '💳 Payments': 'payments',
                    '🧪 Quality Tests': 'quality_tests'
                }
            elif st.session_state.user['role'] == 'staff':
                pages = {
                    '🏠 Dashboard': 'dashboard',
                    '🥛 Collections': 'collections',
                    '💳 Payments': 'payments',
                    '🧪 Quality Tests': 'quality_tests'
                }
            else:  # admin
                pages = {
                    '📊 Dashboard': 'dashboard',
                    '🥛 Collections': 'collections',
                    '💳 Payments': 'payments',
                    '🧪 Quality Tests': 'quality_tests'
                }
            
            for page_name, page_key in pages.items():
                if st.button(page_name, use_container_width=True, key=page_key):
                    st.session_state.page = page_key
                    st.rerun()
            
            st.markdown("---")
            if st.button("🚪 Logout", use_container_width=True):
                logout_user()
        
        # Main content
        if st.session_state.page == 'dashboard':
            if st.session_state.user['role'] == 'farmer':
                page_farmer_dashboard()
            elif st.session_state.user['role'] == 'staff':
                page_staff_dashboard()
            else:
                page_admin_dashboard()
        elif st.session_state.page == 'collections':
            page_collections()
        elif st.session_state.page == 'payments':
            page_payments()
        elif st.session_state.page == 'quality_tests':
            page_quality_tests()

if __name__ == "__main__":
    main()
