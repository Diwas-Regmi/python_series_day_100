import time


# def decorator_func(func):
#     def wrapper_func():
#         func()
#
#     return wrapper_func
#
# def say_hello():
#     time.sleep(2)
#     print("hello")
#
# say_hello()

# you can do the same using decorators
def decorator_func(function):
    def wrapper_func():
        print(f"Waiting 2 seconds calling the {function}")
        time.sleep(2)
        function()
        print()

    return wrapper_func

@decorator_func
def say_hello():
    print("Hello")

def say_bye():
    print("bye")

@decorator_func
def say_greetings():
    print("Greetings!")

# or you can call decorators in this way also
def say_bad_words():
    print("Dumbass")

decorator_function = decorator_func(say_bad_words)
decorator_function()


say_hello()
say_bye()
say_greetings()
