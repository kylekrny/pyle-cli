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




create_file("test")