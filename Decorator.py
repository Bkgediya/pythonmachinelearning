def say_hello(name):
    return f'Hello {name}'


def greet_bob(greeter_func):
    return greeter_func("bob")

print(greet_bob(say_hello))

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Somethings is happening before the function is called")
        func()
        print("Somethings after the function is called")

    return wrapper

def say_whee():
    print("wheel")


say_whee = my_decorator(say_whee)
say_whee()


#decorators

@my_decorator # == say_whee = my_decorator(say_whee)
def say_whee():
    print("wheel")

print(say_whee.__name__)
say_whee()


#function with arguments

def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello + {name}")

greet("Hiii")


#value return from decorated functions

def do_twice_return(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_do_twice

@do_twice_return
def return_greeting(name):
    print("value is returned")
    return f"Hii {name}"

message = return_greeting("Kaizen")
print(message)


