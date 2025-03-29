import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import joblib

# Load dataset
df = pd.read_csv("labeled_c_dataset_fixed.csv")

# Vectorize C code
vectorizer = TfidfVectorizer()
X_buggy = vectorizer.fit_transform(df["Buggy Code"]).toarray()
y_fixed = vectorizer.transform(df["Fixed Code"]).toarray()  # Transform using same vectorizer

# Save processed data
np.save("processed_data/X_buggy.npy", X_buggy)
np.save("processed_data/y_fixed.npy", y_fixed)

# Save vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Code vectorization completed!")
