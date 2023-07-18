from tabulate import tabulate

# contacts_old = list()

# contacts = ['Mary', 'Ann', '1234567', 'Some City, 1, Some Str.']
contacts = [
        ['Mary', 'Ann', '1234567', 'Some City, 1, Some Str.'],
        ['John', 'Doe', '1112345', 'Other City, 11, Other Str.'],
        ['John', 'Dick', '3213215', 'Other City, 1, Other Str.'],
    ]
# for contact in contacts:
#     print(contact)
    
# print(contacts[0:2])

def full_name(first_name, last_name):
    return " ".join([first_name, last_name])

# print(full_name(contacts[0:2][0], contacts[0:2][1]))

# print(len(contacts[0]))

TITLE = 'Your Phonebook'

def hello():
    print(f"Hi! It's me, {TITLE}")
    return input("What You wanna do? [a(dd)|l(ist)|f(ind)|r(emove)|q(uit))]: ")

def bey():
    print(f"Thank You for using {TITLE}")
    exit(0)

def element_exists(lst, el):
    try:
        lst.index(el)
        return True
    except ValueError:
        return False

def check_element(lst, element):
    for item in lst:
        if element_exists(item, element):
            print(f"Errer: item {element} alreade exists")
            return False
        else:
            return True

def short_list(contacts):
    y = []
    
    for (i, contact) in enumerate(contacts):
        x = []
        x.extend(contact[0:2])
        x.extend(contact[2:3])
        y.append([str(i), full_name(x[0], x[1]), x[2]])
    return y

def add_contact():
    contact = []
    
    number = input('Enter Phone Number = ')
    if check_element(contacts, number):
        contact.append(number)
    else:
        return
    
    first_name = input('Enter First Name = ')
    last_name = input('Enter Last Name = ')
    
    if check_element(short_list(contacts), full_name(first_name, last_name)):
        contact.insert(0, first_name)
        contact.insert(1, last_name)
    else:
        return
    
    address = input('Enter Address = ')
    contact.append(address)
    
    contacts.append(contact)
    
    print(f"{full_name(first_name, last_name)} added with {number}")
    contact_list(short_list(contacts))
    
    
def lookup_element(lst, el):
    result = []
    for contact in lst:
        if element_exists(contact, el):
            result.append(contact)
            
    if result:
        return (True, result)
    else:
        return (False, result)

def show_contact(result):
    columns = ['First Name', 'Last Name', 'Number', 'Address']
    print(tabulate(result, headers=columns, tablefmt="fancy_grid"))

def lookup_contact(el):
    state = False
    result = []
    
    state, result = lookup_element(contacts, el)
    
    if state:
        show_contact(result)
    else:
        print(f"Error: {el} not exists in phonebook")
    

def remove_contact(index):
    if contacts[index]:
        contacts.pop(index)
    else:
        print(f"Error: element with {index} noe exists")

def contact_list(contacts):
    # print(contacts)
    columns = ['#', 'Full Name', 'Number']
    print(tabulate(contacts, headers=columns, tablefmt="fancy_grid"))

match hello():
    case 'a'| 'add':
        add_contact()
    case 'f' | 'find':
        el = input("What You're looking for? :")
        lookup_contact(el)
    case 'l' | 'list':
        contact_list(short_list(contacts))
    case 'r' | 'remove' | 'delete':
        index = int(input("What contact You wanna remove? :"))
        remove_contact(index)
        contact_list(short_list(contacts))
    case 'q' | 'quit' | 'exit':
        bey()
    case _:
        print("Command not recognized")