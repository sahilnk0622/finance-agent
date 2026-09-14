import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv("sample_transactions.csv")
df["date"] = pd.to_datetime(df["date"])

# Look at the first 5 rows
print(df.head())

# See column names and data types
print(df.info())

# Filter: transactions where amount > 5000
big_spends = df[df["amount"] > 5000]
print(big_spends)

# Group by category, sum the amounts
category_totals = df.groupby("category")["amount"].sum()
print(category_totals)