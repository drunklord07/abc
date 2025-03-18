import json
import re

# Function to find mobile numbers (10 digits or 91 followed by 10 digits)
def find_mobile_numbers(text):
    # Regular expression for matching 10-digit numbers or 91 followed by 10 digits
    mobile_pattern = r'\b(91\d{10}|\d{10})\b'
    return re.findall(mobile_pattern, text)

# Function to read the JSON file and parse it
def parse_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Ensure UTF-8 encoding
        data = json.load(file)
    return data

# Function to recursively search through JSON data and print mobile numbers
def search_json_for_mobile_numbers(data):
    def recursive_search(data):
        if isinstance(data, dict):
            for key, value in data.items():
                recursive_search(value)
        elif isinstance(data, list):
            for item in data:
                recursive_search(item)
        elif isinstance(data, str):
            mobile_numbers = find_mobile_numbers(data)
            if mobile_numbers:
                for number in mobile_numbers:
                    # Print mobile number in red using ANSI escape codes
                    try:
                        print(f"\033[91mFound mobile number: {number}\033[0m")
                    except UnicodeEncodeError:
                        print(f"Found mobile number: {number}")  # Fallback if color printing fails
        
    recursive_search(data)

# Main function
def main():
    file_path = 'sample.json'  # Change this to the path of your JSON file
    try:
        data = parse_json(file_path)
        search_json_for_mobile_numbers(data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
