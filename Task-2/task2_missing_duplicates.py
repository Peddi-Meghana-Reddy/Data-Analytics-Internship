import pandas as pd

INPUT_FILE = "sample_dataset.csv"
OUTPUT_FILE = "cleaned_sample_dataset.csv"

# 1. Load data
df = pd.read_csv(INPUT_FILE)

print("Original shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isna().sum())

# Treat blank strings as missing values as well.
df = df.replace(r"^\s*$", pd.NA, regex=True)

# 2. Handle missing values
numeric_cols = df.select_dtypes(include="number").columns
categorical_cols = df.select_dtypes(exclude="number").columns

for col in numeric_cols:
    if df[col].isna().any():
        df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    if df[col].isna().any():
        mode = df[col].mode(dropna=True)
        if not mode.empty:
            df[col] = df[col].fillna(mode.iloc[0])

# 3. Find and remove exact duplicate rows
exact_duplicates = int(df.duplicated().sum())
df = df.drop_duplicates().copy()

# 4. Check duplicate order IDs (business key)
duplicate_order_ids = int(df["order_id"].duplicated().sum())
df = df.drop_duplicates(subset=["order_id"], keep="first").copy()

print("\nExact duplicate rows found:", exact_duplicates)
print("Duplicate order_id values found:", duplicate_order_ids)

print("\nMissing values after cleaning:")
print(df.isna().sum())

print("\nCleaned shape:", df.shape)

# 5. Save cleaned data
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nSaved cleaned dataset to: {OUTPUT_FILE}")
