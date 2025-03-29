import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 📌 Load the preprocessed features and labels
X_train = np.load("processed_data/X_train.npy")
X_test = np.load("processed_data/X_test.npy")
y_train = np.load("processed_data/y_train.npy")
y_test = np.load("processed_data/y_test.npy")

# Print dataset size
print(f"Training Samples: {X_train.shape[0]}, Features: {X_train.shape[1]}")
print(f"Testing Samples: {X_test.shape[0]}, Features: {X_test.shape[1]}")

# 📌 Train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 📌 Make predictions
y_pred = model.predict(X_test)

# 📌 Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")

# 📌 Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 📌 Save the trained model
joblib.dump(model, "trained_model.pkl")
print("✅ Model saved as 'trained_model.pkl'")
