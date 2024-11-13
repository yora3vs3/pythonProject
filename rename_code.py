import os
import shutil

# Define the old and new file names
old_filename = 'queue.py'
new_filename = 'queue1.py'

# Check if the file exists and rename it
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"Renamed {old_filename} to {new_filename}")
else:
    print(f"{old_filename} does not exist")


# Function to clear __pycache__ directories
def clear_pycache():
    for root, dirs, files in os.walk("."):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.join(root, dir_name)
                print(f"Removing {dir_path}")
                shutil.rmtree(dir_path)


# Clear __pycache__ directories to avoid conflicts
clear_pycache()

# (Revised script to avoid circular import issue)

# Importing the required module correctly
from statistics import mean, median

# Your pre-defined data for two datasets
data1 = [1, 2, 3, 4, 5]
data2 = [5, 4, 3, 2, 1]

try:
    # Validation for non-empty lists
    if not data1 or not data2:
        raise ValueError("Datasets must not be empty.")

    # Validation for numerical values
    if not all(isinstance(i, (int, float)) for i in data1 + data2):
        raise TypeError("All elements in datasets must be numbers.")

    # Calculating means and medians
    mean1, mean2 = mean(data1), mean(data2)
    median1, median2 = median(data1), median(data2)

    # Using zip and all to compare means and medians
    comparison = zip([mean1, median1], [mean2, median2])
    are_stats_equal = all(x == y for x, y in comparison)

    print(f"Are the statistical measures equal for both datasets?: {are_stats_equal}")

except Exception as e:
    print(f"An error occurred: {e}")
