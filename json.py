import json

# Step 2: Open the JSON file
with open('data.json', 'r') as file:
    # Step 3: Load the JSON data
    data = json.load(file)

# Step 4: Process the data (example: print it)
print(data)

# If you need to modify the data and write it back to the file
data['new_key'] = 'new_value'

# Step 5: Open the JSON file in write mode
with open('data.json', 'w') as file:
    # Step 6: Write the modified data back to the file
    json.dump(data, file, indent=4)