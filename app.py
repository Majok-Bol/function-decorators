from functools import wraps
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




# # Build your first decorator manually
# def greet():
#     print("Hello,learner")

# def my_decorator(fn):
#     def wrapper():
#         print("Before the function runs.")
#         fn()
#         print("After the function runs")
#     return wrapper

# greet=my_decorator(greet)
# greet()



# # Python gives us a shorter way to write the same thing.
# # Instead of writing:
# # def greet():
# #     print("Hello, learner!")
# # greet = my_decorator(greet)


# # You can write:
# @my_decorator
# def greet():
#     print("Hello,Learner")



#other example
# def my_name():
#     print("My name is Mary Hill")
# def name_decorator(fn):
#     def name_wrapper():
#         print("I would like to introduce myself")
#         fn()
#         print("Iam done with my introduction")
#     return name_wrapper
# introduction=name_decorator(my_name)
# introduction()

#decorator
def name_decorator(fn):
    def name_wrapper():
        print("I would like to introduce myself")
        fn()
        print("Iam done with my introduction")
    return name_wrapper
@name_decorator
def my_name():
    print("My name is Mary Jane")
my_name()


#another example
# def city():
#     print("Nairobi")
# def city_decorator(name):
#     def city_wrapper():
#         print("Welcome to Suncity")
#         city()
#         print("Enjoy your holiday")
#     return city_wrapper
# city_name=city_decorator(city)
# city_name()

#decorator
def city_decorator(city):
    def city_wrapper():
        print("Welcome to Suncity")
        city()
        print("Enjoy your holiday")
    return city_wrapper
@city_decorator
def city_name():
    print("Nebraska")
city_name()



#position arguments
# *args allows a function to accept any number of positional arguments.
# Python collects the arguments into a tuple.
def greet(*args):
    print(args)
    for name in args:
        print(f"Hello, {name}")
   
greet("Mary","Jane","Hill",'Jone')

#keyword arguments
# Python collects the keyword arguments into a dictionary.
def introduce(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}:{value}")

introduce(name="Napoleon",age=25,city="Memphis")



# def code(*args):
#     # print(args)
#     for lang in args:
#         print(lang)

    # print("I would like to learn programming")
# def code_decorator(fn):
#     def code_wrapper(*language):
#         print("--Programming languages--")
#         fn(*language)
#         print("Happy coding!\n")
#     return code_wrapper
# code_lang=code_decorator(code)
# code_lang("C","Python")
# code_lang("C#","Golang")
# code_lang("Perl","Pascal")
# code_lang("Rust","Java")
# code_lang("JavaScript","C++","Fotran")



#decorator
def code_decorator(fn):
    # @wraps(fn) copies important metadata from fn to wrapper, including the original function's name, documentation string, and annotations.
    #  It also sets __wrapped__ to reference the original function.
    @wraps(fn)
    def code_wrapper(*language):
        print("--Iam learning:--")
        fn(*language)
        print("Wishing you the best!\n")
    return code_wrapper
@code_decorator
def learning(*args):
    for lang in args:
        print(lang)
learning("HTML","JSON")
learning("C#","Java","API testing","Networking")


#before using @wraps(fn)
# print(learning.__name__) #code_wrapper
# print(learning.__doc__) #None

#after using @wraps(fn)
print("Function name: ",learning.__name__) #
print("Documentation: ",learning.__doc__) #