import os

# Get current working directory
current_dir = os.getcwd()

print(current_dir)

# User prompt to enter file name
filename = input("Enter file name: ")

# function to concatenate current directory with the file name
path = os.path.join(current_dir, filename)

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if isExist:
    print(f'File {filename} exists in directory {current_dir}')
else:
    print(f'No such file {filename} found in directory {current_dir}')

