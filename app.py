"""_summary_ documentation
"""
def add (x, y):
    return x + y

def div(x, y, o):
    match o:
        case '/':
            return a / b
        case '//':
            return a // b
        case '%':
            return a % b


a = int(input("Enter a = "))
b = int(input("Enter b = "))
o = input("Enter operation = ")



if o == '+':
    print('a + b = ', a + b)
elif o == '-':
    print('a - b = ', a - b)
elif o == '/' or o == '//' or o == '%':
    print('a ' + o +' b = ', div(a, b, o)) if b != 0 else print("Can't divide by zero!")
else:
    print('Operation not recognized!')
