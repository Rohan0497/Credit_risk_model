import streamlit as st
import matplotlib.pyplot as plt
from prediction_helper import predict

# Page config
st.set_page_config(page_title="Credit Risk Modelling", page_icon="📊", layout="wide")

# Sidebar
with st.sidebar:
    st.image("assets/credit_risk_thumbnail.png", width=200)
    st.markdown("### 📊 Credit Risk Modelling")
    st.write("Predict default risk, credit score & risk category using financial and behavioral inputs.")

# Title
st.markdown("<h1 style='color:#4A90E2;'>Credit Risk Modelling Dashboard</h1>", unsafe_allow_html=True)
st.markdown("#### 🧠 Enter applicant details to assess credit risk")

# Input Form
with st.form("input_form"):
    st.markdown("### 📝 Applicant Financial Profile")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('👤 Age', min_value=18, max_value=100, step=1, value=28)
    with col2:
        income = st.number_input('💰 Annual Income (₹)', min_value=1, value=1200000)
    with col3:
        loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000)

    loan_to_income_ratio = loan_amount / income

    col4, col5, col6 = st.columns(3)
    with col4:
        loan_tenure_months = st.number_input('📅 Loan Tenure (months)', min_value=1, value=36)
    with col5:
        avg_dpd_per_delinquency = st.number_input('📉 Avg Days Past Due (DPD)', min_value=0, value=20)
    with col6:
        num_open_accounts = st.number_input('📂 Open Loan Accounts', min_value=1, max_value=10, value=2)

    col7, col8, col9 = st.columns(3)
    with col7:
        delinquency_ratio = st.slider('⚠️ Delinquency Ratio (%)', 0, 100, 30)
    with col8:
        credit_utilization_ratio = st.slider('💳 Credit Utilization (%)', 0, 100, 30)
    with col9:
        st.metric("📊 Loan-to-Income Ratio", f"{loan_to_income_ratio:.2f}")

    st.markdown("### 🏠 Additional Information")
    col10, col11, col12 = st.columns(3)
    with col10:
        residence_type = st.selectbox('🏡 Residence Type', ['Owned', 'Rented', 'Mortgage'])
    with col11:
        loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
    with col12:
        loan_type = st.selectbox('🔐 Loan Type', ['Unsecured', 'Secured'])

    submit = st.form_submit_button("🚀 Calculate Risk")

# Prediction
if submit:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months,
        avg_dpd_per_delinquency, delinquency_ratio,
        credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("---")
    st.subheader("📈 Credit Risk Evaluation Results")

    colA, colB, colC = st.columns(3)
    with colA:
        st.metric(label="📉 Default Probability", value=f"{probability:.2%}")
    with colB:
        st.metric(label="🏅 Credit Score", value=f"{credit_score}")
    with colC:
        st.metric(label="✅ Risk Rating", value=rating)

    # Interpretation
    st.markdown("### 📌 Model Interpretation & Suggestions")
    if probability > 0.75:
        st.warning("🔴 High risk: Immediate review recommended.")
    elif probability > 0.5:
        st.info("🟠 Medium risk: Consider additional verification or adjusting credit terms.")
    else:
        st.success("🟢 Low risk: Applicant appears to be creditworthy.")

    # Key Factors
    st.markdown("### 🔍 Key Factors Influencing Risk")
    st.markdown(f"- 📊 **Loan-to-Income Ratio**: `{loan_to_income_ratio:.2f}` → Higher values increase risk.")
    st.markdown(f"- ⚠️ **Delinquency Ratio**: `{delinquency_ratio}%` → Reflects past payment behavior.")
    st.markdown(f"- 💳 **Credit Utilization**: `{credit_utilization_ratio}%` → Usage over 60% may flag risk.")

    # Visualizations
    st.markdown("### 📊 Interactive Risk Visualizations")

    col_v1, col_v2 = st.columns(2)

    with col_v1:
        # Pie Chart
        remaining_income = income - loan_amount
        if remaining_income < 0:
            remaining_income = 0
            st.warning("⚠️ Loan amount exceeds income! Adjust inputs for realistic visualization.")
        fig1, ax1 = plt.subplots()
        ax1.pie(
            [loan_amount, remaining_income],
            labels=["Loan Amount", "Remaining Income"],
            colors=["#ff9999", "#66b3ff"],
            autopct='%1.1f%%',
            startangle=90
        )
        ax1.axis('equal')
        st.pyplot(fig1, use_container_width=True)

    with col_v2:
        # Bar chart
        fig2, ax2 = plt.subplots(figsize=(4, 2))
        ax2.barh(["Delinquency", "Credit Utilization"],
                 [delinquency_ratio, credit_utilization_ratio],
                 color=["orange", "teal"])
        ax2.set_xlim([0, 100])
        ax2.set_xlabel("Percentage (%)")
        st.pyplot(fig2, use_container_width=True)


