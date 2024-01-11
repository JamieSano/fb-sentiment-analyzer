import json

# Specify the path to your downloaded Facebook data JSON file
json_file_path = 'C:/Users/Jamie Sano/deploy-fb/deploy-fb-proj/data/likes_and_reactions_1.json'

# Open the JSON file and load its content
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Assuming 'field_name' is a key in dictionaries within the list
key_to_find = 'field_name'
reactions_data = 'reaction'
# Iterate over the list and find the value associated with the key
for item in data:
    if key_to_find in item:
        field_value = item[key_to_find]
        reactions_value= item[reactions_data]
        num_reactions = len(reactions_value)
        print(f'The value for key "{key_to_find}" is: {field_value}')
        print(f'The total number of reactions is: {num_reactions}')
        break  # Stop iterating after the first occurrence
