import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser(description="Pyle - React.js files generated with Python")
    parser.add_argument("-a", "--atom", metavar="", help="Creates an file in the atom directory")
    parser.add_argument("-m", "--molecule", metavar="", help="Creates an file in the molecule directory")
    parser.add_argument("-o", "--organism", metavar="", help="Creates an file in the organism directory")
    parser.add_argument("-t", "--template", metavar="", help="Creates an file in the template directory")
    parser.add_argument("-p", "--page", metavar="", help="Creates an file in the page directory")
    return parser

def create_file(fileName):
    fileString= f"{fileName}.tsx"
    with open(fileString, "x") as file:
        file.write("const hello= 'hello';")


def display_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
        
    choice = int(input("Enter the number of your choice: "))

    if 1 <=choice <= len(options):
        return options[choice - 1]
    else:
        print("Invalid choice please try again.")
        return display_question()    


def config_menu():
    question = "What programming language would you like to use?"
    options = ["Javascript", "Typescript"]

    return display_question(question, options)


selected_option = config_menu()
print(f"You selected: {selected_option}")

# create_file("test")