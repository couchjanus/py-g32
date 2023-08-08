# decorators

def my_decorator(fn):
    def wrapper():
        f = fn()
        uppercase = f.upper()
        return uppercase
    return wrapper

def say_hi():
    return f"hello there"

decor = my_decorator(say_hi)
print(decor())
import sys

def decorator(fn):
    def wrapper(arg = None):
        if arg == None:
            print(f"""
                  You got am error, You are missing Name
                  Usage: main.py [OPTIONS] Name""")
            raise sys.exit("Missing argument Name")
        f = fn(arg)
        uppercase = f.upper()
        return uppercase
    return wrapper

@decorator
def say_hello(name):
    return f"hello there {name}"

print(say_hello('Decorator'))
# print(say_hello())


def lowercase(fn):
    def wrapper():
        f = fn()
        lowercase = f.lower()
        return lowercase
    return wrapper


def split_str(fn):
    def wrapper():
        f = fn()
        out = f.split()
        return out
    return wrapper

@split_str
@lowercase
def hello():
    return f"HELLO WORLD"

print(hello())


def annoce(language: str, version: float) -> str:
    return f"{language} {version} has been released"

print(annoce("Python", 3.11))

print(annoce.__annotations__)

def check_range(fn):
    def wrapper(*args, **kwargs):
        for name, range in fn.__annotations__.items():
            min_value, max_value = range
            if not(min_value <= kwargs[name] <= max_value):
                msg = 'argument {} is out of range [{} - {}]'
                raise ValueError(msg.format(name, min_value, max_value))
        return fn(*args, **kwargs)
    return wrapper
    
@check_range
def foo(a: (0, 8), b: (5, 9), c: (10, 20)):
    return a * b - c

print(foo(a=4, b=6, c=150))