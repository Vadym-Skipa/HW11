from functools import wraps
import logging


# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    def inner(*args, **kwargs):
        return 2 * func(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


# print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


# print(add(5, 5))  # 20


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    def inner(*args):
        if all(a % 2 for a in args):
            return func(*args)
        else:
            return "Please use only odd numbers!"

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


# print(add(5, 5))  # 10
# print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


# print(multiply(1, 2, 3, 4, 5))
# print(multiply(1, 3, 5, 7, 9))

# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):
logging.basicConfig(level=logging.INFO)

def to_str(arg):
    if isinstance(arg, str):
        return "\"" + arg + "\""
    else:
        return str(arg)

def logged(func):
    # log function arguments and its return value
    # @wraps(func)
    def inner(*args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        str_args = ''
        if args:
            str_args += " ,".join(to_str(arg) for arg in args)
        if kwargs:
            str_kwargs = " ,".join(to_str(key) + "=" + to_str(value) for key, value in kwargs.items())
            if str_args:
                str_args += ", "
            str_args += str_kwargs
        logging.info(f"you called {func.__name__}({str_args})")
        result = func(*args, **kwargs)
        logging.info(f"it returned {result}")
        return result

    return inner


@logged
def func1(*args, **kwargs):
    return 3 + len(args)


# print(func1(4, 4, 4, a=3, error="   "))
# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    # put code here
    def decorator(func):
        def inner(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                print(f"Wrong type: {type(arg).__name__}")

        return inner

    return decorator


@type_check(int)
def times2(num):
    return num * 2


# print(times2(2))
# times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]

# print(first_letter('Hello World'))
# first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
