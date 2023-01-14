import csv
import os
import pandas as pd

# Initializing empty lists
data = []   # A list to store the final data
l = []      # A list to store the file paths of each part
engine_data = []
module_data = []

# Looping through all directories and sub-directories, recording the file paths for .cfg files in a list
input = "YOURPATH"
path = os.path.join(input, "targetdirectory")
type = '.cfg'
output = 'OUTPUTPATH.csv'

for path, subdirs, files in os.walk(input):
    for name in files:
        if name.endswith(type):
            l.append(os.path.join(path, name))

# Function to parse engine name and mass data from a cfg file
def part_data(config):

    engine_found = False
    # Initialize an temporary list to store the data
    i = {}
    # Open the CFG file
    # Open the .cfg file and read its contents
    with open(config, 'r') as cfg_file:
        cfg_text = cfg_file.read()

    # Split the text into lines
    lines = cfg_text.split('\n')
    # Iterate over the lines in the CFG file
    for line in lines:
        # Check if the '=' character is in the line
        if '=' in line:
            # Split the line into key and value using the first '=' character as the separator
            key, value = line.strip().split('=', 1)

            # Check if the part is an Engine
            if 'Engine' in value:
                engine_found = True

            # Only parse the data that we need
            if engine_found and key.startswith('title'):
                # Add the value to the list
                i['Title'] = value

            if engine_found and key.startswith('mass'):
                # Add the value to the list
                i['Mass'] = value

    # Add the data to the main list
    engine_data.append(i)

# Function to parse thrust and specific impulse data from a cfg file
def read_module(config):
    with open(config, 'r') as cfg_file:
        cfg_text = cfg_file.read()

    # Split the text into lines
    lines = cfg_text.split('\n')
    module = ''
    data_list = ''

    module_found = False
    module_end = False

    for line in lines:
        if line.__contains__('name = ModuleEngines'):
            module_found = True
            module_end = False
            data_list = ''
        if module_found:
            data_list += ''.join(["', '", line])
        if line.__contains__('atmosphereCurve'):
            module_end = True
        if module_end and line.__contains__('}') or line.__contains__('key = 1'):
            module_found = False
            module = module + data_list
            data_list = ''

    i = {}

    lines = module.split(',')

    for line in lines:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            if key.__contains__('minThrust'):
                # Add the value to the list
                i['Min Thrust'] = value

            if key.__contains__('maxThrust'):
                # Add the value to the list
                i['Max Thrust'] = value

            if key.__contains__('key'):
                # Check if the 'key' key already exists in the dictionary
                if 'Key' in i:
                    # If it does, append the value to the list of values
                    i['Key'].append(value)
                else:
                    # If it doesn't, create a new list with the value
                    i['Key'] = [value]
    module_data.append(i)

# Save the data to a csv file
def to_csv(config):
    # Write the list of dictionaries to a CSV file
    with open(output, 'w', newline='') as f:
        # Create a dictionary writer with the fieldnames as the keys in the dictionaries
        fieldnames = ['Title', 'Mass', 'Min Thrust', 'Max Thrust', 'Key']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write each row of data
        for row in config:
            writer.writerow(row)

# Loop through all the files in the l list
for file in l:
    part_data(file)
    read_module(file)


data = [{**x, **y} for x, y in zip(engine_data, module_data)]
to_csv(data)

# Reformat the csv file to be usable
df = pd.read_csv(output)
df[['path','Title']] = df.Title.str.split('=',expand=True)
df['Min Thrust'] = df['Min Thrust'].str.replace("'", "")
df['Max Thrust'] = df['Max Thrust'].str.replace("'", "")
df['Key'] = df['Key'].str.replace('"', "")
df['Key'] = df['Key'].str.replace("'", "")
df.drop(df.columns[[5]], axis=1, inplace=True)

# Export to csv, with the index removed
df.to_csv(output, index=False)