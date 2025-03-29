import pandas as pd

# Load the dataset
df = pd.read_csv("labeled_c_dataset.csv")

# Ensure correct column names
if "code" not in df.columns or "label" not in df.columns:
    print("❌ Error: CSV does not have expected columns ('code', 'label')")
    exit()

# Split dataset: buggy code (label = 1) and fixed code (label = 0)
buggy_df = df[df["label"] == 1].rename(columns={"code": "Buggy Code"}).drop(columns=["label"])
fixed_df = df[df["label"] == 0].rename(columns={"code": "Fixed Code"}).drop(columns=["label"])

# Merge both datasets (aligning buggy and fixed code side-by-side)
merged_df = pd.concat([buggy_df.reset_index(drop=True), fixed_df.reset_index(drop=True)], axis=1)

# Save new dataset
merged_df.to_csv("labeled_c_dataset_fixed.csv", index=False)

print("✅ Converted CSV format saved as labeled_c_dataset_fixed.csv!")
