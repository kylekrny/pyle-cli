import argparse
import string
from file import create_file

def create_parser():
    parser = argparse.ArgumentParser(description="Pyle - React.js files generated with Python")
    parser.add_argument("-a", "--atom", metavar="atoms", help="Creates an file in the atom directory")
    parser.add_argument("-m", "--molecule", metavar="", help="Creates an file in the molecule directory")
    parser.add_argument("-o", "--organism", metavar="", help="Creates an file in the organism directory")
    parser.add_argument("-t", "--template", metavar="", help="Creates an file in the template directory")
    
    return parser


def parse_string(user_input):
    verify_string = any(char in string.punctuation or char.isdigit() for char in user_input)
    if not verify_string:
        capitalize_string = user_input.title()
        camel_case = capitalize_string.replace(" ", "")
        return camel_case
    else:
        print("Filenames with special characters or numbers are not permitted.")


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.atom:
        create_file("atoms", args.atom)
    elif args.molecule:
        create_file("molecules", args.atom)
    elif args.organism:
        create_file("organisms", args.atom)
    elif args.template:
        create_file("templates", args.atom)

# create_file("test")


if __name__ == "__main__":
    main()
