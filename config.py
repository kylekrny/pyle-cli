import json
import os


questions = [
    {
        "name": "language",
        "prompt": "What programming language would you like to use?",
        "options": [{"text": "Javascript", "value": ".jsx"}, {"text": "Javascript", "value": ".tsx"}],
     },
    { 
        "name": "import",
        "prompt": "Would you like to use React 17+? (17+ does not require you to import react in each file)",
        "options": [{"text": "Yes", "value": True}, {"text": "No", "value": False}]
     },
    {
        "name": "component",
        "prompt": "What React component style do you like?",
        "options": [
            {"text": "Arrow Functional Components", "value": "arrow"}, 
            {"text": "Functional Components", "value": "functional"}, 
            {"text": "Class Components", "value": "class"},             
                    ]
     },
    { 
        "name": "test",
        "prompt": "Would you like to setup a .test file which each organism file?",
        "options": [{"text": "Yes", "value": True}, {"text": "No", "value": False}]
     },

    ]

def display_question(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option["text"]}")
        
    choice = int(input("Enter the number of your choice: "))

    if 1 <=choice <= len(options):
            return options[choice - 1]["value"]
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