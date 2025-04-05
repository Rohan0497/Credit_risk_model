
# 📊 Credit Risk Prediction App

An end-to-end **Credit Risk Modelling** app using machine learning, deployed with **Streamlit**.

Predict the likelihood of a borrower defaulting based on financial history, income, loan details, and behavioral metrics. Built as part of a portfolio project to demonstrate data science and model deployment skills.

🔗 **Live App**: [mlprojcreditriskmodel.streamlit.app](https://mlprojcreditriskmodel.streamlit.app/)

---

## ❓ Why does it matter?

Credit risk modelling is a **critical part of financial decision-making**. Accurate predictions can:

- Prevent loan defaults  
- Help lenders make informed decisions  
- Improve access to credit for low-risk borrowers  

This app showcases how **machine learning can automate and enhance** the risk evaluation process in real-time.

## 🧠 Key Features

- ✅ Predicts **Default Probability**, **Credit Score**, and **Risk Rating**
- 🧮 Calculates important metrics like **Loan-to-Income Ratio**
- 🎯 Accepts inputs like income, loan amount, purpose, DPD, open accounts, etc.
- 📊 Interactive UI with sliders, metrics, dropdowns, and real-time risk evaluation
- 🖼️ Animated and responsive interface with **Lottie** integration
- 🚀 Deployed publicly using **Streamlit Cloud**

---

##  How It Works

- Users provide input values such as **age**, **income**, **loan amount**, **credit history**, **loan tenure**, and other financial indicators.
- The **Streamlit UI** captures the inputs and sends them to `prediction_helper.py`.
- Inputs are **preprocessed**, converted into model-ready format, and **scaled** using saved preprocessing logic.
- The trained prediction model (`model_data.joblib`) is used to generate:
  - 📉 **Default Probability**
  - 🏅 **Credit Score**
  - ✅ **Risk Rating** (e.g., Low, Medium, High)
- Based on the result:
  - If **Default Probability > 0.5** → User is flagged as **high risk** (🔴)
  - Else → User is marked **low risk** (🟢)
- The result is instantly displayed in the UI using **dynamic metric cards** and **visual cues**.


---


## 📊 Visual Insights

Below are insights gained from data exploration and model diagnostics:

| Screenshot | Description |
|-----------|-------------|
| ![Viz 1](./assets/credit_risk_viz_1.png) | Box plots for continuous variables : Detect outliers and compare spread. |
| ![Viz 2](./assets/credit_risk_viz_2.png) | Additional box plots showing feature behavior across default classes. |
| ![Viz 3](./assets/credit_risk_viz_3.png) | KDE plot for age: Visualizes risky age groups. |
| ![Viz 4](./assets/credit_risk_viz_4.png) | Grid of KDE plots : Feature separation between defaulters and non-defaulters. |
| ![Viz 5](./assets/credit_risk_viz_5.png) | KDE for loan-to-income ratio : Highlights risk clusters. |
| ![Viz 6](./assets/credit_risk_viz_6.png) | KDE for delinquency ratio : Identifies high-risk borrowers. |
| ![Viz 7](./assets/credit_risk_viz_7.png) | KDE of avg DPD: More delay correlates with risk. |
| ![Viz 8](./assets/credit_risk_viz_8.png) | Correlation heatmap: Guides feature selection and reduction. |
| ![Viz 9](./assets/credit_risk_viz_9.png) | Feature importance from Logistic Regression. |
| ![Viz 10](./assets/credit_risk_viz_10.png) | ROC Curve : Evaluates model's classification ability. |
| ![Viz 11](./assets/credit_risk_viz_11.png) | Final feature importance from trained model. |

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
├── credit_risk_model.ipynb  # Development notebook
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Credit_risk_model.git
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



## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Built during the [Codebasics ML Course](https://codebasics.io/)


---



<!---

## 🎥 App in Action

> 👉 Replace the GIF below with a real app demo  
![App Demo](./assets/demo.gif)

---

## 🖼️ Screenshots

| User Input Interface | Prediction Output |
|----------------------|-------------------|
| ![Input](./assets/screenshot_1.png) | ![Output](./assets/screenshot_2.png) |

---
-->