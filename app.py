
# A function is a reusable block of code that performs a task
# def greet():
#     print("Hello world")

#call the function
# greet()
# greet()
# greet()
# greet()
# greet()


#functions can accept other values
# def hello(name):
#     print(f"Hello, {name}")


#call the function
# hello("Mary")
# hello("Jonny")
# hello("Napoleon")

# functions are objects in python
# my_function=hello
# my_function("Carnegie")


# passing a function into another function
# def say_hello():
#     print("Hello World")
# def execute_function(fn):
#     fn()
# execute_function(say_hello)
# def say_goodbye():
#     print("Goodbye")
# execute_function(say_goodbye)


# Python defines say_hello.
# Python defines execute_function, which accepts a parameter called fn.
# execute_function(say_hello) passes the function itself into execute_function.
# Inside execute_function, fn refers to say_hello.
# fn() calls say_hello, printing Hello!.


# In Python, you can pass a function into another function just like you pass a string or an integer.
# This is called a higher-order function when a function accepts another function or returns a function.


# functions inside other functions
# def outer():
#     print("This is the outer function")
#     def inner():
#         print("This is inner function")
#     inner()

# outer()
# 1. outer() runs.
# 2. Python prints the first message.
# 3. Python defines the inner() function.
# 4. The line inner() calls the inner function.
# 5. The inner function prints its message.
# Look closely at the indentation:

# Because inner is defined inside outer, it is a local function. You normally call it from within outer.
# Why is this useful for decorators? Because a decorator commonly defines an inner function that adds behavior around another function.


# return a function
# def add():
#     return 10
# result=add()
# print(result)


# def outer():
#     def inner():
#         print("Hello from inner")
#     return inner
    

# my_function=outer()
# my_function()

# Build your first decorator manually
def greet():
    print("Hello,learner")

def my_decorator(fn):
    def wrapper():
        print("Before the function runs.")
        fn()
        print("After the function runs")
    return wrapper

greet=my_decorator(greet)
greet()



# Python gives us a shorter way to write the same thing.
# Instead of writing:
# def greet():
#     print("Hello, learner!")
# greet = my_decorator(greet)


# You can write:
@my_decorator
def greet():
    print("Hello,Learner")