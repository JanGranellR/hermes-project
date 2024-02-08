import os
import shutil
import pandas as pd

def create_path(p: str = None) -> bool:
    """
    Create a directory path if it does not exist.

    Parameters:
    - p (str): The path to be created.

    Returns:
    - bool: True if the path is created or already exists, False otherwise.
    """

    # Check if the path is not specified
    if p == None:
        print("[INFO] No path specified")
        return False
    
    # Check if the path already exists
    if os.path.exists(p):
        print(f"[INFO] Path {p} already exists")
        return True
    
    try:
        # Create the directory path
        os.makedirs(p)
        print(f"[INFO] Path {p} created successfully")
        return True

    except Exception as e:
        # Handle potential errors during path creation
        print(f"[ERROR] Unable to create path {p}: {e}")
        return False

def delete_path(p: str = None, f: bool = False) -> bool:
    """
    Delete a directory path if it does exist.

    Parameters:
    - p (str): The path to be deleted.

    Returns:
    - bool: True if the path is deleted or does not already exist, False otherwise.
    """

    # Check if the path is not specified
    if p == None:
        print("[INFO] No path specified")
        return False
    
    # Check if the path does not exist
    if not os.path.exists(p):
        print(f"[INFO] Path {p} does not exist")
        return True
    
    try:
        # Check if the path is empty and if the user wants to force it
        if os.listdir(p) != 0 and f == False:
            raise Exception()

        shutil.rmtree(p)
        print(f"[INFO] Path {p} deleted successfully")

        return True
    except Exception as e:
        # Handle potential errors during path creation
        print(f"[ERROR] Unable to delete path {p}: {e}")
        return False

def import_data_as_pandas_dataframe(path: str = None, folder: str = None) -> pd.DataFrame:
    """
    Import data files located in a specified folder within a directory path and return as a Pandas DataFrame.

    Parameters:
    - path (str): Directory path containing subfolders with data files.
    - folder (str): Subfolder name within the directory path containing data files.

    Returns:
    - pd.DataFrame: DataFrame containing two columns: 'label' and 'feature'.
    """

    data = []  # Store data

    # Iterate through subfolders
    for d in os.listdir(path):

        # Iterate through files
        for f in os.listdir(os.path.join(path, d, folder)):

            # Exclude specific files
            if f == "response.txt" or f == "urls.txt":
                continue
            
            # Read content
            with open(os.path.join(path, d, folder, f), "r") as r:
                data.append([d, r.read()])

    # Create a DataFrame from the 'data' list
    return pd.DataFrame(data, columns = ["label", "feature"])


def print_matrix(results: dict[str, dict[str, int]], column_width: int = 10) -> None:
    """
    Print a matrix of results with given column width.

    Patameters:
    - results (dict[str, dict[str, int]]): A dictionary containing predicted results. It has labels as keys, and inner dictionaries as values, where inner dictionaries have labels as keys and corresponding counts as values.
    - column_width (int, optional): Width for each column in the matrix. Default is 10.
    """

    # Get all unique labels
    labels = list(results.keys())

    # Print table header
    print(" " * column_width, end=' ')

    for label in labels:
        print(f"{label:^{column_width}}", end=' ')
    
    print()

    # Print table rows
    for label in labels:
        print(f"{label:<{column_width}}", end=' ')
        
        for inner_label in labels:
            print(f"{results[label].get(inner_label, 0):^{column_width}}", end=' ')
        
        print()