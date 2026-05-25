import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:12345@localhost:5432/telecom_churn"
)

df = pd.read_sql("SELECT version();", engine)

print(df)