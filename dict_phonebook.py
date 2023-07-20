from tabulate import tabulate
from collections import OrderedDict

TITLE = 'Your Dict Phonebook'

def full_name(first_name, last_name):
    return " ".join([first_name, last_name])

def hello():
    print(f"Hi! It's me, {TITLE}")
    return input("What You wanna do? [a(dd)|l(ist)|f(ind)|r(emove)|q(uit))]: ")

def bye():
    print(f"Thank You for using {TITLE}")
    exit(0)

set1 = set()
{1,2,3}

data = {
    '0' : {'First name':'Mary', 'Last name':'Ann', 'Phonenumber':'1234567', 'Address':'Some City, 1, Some Str.'},
    '1' : {'First name':'John', 'Last name':'Doe', 'Phonenumber':'1111111', 'Address':'Some City, 11, Some Str.'},
    '2' : {'First name':'John', 'Last name':'Dick', 'Phonenumber':'2222222', 'Address':'Some City, 111, Some Str.'},
}

# for key in data:
#     print(key)

# for key in data.keys():
#     print(key)

# for val in data.values():
#     print(val)

# for key, val in data.items():
#     print(key, '=>', val)


# for id in data:
#     for key in data[id]:
#         print(f'{key} => {data[id][key]}')

contacts = []

for id in data:
    contact = {}
    for key in data[id]:
        contact['id'] = id
        contact[key] = data[id][key]
    contacts.append(contact)
# print(contacts)

def contact_list(contacts):
    print(tabulate(contacts, headers='keys', tablefmt="fancy_grid"))

# contact_list(contacts)

def in_dict(key, value, dictlist):
    for item in dictlist:
        if item[key].lower() == value:
            return True
    return False

def add_contact():
    number = input('Enter Phone Number = ').strip()
    if in_dict('Phonenumber', number, contacts):
        print(f"The contact {number} is already in the phonebook")
        return
    
    first_name = input('Enter First Name = ').strip()
    last_name = input('Enter Last Name = ').strip()
    
    if in_dict('First name', first_name, contacts) and in_dict('Last name', last_name, contacts):
        print(f"The contact {full_name(first_name, last_name)} is already in the phonebook")
        return
    
    address = input('Enter Address = ').strip()
    
    return {
        'First name': first_name.title(),
        'Last name': last_name.title(),
        'Phonenumber': number,
        'Address': address
        }
    
    
def lookup_element(lst, el):
    result = []
    # for contact in lst:
    #     if element_exists(contact, el):
    #         result.append(contact)
            
    # if result:
    #     return (True, result)
    # else:
    #     return (False, result)

def show_contact(result):
    columns = ['First Name', 'Last Name', 'Number', 'Address']
    print(tabulate(result, headers=columns, tablefmt="fancy_grid"))


# contacts[0].keys()

def lookup_contact(target):
    founded_contacts = []
    for key in list(contacts[0].keys())[0:4]:
        for index, contact in enumerate(contacts):
            if contact[key] == target:
                founded_contacts.append(contact)
    return founded_contacts

def remove_contact(index):
    if index in range(len(contacts)):
        confirm = input("Are You sure You wish delete this contact? (y|n): ")
        if confirm.lower() in ('yes', 'y'):
            contacts.pop(index)
        else:
            return
    else:
        print(f"Error: element with {index} noe exists")


match hello():
    case 'a'| 'add':
        contact = {}
        contact = add_contact()
        if contact:
            
            # print(contact)
            contact['id'] = str(len(contacts))
            contacts.append(contact)
            contact_list(contacts)
    case 'f' | 'find':
        el = input("What You're looking for? :").strip().title()
        if lookup_contact(el):
            contact_list(lookup_contact(el))
        else:
            print(f"Sorry, nothibg found for {el}")
    case 'l' | 'list':
        contact_list(contacts)
        
        order = int(input("Enter order by name = 1 or oder by surname = 2: "))
        match order:
            case 1:
                sortedbook = sorted(contacts, key=lambda x: x['First name'])
                contact_list(sortedbook)
            case 2:
                sortedbook = sorted(contacts, key=lambda x: x['Last name'])
                contact_list(sortedbook)
            case _:
                contact_list(contacts)
        # contact_list(short_list(contacts))
    case 'r' | 'remove' | 'delete':
        
        index = int(input("What contact You wanna remove? :"))
        remove_contact(index)
        contact_list(contacts)

    case 'q' | 'quit' | 'exit':
        bye()
    case _:
        print("Command not recognized")