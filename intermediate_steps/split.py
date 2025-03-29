import numpy as np
from sklearn.model_selection import train_test_split

# Load features and labels
X = np.load("features.npy")  # Feature matrix
y = np.load("labels.npy")  # Labels

# Split data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save split data
np.save("X_train.npy", X_train)
np.save("X_test.npy", X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)

print("✅ Data split into training and testing sets!")
