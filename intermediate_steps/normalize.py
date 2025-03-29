import os
import re

def normalize_variables(code):
    """Replaces variable names with generic names (VAR1, VAR2, etc.)."""
    keywords = {"int", "return", "if", "else", "for", "while", "char", "float", "double", "void"}
    
    # Find all variable-like words
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
    unique_tokens = list(set(tokens) - keywords)
    
    # Replace variable names with generic placeholders
    for i, token in enumerate(unique_tokens):
        code = re.sub(r'\b' + token + r'\b', f'VAR{i+1}', code)
    
    return code

# Process all .c files in the dataset folder
input_folder = "dataset"
output_folder = "dataset/normalized"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all .c files
for filename in os.listdir(input_folder):
    if filename.endswith(".c"):  # Process only C files
        with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
            code = f.read()

        # Normalize variable names
        normalized_code = normalize_variables(code)

        # Save the processed file
        output_file = os.path.join(output_folder, filename)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(normalized_code)

        print(f"✅ Processed: {filename} → Saved to {output_file}")
