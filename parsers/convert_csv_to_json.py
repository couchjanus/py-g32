# convert_csv_to_json.py
import csv
import json

# Function to convert a CSV to JSON Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    data = {} # create a dictionary
    with open(csvFilePath) as csvf: 
        # Open a csv reader called DictReader
        csvReader = csv.DictReader(csvf)
        # Convert each row into a dictionary and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to be the primary key
            key = rows['id']
            data[key] = rows
            
    # Open a json writer, and use the json.dumps()
    # function to dump data

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# Call the make_json function

make_json('blogger.csv', 'blogger.json')
