import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser(description="Pyle - React.js files generated with Python")
    parser.add_argument("-a", "--atom", metavar="atoms", help="Creates an file in the atom directory")
    parser.add_argument("-m", "--molecule", metavar="", help="Creates an file in the molecule directory")
    parser.add_argument("-o", "--organism", metavar="", help="Creates an file in the organism directory")
    parser.add_argument("-t", "--template", metavar="", help="Creates an file in the template directory")
    
    return parser


def create_file(directory, fileName,ext):
    file_string= f"src/{directory}/{fileName.capitalize()}.{ext}"
    try:
        with open(file_string, "x") as file:
            file.write("const hello= 'hello';")
    except:
        print (f"{fileName} already exists in {directory} directory")


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.atom:
        create_file("atoms", args.atom, "tsx")
    elif args.molecule:
        create_file("molecules", args.atom, "tsx")
    elif args.organism:
        create_file("organisms", args.atom, "tsx")
    elif args.template:
        create_file("templates", args.atom, "tsx")

# create_file("test")


if __name__ == "__main__":
    main()