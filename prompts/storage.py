import json
import os

#Define the path to the JSON file
FILE_PATH = 'prompts.json'

def load_data():
    """Loads data from de JSON file.
    If it doesn't exist, it creates an empty one.
    """
    if not os.path.exists(FILE_PATH):
        # Create an empty list
        save_data([])
        return []
    
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # If the file is corrupted or not found, return an empty list
        return []
    
def save_data(data):
    """Saves the given data to the JSON file.
    The prompt should be a list of prompt dictionaries.
    """
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        # Use indent=4 for pretty printing in the JSON
        json.dump(data, f, indent=4)
        
    