
# 📊 Credit Risk Prediction App

An end-to-end **Credit Risk Modelling** app using machine learning, deployed with **Streamlit**.

Predict the likelihood of a borrower defaulting based on financial history, income, loan details, and behavioral metrics. Built as part of a portfolio project to demonstrate data science and model deployment skills.

🔗 **Live App**: [mlprojcreditriskmodel.streamlit.app](https://mlprojcreditriskmodel.streamlit.app/)

---

## 🧠 Key Features

- ✅ Predicts **Default Probability**, **Credit Score**, and **Risk Rating**
- 🧮 Calculates important metrics like **Loan-to-Income Ratio**
- 🎯 Accepts inputs like income, loan amount, purpose, DPD, open accounts, etc.
- 📊 Interactive UI with sliders, metrics, dropdowns, and real-time risk evaluation
- 🖼️ Animated and responsive interface with **Lottie** integration
- 🚀 Deployed publicly using **Streamlit Cloud**

---

## 📁 Project Structure

```
├── app/
│   ├── artifacts/
│   │   └── model_data.joblib         # Trained model
│   ├── app.py                        # Streamlit UI (entrypoint)
│   ├── main.py                       # Optional for CLI/local runs
│   └── prediction_helper.py          # Input preprocessing and prediction logic
│
├── artifacts/
│   └── model_data.joblib             # Backup model storage
│
├── dataset/
│   ├── bureau_data.csv
│   ├── customers.csv
│   └── loans.csv                     # Source datasets
│
├── credit_risk_model_codebasics.ipynb  # Development notebook
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/credit-risk-app.git
cd credit-risk-app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> ✅ Compatible with **Python 3.10+**. For Python 3.12, use `numpy>=1.26.0`.

### 3️⃣ Run the Streamlit App

```bash
streamlit run app/app.py
```

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Streamlit** for frontend & deployment
- **scikit-learn** for model training
- **XGBoost** for gradient boosting models
- **pandas**, **numpy** for data handling
- **joblib** for model serialization


---



---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Built during the [Codebasics ML Course](https://codebasics.io/)


---


