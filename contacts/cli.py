"""contacts/cli.py"""
from tabulate import tabulate
import argparse

from .helpers import hello, bye

from contacts import TITLE, DATABASE_PATH, DATABASE

import contacts.controllers as c

import os
from pathlib import Path

def contact_list(contacts):
    print(tabulate(contacts, headers='keys', tablefmt="fancy_grid"))

def check_db():
    cwd = Path.cwd()
    path = os.path.join(cwd, DATABASE_PATH)
    database_dir = Path(DATABASE_PATH)
    
    if not database_dir.is_dir():
        try:
            os.mkdir(path)
        except OSError as err:
            raise SystemError(1)
    
    if not Path(DATABASE).exists():
        Path.touch(DATABASE)
    return True
    

def ui(recursive=False):
    match hello(TITLE):
        case 'a'| 'add':
            print(c.add_contact())

        case 'f' | 'find':
            el = input("What You're looking for? :").strip().title()
            found = c.lookup_contact(el)
            if found:
                contact_list(found)
            else:
                print(f"Sorry, nothibg found for {el}")
        case 'l' | 'list':
            contact_list(c.all_contacts())
            
            order = int(input("Enter order by name = 1 or oder by surname = 2: "))
            
            contact_list(c.sort_contacts(order))
        
        case 'r' | 'remove' | 'delete':
            
            index = int(input("What contact You wanna remove? :"))
            print(c.remove_contact(index))
            contact_list(c.all_contacts())

        case 'q' | 'quit' | 'exit':
            bye(TITLE)
            
        case _:
            print("Command not recognized")
    if recursive:
        ui(recursive)

def app(prog_name):
    """interactive"""
    parser = argparse.ArgumentParser(
        prog=prog_name,
        description='The contacts list of phonebook',
        epilog='Thanks for using %(prog)s! :)'
    )
    
    recursively = parser.add_argument_group('running recursively')
    
    recursively.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="run Your program recursively"
    )
    
    args = parser.parse_args()
    
    if check_db():
        ui(recursive=args.recursive)
    

def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    print(F"The variable __name__ tells me which context this file is running in.")
    print("The value of __name__ is:", repr(__name__))
    # app()
    
if __name__ == '__main__':
    main()
    
