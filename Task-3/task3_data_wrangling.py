import pandas as pd

INPUT_FILE = "messy_dataset.csv"
OUTPUT_FILE = "cleaned_dataset.csv"

df = pd.read_csv(INPUT_FILE)
print("Original shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isna().sum())

df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ", "_")
)

for col in ["customer_name", "region", "product", "status"]:
    df[col] = df[col].astype("string").str.strip()

df["region"] = df["region"].str.title()
df["status"] = df["status"].str.title()

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

df["quantity"] = df["quantity"].fillna(df["quantity"].median())
df["unit_price"] = df["unit_price"].fillna(df["unit_price"].median())
for col in ["customer_name", "region", "product", "status"]:
    df[col] = df[col].fillna("Unknown")

df = df.drop_duplicates()

df["total_sales"] = df["quantity"] * df["unit_price"]

filtered_df = df[
    (df["status"] == "Completed") &
    (df["total_sales"] > 1000)
].copy()

filtered_df = filtered_df.sort_values("order_date")
filtered_df.to_csv(OUTPUT_FILE, index=False)

print("\nFinal shape:", filtered_df.shape)
print("\nRemaining missing values:")
print(filtered_df.isna().sum())
print(f"\nSaved cleaned dataset to: {OUTPUT_FILE}")
print("\nPreview:")
print(filtered_df.head(10).to_string(index=False))
