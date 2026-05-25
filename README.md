# 📊 Telecom Customer Churn Prediction Dashboard

## 🚀 Overview

An end-to-end Machine Learning and Data Analytics project that predicts telecom customer churn using PostgreSQL, Python, Scikit-learn, and Streamlit.

This project simulates a real-world business problem where telecom companies aim to identify customers likely to leave their service. The application provides churn risk predictions along with interactive business insights through a professional dashboard interface.

---

# 🎯 Project Objectives

- Analyze telecom customer behavior
- Identify churn patterns and business risks
- Build a machine learning model for churn prediction
- Develop an interactive analytics dashboard
- Demonstrate end-to-end data workflow skills

---

# 🛠️ Tech Stack

## Languages & Libraries
- Python
- Pandas
- Scikit-learn
- Streamlit
- Plotly

## Database
- PostgreSQL

## Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

# ⚙️ Features

✅ PostgreSQL database integration  
✅ ETL data loading pipeline  
✅ SQL-based analytics queries  
✅ Exploratory Data Analysis (EDA)  
✅ Feature engineering & preprocessing  
✅ Random Forest Machine Learning model  
✅ Real-time churn prediction  
✅ Interactive Streamlit dashboard  
✅ KPI cards and churn risk gauge  
✅ Business insights generation  

---

# 📈 Machine Learning

### Model Used
- Random Forest Classifier

### Prediction Target
- Customer Churn (Yes / No)

### Key Features
- Customer Tenure
- Monthly Charges
- Contract Type

---

# 📊 Dashboard Capabilities

The Streamlit dashboard allows users to:

- Input customer information
- Predict churn probability
- View churn risk score
- Analyze business insights
- Explore customer retention indicators

---

# 🧠 Business Insights

Key findings from the analysis:

- Month-to-month contracts have significantly higher churn rates
- Customers with short tenure are more likely to leave
- Higher monthly charges increase churn risk
- Long-term contracts improve customer retention

---

# 🗂️ Project Structure

```bash
telecom-churn-platform/
│
├── app/
│   └── app.py
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── scripts/
│   ├── load_data.py
│   └── test_connection.py
│
├── requirements.txt
│
└── README.md
