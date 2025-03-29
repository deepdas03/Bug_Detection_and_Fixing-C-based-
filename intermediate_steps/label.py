import os
import pandas as pd

# Define input dataset folder
dataset_folder = "dataset"

# Initialize an empty list to store data
data = []

# Loop through all files in the dataset folder
for filename in sorted(os.listdir(dataset_folder)):  
    if filename.endswith(".c"):  # Process only C files
        # Read the C program
        with open(os.path.join(dataset_folder, filename), "r", encoding="utf-8") as f:
            code = f.read()
        
        # Determine the label (buggy = 1, fixed = 0)
        label = 1 if "bug" in filename else 0  

        # Append to the data list
        data.append({"filename": filename, "code": code, "label": label})

# Convert list to a Pandas DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("labeled_c_dataset.csv", index=False)

print("✅ Dataset labeled and saved as 'labeled_c_dataset.csv'")
