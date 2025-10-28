import os
import numpy as np
import scipy.io

# -----------------------------
# 1. Specify the file path
# -----------------------------
file_path = r'C:\Users\nipun\OneDrive\Desktop\LetsMasterPython\15_scientific_python\mat_data.mat'

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file does not exist: {file_path}")

# -----------------------------
# 2. Load the file based on extension
# -----------------------------
ext = os.path.splitext(file_path)[1].lower()

if ext == '.mat':
    # Load MATLAB file
    mat_data = scipy.io.loadmat(file_path)
    # Assume the variable we want is named 'mat_array'
    if 'mat_array' in mat_data:
        mat_array = mat_data['mat_array']
    else:
        # If unsure, print all variables in the file
        print("Variables in .mat file:", [k for k in mat_data.keys() if not k.startswith('__')])
        raise KeyError("Variable 'mat_array' not found in the MATLAB file.")
elif ext == '.txt':
    # Load plain text file as NumPy array
    mat_array = np.loadtxt(file_path)
else:
    raise ValueError("Unsupported file type. Use .mat or .txt files.")

# -----------------------------
# 3. Print the loaded array
# -----------------------------
print("Loaded array:\n", mat_array)
print("Shape:", mat_array.shape)
print("Type:", type(mat_array))
