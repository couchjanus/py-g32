"""contacts/cli.py"""
from tabulate import tabulate
from .helpers import hello, bye

from contacts import TITLE

import contacts.controllers as c

def contact_list(contacts):
    print(tabulate(contacts, headers='keys', tablefmt="fancy_grid"))


def app():
    """interactive"""
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

def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    print(F"The variable __name__ tells me which context this file is running in.")
    print("The value of __name__ is:", repr(__name__))
    # app()
    
if __name__ == '__main__':
    main()
    
