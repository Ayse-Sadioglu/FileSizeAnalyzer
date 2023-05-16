import os

def get_file_size(file_path):
    return os.path.getsize(file_path)

def get_directory_file_sizes(directory_path):
    file_sizes = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_sizes[file_path] = get_file_size(file_path)
    return file_sizes



directory_path = input("Enter the file path: ")
file_sizes = get_directory_file_sizes(directory_path)
for file_path, size in file_sizes.items():
    file_name = os.path.basename(file_path)
    # TODO: Implement converting mechanism bytes to Gb/Mb...
    print(f'{file_name}: {size} bytes')
