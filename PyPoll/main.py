# Import Modules
import os
import csv

# Import CSV
csvPath = os.path.join('Resources', 'election_data.csv')

# Read CSV
with open(csvPath) as data:

    # Parse CSV
    reader = csv.reader(data, delimiter=",")

    # Skip header
    next(reader, None)
