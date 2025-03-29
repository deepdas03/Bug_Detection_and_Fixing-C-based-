# C Bug Detection and Fixing Model

## 📌 Overview
This project detects and fixes bugs in C programs using machine learning. It extracts features from buggy C code, trains an ML model to identify errors, and suggests potential fixes.

## 🔹 How This Project Works
1. **Feature Extraction**: Converts C code into numerical features using TF-IDF.
2. **Data Preprocessing**: Saves processed data into `.npy` format.
3. **Model Training**: Uses a RandomForestClassifier to learn patterns of buggy vs. fixed code.
4. **Bug Detection & Fixing**: The trained model suggests fixes for new buggy code inputs.

## 🔹 Where the Code is Tested
- The scripts are tested in **Python 3.10+**.
- The training and testing are performed in **VS Code** (Windows environment).
- The model predictions are verified using sample C programs.
