# def hello():
#     return 'Hello world'
#
#
# def decorate(func):
#     def wrap():
#
#         print('I am a before decorator')
#         print(func())
#         print('I am after decorator')
#     # return f
#     return wrap
#
#
# hello = decorate(hello)()
# # print(hello())

#
# def hello():
#     return 'Hello world'


# def decorate(func):
#     def wrap():
#         print('I am a before decorator')
#         print(func())
#         print('I am after decorator')
#
#     return wrap
#
#
# @decorate
# def hello():
#     return 'Hello World'
#
#
# hello()


# def decorate(func):
#     def wrap(arg):
#         print('I am a before decorator')
#         print(func(arg))
#         print('I am after decorator')
#
#     return wrap
#
#
# @decorate
# def hello(name):
#     return f'Hello {name}'
#
#
# hello('Anu')


#
# def decorate(func):
#     def wrap(*arg):
#         print('I am a before decorator')
#         print(func(*arg))
#         print('I am after decorator')
#
#     return wrap
#
#
# @decorate
# def add(x, y):
#     return x + y
#
#
# add(2, 7)


# def decorate(func):
#     def wrap(*arg, **kwargs):
#         print('I am a before decorator')
#         print(func(*arg, **kwargs))
#         print('I am after decorator')
#
#     return wrap
#
#
# @decorate
# def add(x, y):
#     return x + y
#
#
# add(2, 7)


import functools
import time


# def decorate(func):
#     @functools.wraps(func)
#     def wrap(*arg, **kwargs):
#         print('I am a before decorator')
#         print(func(*arg, **kwargs))
#         print('I am after decorator')
#
#     return wrap
#
#
# @decorate
# def add(x, y):
#     return x + y
#
#
# add(2, 7)
#
# print(add.__name__)
# print(add.__doc__)


def decorate(func):
    @functools.wraps(func)
    def wrap(*arg, **kwargs):
        print('I am a before decorator')
        f = (func(*arg, **kwargs))
        print('I am after decorator')
        return f

    return wrap


def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f'The function {f.__name__} took {end - start} to run')
        return func

    return wrapper


@decorate
def hello(name):
    return f'Hello {name}'


@performance_counter
@decorate
def add(x, y):
    return x + y


print(hello('Anuoluwa'))
print(add(2, 7))

print(add.__name__)
print(add.__doc__)


def multiply(a, b):
    return a * b


multiply_by_5 = functools.partial(multiply, 5)
for number in range(6):

    print(multiply_by_5(number))
print()
