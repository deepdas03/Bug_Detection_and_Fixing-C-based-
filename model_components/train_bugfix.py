import numpy as np
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load tokenized data
X_buggy = np.load("processed_data/X_buggy.npy")
y_fixed = np.load("processed_data/y_fixed.npy")

# Reshape for LSTM
X_buggy = X_buggy.reshape((X_buggy.shape[0], 1, X_buggy.shape[1]))
y_fixed = y_fixed.reshape((y_fixed.shape[0], y_fixed.shape[1]))

# Define LSTM model
model = Sequential([
    LSTM(128, return_sequences=True, input_shape=(1, X_buggy.shape[2])),
    LSTM(64, return_sequences=False),
    Dense(y_fixed.shape[1], activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_buggy, y_fixed, epochs=20, batch_size=16)

# Save model
model.save("bug_fix_model.h5")

print("✅ Bug fixing model trained & saved!")
