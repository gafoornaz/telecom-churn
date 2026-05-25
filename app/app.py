import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Telecom Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

model = joblib.load(
    r"E:\my projects\telecom-churn-platform\models\churn_model.pkl"
)

# ---------------- TITLE ----------------

st.title("📊 Telecom Customer Churn Dashboard")

st.markdown(
    "Predict customer churn risk using machine learning."
)

# ---------------- SIDEBAR ----------------

st.sidebar.header("Customer Information")

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

monthly_charges = st.sidebar.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

contract = st.sidebar.selectbox(
    "Contract Type",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

# ---------------- INPUT DATA ----------------

input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "Contract_One year": [
        1 if contract == "One year" else 0
    ],
    "Contract_Two year": [
        1 if contract == "Two year" else 0
    ]
})

# ---------------- KPI CARDS ----------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Tenure",
    f"{tenure} Months"
)

col2.metric(
    "Monthly Charges",
    f"${monthly_charges:.2f}"
)

col3.metric(
    "Contract",
    contract
)

st.divider()

# ---------------- PREDICTION ----------------

if st.button("Predict Churn Risk"):

    prediction = model.predict(
        input_data
    )[0]

    probability = model.predict_proba(
        input_data
    )[0][1]

    # ---------------- RESULT ----------------

    if prediction == 1:

        st.error(
            f"⚠️ High Churn Risk "
            f"({probability:.2%})"
        )

    else:

        st.success(
            f"✅ Low Churn Risk "
            f"({probability:.2%})"
        )

    # ---------------- GAUGE CHART ----------------

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={
            "text": "Churn Risk Score"
        },
        gauge={
            "axis": {
                "range": [0, 100]
            },
            "bar": {
                "thickness": 0.3
            },
            "steps": [
                {
                    "range": [0, 40],
                    "color": "lightgreen"
                },
                {
                    "range": [40, 70],
                    "color": "orange"
                },
                {
                    "range": [70, 100],
                    "color": "red"
                }
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------- BUSINESS INSIGHTS ----------------

    st.subheader("Business Insights")

    if tenure < 12:
        st.write(
            "- New customers are more likely to churn."
        )

    if monthly_charges > 80:
        st.write(
            "- High monthly charges increase churn risk."
        )

    if contract == "Month-to-month":
        st.write(
            "- Month-to-month contracts have higher churn rates."
        )

    if contract == "Two year":
        st.write(
            "- Long-term contracts improve retention."
        )