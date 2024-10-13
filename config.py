import json
import os


questions = [
    {
        "name": "language",
        "prompt": "What programming language would you like to use?",
        "options": ["Javascript", "Typescript"]
     },
    { 
        "name": "import",
        "prompt": "Would you like to use React 17+? (17+ does not require you to import react in each file)",
        "options": ["Yes", "No"]
     },
    {
        "name": "component",
        "prompt": "What React component style do you like?",
        "options": ["Arrow Functional Components", "Functional Components", "Class Components"]
     },
    { 
        "name": "test",
        "prompt": "Would you like to setup a .test file which each organism file?",
        "options": ["Yes", "No"]
     },

    ]

def display_question(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
        
    choice = int(input("Enter the number of your choice: "))

    if 1 <=choice <= len(options):
        if options[choice - 1] == "Yes":
            return True
        elif options[choice - 1] == "No":
            return False
        else:
            return options[choice - 1]
    else:
        print("Invalid choice please try again.")
        return display_question()    

def save_config_to_json(config_data):
    filepath =  'config.json'
    
    with open(filepath, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)
    print(f"Configuration saved to {filepath}")

def config_menu():
    config_data = {}

    for question in questions:
        config_data[question["name"]] = display_question(question["prompt"], question["options"])
    
    save_config_to_json(config_data)

config_menu()