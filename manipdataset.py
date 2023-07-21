import os
import shutil

def preprocess_datasets(directory, target_count=300):
    for root, dirs, files in os.walk(directory):
        num_files = len(files)
        
        # Skip empty folders
        if num_files == 0:
            continue
        
        print(f"Processing folder: {root}")
        print(f"Current number of files: {num_files}")
        
        if num_files > target_count:
            # Delete excess files
            files_to_delete = files[target_count:]
            for file_name in files_to_delete:
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
            print(f"Deleted {num_files - target_count} files.")
            
        elif num_files < target_count:
            # Duplicate existing files if target count is not yet met
            num_files_before_duplication = num_files
            counter = 0
            while num_files < target_count:
                for file_name in files[:num_files_before_duplication]:
                    src_file_path = os.path.join(root, file_name)
                    dst_file_name = f"{counter:03d}.csv"
                    dst_file_path = os.path.join(root, dst_file_name)
                    if src_file_path != dst_file_path:
                        shutil.copy(src_file_path, dst_file_path)
                        counter += 1
                        num_files += 1
                        if num_files >= target_count:
                            break
                if num_files_before_duplication == num_files:
                    break
            print(f"Duplicated {target_count - num_files_before_duplication} files.")
        
        print(f"Final number of files: {target_count}")
        print("---")

# Preprocess Crystal System dataset
crystal_system_dir = "CNN Datasets/Crystal System"
preprocess_datasets(crystal_system_dir)

# # Preprocess Material dataset
# material_dir = "CNN Datasets/Material"
# preprocess_datasets(material_dir)

# # Preprocess Space Group dataset
# space_group_dir = "CNN Datasets/Space Group"
# preprocess_datasets(space_group_dir)

# # Preprocess Sub Material dataset
# sub_material_dir = "CNN Datasets/Sub Material"
# preprocess_datasets(sub_material_dir)
