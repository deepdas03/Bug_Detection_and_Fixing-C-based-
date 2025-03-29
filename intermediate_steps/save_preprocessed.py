import numpy as np
import pandas as pd
import os

# Create directory if not exists
processed_folder = "processed_data"
os.makedirs(processed_folder, exist_ok=True)

# Load data
df = pd.read_csv("labeled_c_dataset.csv")
X_train = np.load("X_train.npy")
X_test = np.load("X_test.npy")
y_train = np.load("y_train.npy")
y_test = np.load("y_test.npy")

# Save labeled dataset
df.to_csv(os.path.join(processed_folder, "labeled_data.csv"), index=False)

# Save preprocessed feature vectors
np.save(os.path.join(processed_folder, "X_train.npy"), X_train)
np.save(os.path.join(processed_folder, "X_test.npy"), X_test)
np.save(os.path.join(processed_folder, "y_train.npy"), y_train)
np.save(os.path.join(processed_folder, "y_test.npy"), y_test)

print("✅ Preprocessed data saved successfully!")
