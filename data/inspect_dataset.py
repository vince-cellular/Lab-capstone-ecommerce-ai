import pandas as pd

# Load the dataset
file_path = "data/online_shoppers_intention.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("DATASET QUICK INSPECTION")
print("=" * 60)

# 1. Dataset size
print("\n1. Dataset size")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# 2. Column names
print("\n2. Columns")
print(df.columns.tolist())

# 3. Data types
print("\n3. Data types")
print(df.dtypes)

# 4. Missing values
print("\n4. Missing values")
print(df.isnull().sum())

# 5. Duplicate rows
print("\n5. Duplicate rows")
print(f"Duplicates: {df.duplicated().sum()}")

# 6. Revenue distribution
print("\n6. Revenue distribution")
print(df["Revenue"].value_counts())

print("\nRevenue percentages:")
print(df["Revenue"].value_counts(normalize=True) * 100)

# 7. Basic numerical statistics
print("\n7. Numerical statistics")
print(df.describe())

print("\n" + "=" * 60)
print("INSPECTION COMPLETE")
print("=" * 60)