import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load model & vectorizer
model = load_model("bug_fix_model.h5")
vectorizer = joblib.load("vectorizer.pkl")

# Input new buggy C code
buggy_code = "#include <stdio.h> int main() { int x = 10 printf(%d, x); return 0; }"

# Convert code to vector
X_buggy = vectorizer.transform([buggy_code]).toarray()
X_buggy = X_buggy.reshape((X_buggy.shape[0], 1, X_buggy.shape[1]))

# Predict fixed code
y_pred = model.predict(X_buggy)

# Convert back to text (approximate fix)
fixed_code = vectorizer.inverse_transform(y_pred)[0]

print("🔍 Fixed Code Suggestion:\n", " ".join(fixed_code))
