import streamlit as st
from prediction_helper import predict  # Make sure this file is correctly set up

# Page configuration
st.set_page_config(page_title="Credit Risk Modelling", page_icon="📊", layout="wide")

# App Title with style
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📊 Credit Risk Modelling App</h1>", unsafe_allow_html=True)
st.markdown("### 🧠 Enter applicant details to assess their credit risk")

# --- Input Form Section ---
with st.form("input_form"):
    st.markdown("#### 📝 Applicant Financial Profile")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('👤 Age', min_value=18, max_value=100, step=1, value=28)
    with col2:
        income = st.number_input('💰 Annual Income (₹)', min_value=0, value=1200000)
    with col3:
        loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000)

    loan_to_income_ratio = loan_amount / income if income > 0 else 0

    col4, col5, col6 = st.columns(3)
    with col4:
        loan_tenure_months = st.number_input('📅 Loan Tenure (months)', min_value=0, step=1, value=36)
    with col5:
        avg_dpd_per_delinquency = st.number_input('📉 Avg Days Past Due (DPD)', min_value=0, value=20)
    with col6:
        num_open_accounts = st.number_input('📂 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

    col7, col8, col9 = st.columns(3)
    with col7:
        delinquency_ratio = st.slider('⚠️ Delinquency Ratio (%)', 0, 100, 30)
    with col8:
        credit_utilization_ratio = st.slider('💳 Credit Utilization Ratio (%)', 0, 100, 30)
    with col9:
        st.metric("📊 Loan-to-Income Ratio", f"{loan_to_income_ratio:.2f}")

    st.markdown("#### 🏠 Additional Information")

    col10, col11, col12 = st.columns(3)
    with col10:
        residence_type = st.selectbox('🏡 Residence Type', ['Owned', 'Rented', 'Mortgage'])
    with col11:
        loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
    with col12:
        loan_type = st.selectbox('🔐 Loan Type', ['Unsecured', 'Secured'])

    # Submit button
    submit = st.form_submit_button("🚀 Calculate Risk")

# --- Prediction Output Section ---
if submit:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("---")
    st.subheader("📈 Credit Risk Evaluation")

    colA, colB, colC = st.columns(3)
    with colA:
        st.metric(label="🧮 Default Probability", value=f"{probability:.2%}")
    with colB:
        st.metric(label="🏅 Credit Score", value=f"{credit_score}")
    with colC:
        st.metric(label="✅ Risk Rating", value=f"{rating}")

    if probability > 0.5:
        st.error("⚠️ High Risk of Default - Caution Advised")
    else:
        st.success("✅ Low Risk of Default - Likely Safe")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 13px;'>A project powered by Streamlit | Part of Codebasics ML Portfolio</div>", unsafe_allow_html=True)
