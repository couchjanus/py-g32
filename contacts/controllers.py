from .helpers import in_dict, full_name
import contacts.models as m

def add_contact():
    contact = {}
    contacts = m.get_contacts()
    number = input('Enter Phone Number = ').strip()
    if in_dict('Phonenumber', number, contacts):
        print(f"The contact {number} is already in the phonebook")
        return f"Error number"
    
    first_name = input('Enter First Name = ').strip()
    last_name = input('Enter Last Name = ').strip()
    
    if in_dict('First name', first_name, contacts) and in_dict('Last name', last_name, contacts):
        print(f"The contact {full_name(first_name, last_name)} is already in the phonebook")
        return f"Error name"
    
    address = input('Enter Address = ').strip()
    
    contact = {
        'First name': first_name.title(),
        'Last name': last_name.title(),
        'Phonenumber': number,
        'Address': address
        }
    m.set_contact(contact)
    return f"Contact added syccessfully"

def all_contacts():
    return m.get_contacts()

def lookup_contact(target):
    contacts = m.get_contacts()
    founded_contacts = []
    for key in list(contacts[0].keys())[0:4]:
        for index, contact in enumerate(contacts):
            if contact[key] == target:
                founded_contacts.append(contact)
    return founded_contacts

def remove_contact(index):
    if index in range(len(m.get_contacts())):
        confirm = input("Are You sure You wish delete this contact? (y|n): ")
        if confirm.lower() in ('yes', 'y'):
            m.get_contacts().pop(index)
            return f"element with {index} deleted successfully"
        else:
            return f"element with {index} not deleted"
    else:
        return f"Error: element with {index} noe exists"

def sort_contacts(order):
    match order:
        case 1:
            return sorted(m.get_contacts(), key=lambda x: x['First name'])
                    
        case 2:
            return sorted(m.get_contacts(), key=lambda x: x['Last name'])

        case _:
            return m.get_contacts()


def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    
    print("The value of __name__ is:", repr(__name__))
    
if __name__ == '__main__':
    main()
