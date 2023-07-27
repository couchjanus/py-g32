"""contacts/helpers.py
"""
import sys 

def full_name(first_name, last_name):
    """full_name"""
    return " ".join([first_name, last_name])

def hello(TITLE, prompt='a(dd)|l(ist)|f(ind)|r(emove)|q(uit))'):
    """hello"""
    print(f"Hi! It's me, {TITLE}")
    return input(f"What You wanna do? [{prompt}]: ")

def bye(TITLE):
    """bye"""
    print(f"Thank You for using {TITLE}")
    sys.exit(0)


def in_dict(key, value, dictlist):
    """is_dict"""
    for item in dictlist:
        if item[key].lower() == value:
            return True
    return False


def main():
    first_name = 'Hello'
    last_name = 'World'
    assert first_name.isalpha() and last_name.isalpha(), f"{first_name} and {last_name} is alpha expected, got: {full_name(first_name, last_name)}" 
    
if __name__ == '__main__':
    main()
