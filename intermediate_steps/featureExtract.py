import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load labeled dataset
df = pd.read_csv("labeled_c_dataset.csv")

# Preprocess C code (Remove special characters)
def preprocess_code(code):
    code = re.sub(r'[^a-zA-Z0-9\s]', ' ', code)  # Remove special symbols
    return code.lower()  # Convert to lowercase

df["processed_code"] = df["code"].apply(preprocess_code)

# Convert code into TF-IDF vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["processed_code"])  # Feature matrix
y = df["label"]  # Labels

# Save feature matrix for ML model
import numpy as np
np.save("features.npy", X.toarray())  # Save features as .npy file
np.save("labels.npy", y.to_numpy())  # Save labels
print("✅ Code converted to numerical format and saved!")
