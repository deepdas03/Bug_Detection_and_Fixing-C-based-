import pandas as pd

# Load dataset
df = pd.read_csv("labeled_c_dataset_fixed.csv")

# Check the first few rows
print(df.head())

# Check if columns exist
if "Buggy Code" in df.columns and "Fixed Code" in df.columns:
    print("✅ Dataset is correctly formatted!")
else:
    print("❌ Error: Missing required columns (Buggy Code, Fixed Code)")
