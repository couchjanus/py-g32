numbers = [1,2,3,4,5,6,7]

iter_numb = iter(numbers)

# print(iter_numb)

# print(dir(iter_numb))

# print(iter_numb.__next__())
# print(iter_numb.__next__())
# print(iter_numb.__next__())
# print(iter_numb.__next__())
# print(iter_numb.__next__())
# print(iter_numb.__next__())
# print(iter_numb.__next__())
# print(iter_numb.__next__())

a, b, c, d, e, f, _ = numbers
print(a, b, c, d, e)

# iter(666)

# print(reversed(numbers))

print([item for item in numbers])

print([x for x in range(0, 19, 2)])

print([x**2 for x in range(10)])

print([x for x in numbers if x%2 == 0])

prices = [1.0, 33, -5, 77, -3, 0.1]

print([i if i > 0 else 0 for i in prices])

print([x if (x > 2 and x % 2 == 0) else '!' for x in range(100)])

print([x + y for x in [1,2,3] if x > 2 for y in [3,4,5]])
print([x + y for x in [1,2,3] for y in [3,4,5] if x > 2])

print([(x, y) for x,y in [(1,2), (3,4), (5,6)]])


# print({x:chr(65 + x) for x in range(2000)})

d1 = {'w':1, 'x': 3}
d2 = {'y':1, 'x': 1, 'z':5}

od = {k: v for d in [d1, d2] for k, v in d.items()}
print(od)

matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)


print([n for row in matrix for n in row])

def fac(n):
    return 1 if n <= 1 else n * fac(n -1)

print(fac(44))

def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(n) for n in range(20)])

