import pandas as pd
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Basic cleaning
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df.dropna(inplace=True)

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:12345@localhost:5432/telecom_churn"
)

# Load into PostgreSQL
df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")
print(df.head())