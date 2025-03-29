import re

def preprocess_code(code):
    """Removes comments and extra spaces from C code."""
    # Remove single-line comments (// ...)
    code = re.sub(r'//.*?\n', '', code)
    # Remove multi-line comments (/* ... */)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # Remove extra whitespace
    code = re.sub(r'\s+', ' ', code).strip()
    return code

# Example usage
sample_code = """
/* This is a buggy function */
#include <stdio.h>
// Function to add two numbers
int add(int a, int b) { return a + b; }  // Missing return statement
"""
clean_code = preprocess_code(sample_code)
print(clean_code)
