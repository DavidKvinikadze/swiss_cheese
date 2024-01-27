import subprocess

def sanitize_input(input_string):
    # Only allow alphanumeric characters and underscores in the filename
    return ''.join(c for c in input_string if c.isalnum() or c == '_')

filename = input("Please provide a file name to search and display:\n")

# Sanitize the input
filename = sanitize_input(filename)

# Construct the command using subprocess
command = ["cat", filename]
# Use subprocess to run the command
try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError:
    print("Error: File not found or unable to read the file.")
