import os
import pandas as pd

def get_unique_ids(user_list_file, folder_path, id_column, user_column):
    # Step 1: Read the in-scope user list into a set
    inscope_users = set(pd.read_csv(user_list_file)[user_column])
    
    unique_ids = set()
    
    # Step 2: Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.csv'):  # Assuming CSV files
            # Step 3: Read each file and filter records
            df = pd.read_csv(file_path)
            filtered = df[df[user_column].isin(inscope_users)]
            unique_ids.update(filtered[id_column])
    
    return unique_ids

# Example usage:
user_list_file = "path_to_user_list.csv"  # File containing in-scope user list
folder_path = "path_to_folder_with_files"  # Folder containing files to scan
id_column = "ID"  # Column with unique IDs
user_column = "User"  # Column with user names or IDs

unique_ids = get_unique_ids(user_list_file, folder_path, id_column, user_column)

# Output results
print(f"Unique IDs: {unique_ids}")