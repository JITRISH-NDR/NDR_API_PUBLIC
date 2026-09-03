import os
# Ask the user for the file name
filename = input("Enter the name of the Python file (with or without .py extension): ").strip()
# Add .py extension if not provided
if not filename.endswith('.py'):
    filename += '.py'
# Check if file exists in the current directory
if os.path.isfile(filename):
    print(f"Running {filename}...\n")
    %run $filename
else:
    print(f"File '{filename}' not found in the current directory.")
