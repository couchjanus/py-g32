print(lambda s: s[::-1])

print(callable(lambda s: s[::-1]))
print(callable([1,2]))

reverse = lambda s: s[::-1]

print(reverse("Hello world"))

print((lambda s: s[::-1])("Hello world"))

print((lambda x1, x2, x3: (x1 + x2 + x3)/3)(3, 4, 5))

get_numb = lambda: 5555
print(get_numb()) 

print((lambda x: (x, x**2, x**5))(4))
print((lambda x: [x, x**2, x**5])(4))
print((lambda x: {1:x, 2:x**2, 5:x**5})(4))


def inner():
    print('Inner function')
    
def outer(fn):
    fn()
    
outer(inner)


my_list = ['ca', 't', 'abs', 'pink']

print(sorted(my_list))

print(sorted(my_list, key=len))
print(sorted(my_list, key=len, reverse=True))

def rev_len(s):
    return -len(s)

print(sorted(my_list, key=rev_len))
l = [2,1,5,2,9]
l.sort()
print(l)

def fn_o():
    def fn_i():
        print('Inner fn')
    return fn_i

fn = fn_o()

# print(fn)
fn()
fn_o()()

numb = [2, 5, -1, 1, -7, -8]

positive = filter(lambda n: n > 0, numb)
print(positive)
print(list(positive))

numbers = [1, 3, 10, 33, 45, 7, 66]

def my_even(numbers):
    even_numb = []
    for n in numbers:
        if n % 2 == 0:
            even_numb.append(n)
    return even_numb

print(my_even(numbers))

print(list(filter(lambda x: x % 2 == 0, numbers)))


# print(list(map(lambda s: s[::-1], ['cat', 'dog', 3.14159, 'gecko'])))


# розрахувати ціну після оподаткування:

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = map(get_price_with_tax, txns)
print(list(final_prices))

alphabet = 'abcdefghijklmnoprstuvwxyz'

rotate = 3

def rotate_chr(c, reverse=False):
    c = c.lower()
    if c not in alphabet:
        return c
    
    rot_pos = ord(c) - rotate if reverse else ord(c) + rotate
    
    if rot_pos <= ord(alphabet[-1]):
        return chr(rot_pos)
    
    return chr(rot_pos - len(alphabet))

print("".join(map(rotate_chr, 'Hello, secret message goes here.')))
print("".join(map(lambda c: rotate_chr(c, True), 'khoor, vhfuhw phvvdjh jrhv khuh.')))


print(sum([1,2,3,4,5]))

from functools import reduce

print(reduce(lambda x, y: x + y, [1,2,3,4,5]))

def factorial(n):
    return reduce(lambda x, y: x *y, range(1, n + 1))

print(factorial(4))

numbers = [1,2,3,4,5]

print(list(map(str, numbers)))

def custom_map(fn, iterable):
    return reduce(lambda items, value: items + [fn(value)], iterable, [])

print(list(custom_map(float, numbers)))


a = [10,20,30,40]
b = ['a', 'b', 'c', 'd']

for i in zip(a, b):
    print(i, type(i))


my_dict = {1: 'a', 2: 'b', 3: 'c'}

print(dict(zip(my_dict.values(), my_dict)))
print(dict(zip(my_dict.values(), my_dict.keys())))