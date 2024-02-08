import sys

sys.path.insert(0, 'config')
sys.path.insert(0, 'utils')

import os
import config
import shutil
from utils import create_path, delete_path

def separate_files() -> None:
    """
    Separates files into training and test sets for each class in the dataset.
    """

    # Delete the processed path to start fresh
    delete_path(os.path.join(config.dataset["path"], config.dataset["path_processed"]), True)

    # Dictionary to hold files categorized by class
    categories = {}

    for web in config.dataset["webs"]:
        if web["category"] not in categories.keys():
            categories[web["category"]] = []

        # Get all files excluding 'response.txt' and 'urls.txt'
        all_files = os.listdir(os.path.join(config.dataset["path"], config.dataset["path_cache"], web["category"], web["name"]))
        all_files = [file for file in all_files if not (file == "response.txt" or file == "urls.txt")]

        input_folder = os.path.join(config.dataset["path"], config.dataset["path_cache"], web["category"], web["name"])

        # Append file paths to respective category in the dictionary
        for file in all_files:
            categories[web["category"]].append(os.path.join(input_folder, file))

    for category in categories:
        # Create directories
        create_path(os.path.join(config.dataset["path"], config.dataset["path_processed"], category, config.dataset["path_train"]))
        create_path(os.path.join(config.dataset["path"], config.dataset["path_processed"], category, config.dataset["path_test"]))

        # Limit files
        all_files = categories[category]
        all_files = all_files[:config.dataset["limit"]]

        # Index based on split ratio
        split_index = int(len(all_files) * config.dataset["split_ratio"])
        
        # Split files
        files_train = all_files[:split_index]
        files_test = all_files[split_index:]

        # Generate folders paths
        output_folder_training = os.path.join(config.dataset["path"], config.dataset["path_processed"], category, config.dataset["path_train"])
        output_folder_test = os.path.join(config.dataset["path"], config.dataset["path_processed"], category, config.dataset["path_test"])

        # Copy files
        for file in files_train:
            if os.path.isfile(file):
                shutil.copy(file, output_folder_training)

        for file in files_test:
            if os.path.isfile(file):                
                shutil.copy(file, output_folder_test)

def main() -> None:
    """
    Main function that executes the program.
    """
    
    separate_files()

if __name__ == "__main__":
    main()
