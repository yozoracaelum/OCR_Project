import os
import shutil

# Set the input directory path
input_dir = "dataset"

# Set the number of duplications
num_duplications = 99

# Process each folder in the input directory
for folder_name in os.listdir(input_dir):
    folder_path = os.path.join(input_dir, folder_name)
    if os.path.isdir(folder_path):

        # Process each file in the folder
        file_list = [file for file in os.listdir(folder_path) if file.endswith(".jpeg")]
        total_files = len(file_list)
        processed_files = 0

        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)

            # Duplicate the file multiple times
            for i in range(num_duplications):
                output_file_name = f"{file_name.split('.')[0]}_{i+1}.jpeg"
                output_file_path = os.path.join(input_dir, folder_name, output_file_name)
                shutil.copy2(file_path, output_file_path)

            processed_files += 1
            progress = processed_files / total_files * 100
            print(f"Processing folder: {folder_name} [{progress:.2f}%]")

print("Processing completed.")
