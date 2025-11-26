import streamlit as st
import pandas as pd
import json
import os
import random
from datetime import datetime

# In a real scenario, use: import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="AI Expense Guardian", layout="wide")

# --- AI INTEGRATION (MOCKED FOR DEMO STABILITY) ---
# As the AI Lead, this is where you would connect the actual LLM API.
# We are mocking this to ensure the app runs immediately for your Capstone demo without API keys.

def analyze_receipt_with_ai(uploaded_image):
    """
    Simulates sending the image to an LLM (like Gemini Vision).
    The LLM would OCR the text and Analyze for risk simultaneously.
    """
    # Simulate processing delay
    import time
    time.sleep(1.5)
    
    # Mock Response Logic based on "random" to show variety
    mock_vendors = ["Starbucks", "Uber Rides", "Luxury Casino", "Office Depot", "Delta Airlines"]
    vendor = random.choice(mock_vendors)
    
    amount = round(random.uniform(10.00, 500.00), 2)
    
    # AI Logic: Flag suspicious items
    risk_score = 10
    risk_reason = "Looks normal."
    category = "Travel & Meals"

    if vendor == "Luxury Casino":
        risk_score = 95
        risk_reason = "HIGH RISK: Gambling establishment detected."
        category = "Entertainment"
    elif amount > 300 and vendor == "Starbucks":
        risk_score = 80
        risk_reason = "SUSPICIOUS: unusually high amount for coffee shop."
        category = "Meals"
    elif amount > 1000:
        risk_score = 60
        risk_reason = "Medium Risk: Amount requires manager approval."
    
    return {
        "vendor": vendor,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category,
        "risk_score": risk_score,
        "risk_reason": risk_reason
    }

# --- UI LAYOUT (Low-Code Interface) ---
st.title("🛡️ AI-Enhanced Expense Approval")
st.markdown("### OCR • Anomaly Detection • Auto-Categorization")

# Sidebar for controls
with st.sidebar:
    st.header("Upload Receipt")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    st.info("System Status: AI Model Online 🟢")

col1, col2 = st.columns([1, 1])

if uploaded_file is not None:
    # Display Image
    with col1:
        st.subheader("Original Receipt")
        st.image(uploaded_file, caption='Uploaded Receipt', use_column_width=True)
        
        if st.button("Analyze Expense"):
            with st.spinner('AI is reading receipt and checking policy...'):
                # CALL THE AI FUNCTION
                data = analyze_receipt_with_ai(uploaded_file)
                
                # Store in session state for persistence
                if 'history' not in st.session_state:
                    st.session_state['history'] = []
                st.session_state['history'].append(data)
                
                # Force reload to show results
                st.rerun()

# Display Results
with col2:
    st.subheader("AI Analysis Results")
    
    if 'history' in st.session_state and st.session_state['history']:
        latest = st.session_state['history'][-1]
        
        # Risk Meter
        st.metric(label="Detected Amount", value=f"${latest['amount']}")
        
        risk_color = "green"
        if latest['risk_score'] > 50: risk_color = "orange" 
        if latest['risk_score'] > 80: risk_color = "red"
        
        st.markdown(f"**Risk Score:** :{risk_color}[{latest['risk_score']}/100]")
        st.progress(latest['risk_score'])
        
        st.write(f"**Vendor:** {latest['vendor']}")
        st.write(f"**Category:** {latest['category']}")
        st.write(f"**AI Audit Note:** {latest['risk_reason']}")
        
        if latest['risk_score'] > 75:
            st.error("❌ AUTO-REJECTION RECOMMENDED")
        else:
            st.success("✅ AUTO-APPROVAL RECOMMENDED")

# --- WEEKLY SUMMARY DASHBOARD ---
st.divider()
st.subheader("📊 Team Spending Summary")

# Mock dataframe for dashboard
df = pd.DataFrame({
    "Category": ["Travel", "Meals", "Software", "Office Supplies", "Entertainment"],
    "Amount": [1200, 450, 3000, 150, 600]
})

st.bar_chart(df.set_index("Category"))
