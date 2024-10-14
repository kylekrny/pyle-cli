import json
from pathlib import Path

yes_no_options = [{"text": "Yes", "value": True}, {"text": "No", "value": False}]

questions = [
    {
        "name": "language",
        "prompt": "What programming language would you like to use?",
        "options": [{"text": "Javascript (jsx)", "value": "jsx"}, {"text": "Typescript (tsx)", "value": "tsx"}]
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
        "options": yes_no_options,
     },

    ]

def display_question(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        option_text = option["text"]
        print(f"{i}. {option_text}")
        
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


def check_for_directories():
    directories = ["atoms", "molecules", "organisms", "templates"]
    directories_to_create = []
    for directory in directories:
        path = Path(f'src/{directory}')
        if not path.exists():
            directories_to_create.append(directory)
    return directories_to_create

def create_starting_directories(directories):
    for directory in directories:
            Path(f"src/{directory}").mkdir(parents=True)
    print("Folder structure setup.")

def handle_config_error(): 
    error_res = display_question("Config error - start configurator?", yes_no_options)
    if (error_res):
        return config_menu()
    else:
        raise ValueError("Unable to create file due to config error - please run config")

def get_config():
    config_file = Path('config.json')
    
    if config_file.exists():
        with open('config.json', 'r') as file:
            data = json.load(file)
            return data
    else:
        return handle_config_error()    

def config_menu():
    config_data = {}

    for question in questions:
        config_data[question["name"]] = display_question(question["prompt"], question["options"])
    
    save_config_to_json(config_data)
    directories = check_for_directories()
    if directories:
        create_starting_directories(directories)
    
    return config_data


if __name__ == "__main__":
    config_menu()    

