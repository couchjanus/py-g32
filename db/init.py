import os.path
import pickle

DATABASE = 'contacts.db'
records = [
    {'id': 0, 'First name':'Mary', 'Last name':'Ann', 'Phonenumber':'1234567', 'Address':'Some City, 1, Some Str.'},
    {'id': 1, 'First name':'John', 'Last name':'Doe', 'Phonenumber':'1111111', 'Address':'Some City, 11, Some Str.'},
    {'id': 2, 'First name':'John', 'Last name':'Dick', 'Phonenumber':'2222222', 'Address':'Some City, 111, Some Str.'},
]

def save_contacts(records):
    if os.path.isfile(DATABASE):
        with open(DATABASE, 'wb') as f:
            pickle.dump(records, f)

save_contacts(records)