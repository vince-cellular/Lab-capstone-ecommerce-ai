import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. File paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

input_file = BASE_DIR / "online_shoppers_intention.csv"
output_file = BASE_DIR / "online_shoppers_intention_clean.csv"


# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------

df = pd.read_csv(input_file)

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

print(f"Original rows: {len(df)}")
print(f"Original columns: {len(df.columns)}")


# --------------------------------------------------
# 3. Check missing values
# --------------------------------------------------

missing_values = df.isnull().sum().sum()

print(f"Total missing values: {missing_values}")


# --------------------------------------------------
# 4. Check duplicate rows
# --------------------------------------------------

duplicate_count = df.duplicated().sum()

print(f"Duplicate rows found: {duplicate_count}")


# --------------------------------------------------
# 5. Remove exact duplicate rows
# --------------------------------------------------

df = df.drop_duplicates().copy()

print(f"Rows after removing exact duplicates: {len(df)}")


# --------------------------------------------------
# 6. Convert boolean fields to clearer labels
# --------------------------------------------------

df["Revenue_Label"] = df["Revenue"].map({
    True: "Converted",
    False: "Not Converted"
})

df["Weekend_Label"] = df["Weekend"].map({
    True: "Weekend",
    False: "Weekday"
})


# --------------------------------------------------
# 7. Save cleaned dataset
# --------------------------------------------------

df.to_csv(output_file, index=False)

print(f"Clean dataset saved to: {output_file}")

print("=" * 60)
print("CLEANING COMPLETE")
print("=" * 60)