import csv
import numpy as np

def load_data(file_path):
    rows = []

    with open(file_path, mode="r", newline="") as file:
        reader = csv.reader(file)   # reader is a iterator. It reads each cell as a string
        next(reader)    # skip header

        for row in reader:
            rows.append([float(x) for x in row])        # Convert data to float
    
    return np.array(rows)
