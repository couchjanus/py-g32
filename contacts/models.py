
data = [
    {'id': 0, 'First name':'Mary', 'Last name':'Ann', 'Phonenumber':'1234567', 'Address':'Some City, 1, Some Str.'},
    {'id': 1, 'First name':'John', 'Last name':'Doe', 'Phonenumber':'1111111', 'Address':'Some City, 11, Some Str.'},
    {'id': 2, 'First name':'John', 'Last name':'Dick', 'Phonenumber':'2222222', 'Address':'Some City, 111, Some Str.'},
]

def get_contacts():
    return data

def set_contact(contact):
    data.append(contact)
    
def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    
    print("The value of __name__ is:", repr(__name__))
    
if __name__ == '__main__':
    main()
