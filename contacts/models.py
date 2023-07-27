import pickle
import os.path
from contacts import DATABASE



def read_file():
    data = []
    if os.path.isfile(DATABASE):
        with open(DATABASE, 'rb') as f:
            data = pickle.load(f)
    return data

def get_contacts():
    data = read_file()
    if data is None:
        data = []
    return data

def save_contacts(records):
    if os.path.isfile(DATABASE):
        with open(DATABASE, 'wb') as f:
            pickle.dump(records, f)

# def set_contact(contact):
#     data.append(contact)
    
def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    
    print("The value of __name__ is:", repr(__name__))
    
if __name__ == '__main__':
    main()
