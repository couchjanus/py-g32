def fn1(n):
    num, nums = 0, [] 
    while num < n:
        nums.append(num)
        num += 1
    return nums

# sum_f1 = sum(fn1(10000000))

# print(sum_f1)

def fn2(n):
    num = 0 
    while num < n:
        yield num
        num += 1


# sum_f2 = sum(fn2(10000000))

# print(sum_f2)


def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b
fib_list = []   
# for n in fib():
#     fib_list.append(n)
#     if n > 200: break
    
# print(fib_list)

def file_reader(file):
    f = open(file)
    res = f.read().split('\n')
    return res

def file_yield(file):
    for row in open(file):
        yield row
        
# my_gen = file_yield("some_csv.csv")
# row_count = 0

# for row in my_gen:
#     row_count += 1
    
# print(row_count)

def infinite_seq():
    n = 0
    while True:
        yield n
        n += 1
        
for i in infinite_seq():
    print(i, end=" ")

