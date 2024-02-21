#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# 
# Why are functions advantageous to have in your programs?
# 
# Solution:-
# 
# Functions are reusable pieces of programs.
# 
# Functions allow us to give a name to a block of statements, allowing us to run that block using the specified function name anywhere in our application and any number of times.
# 
# Primary benefits are:
# 
# Reusability : A function can be used again and again.
# Simplicity : Functions are easy to use and make code readable. We only need to know the purpose of a function and when to use it without focusing on inner working.

# In[1]:


# define a function

def cubeofNumber(x):
    return x**3

print(f"Cube of 2 is : {cubeofNumber(2)}")
print(f"Cube of 4 is : {cubeofNumber(4)}") # calling same function again


# ### Question 2
# 
# When does the code in a function run: when it's specified or when it's called?
# 
# Solution:-

# In[2]:


# specify a function

'''
we use `def <function-name>():`
to specify a function.
'''

def sqrofNumber(x):
    """
    returns square of number
    """
    return x**2


# In above cell we have defined our function. The code inside the function will not get executed unless we call the function with specified parameters.
# 
# Calling a function,

# In[3]:


sqrofNumber(44)


# ### Question 3
# 
# What statement creates a function?
# 
# Solution:-
# 
# A Function can be defined using the def keyword in the following format:
# 
# def function_name(parameters):
#     """
#     define a set of operations
#     """
# The function name is what we use to identify the function.
# The parameters of a function are the inputs for that function. These inputs can be used within the functions for computations. Parameters are optional.
# The body contains the set of operations.

# In[4]:


# function without use of parameters
def greet():            # define a function using def keyword
    print("hello")      # print hello

greet()                 # calling a function


# In[6]:


# function with use of parameters
def addTwoValues(a, b):
    return a+b

addTwoValues(2, -10)


# ### Question 4
# 
# What is the difference between a function and a function call?
# 
# Solution:-
# 
# A function is a set of instructions. We can define a function but the instructions won't be executed until we call the function and tell compiler to execute the instruction of the defined function.

# ### Question 5
# 
# How many global scopes are there in a Python program? Home many local scopes?
# 
# Solution:-
# 
# A variable scope determines where our variables can be accessed within the program and what values are stored inside of those variables.
# 
# There are 4 types of scope,
# 
# Local
# Enclosing
# Global
# Built-in
# 
# Local : variables that are defined inside of a function.
# 
# Enclosing : variables in local scope of enclosed function.
# 
# Global : variables are defined at top level of a program or defined using GLOBAL keyword.
# 
# Built-in : keywords, functions that are built in Python.
# 
# LEGB is the order in which a variable is assigned, the iterpretor checks variable first in local scope, then enclosing scope, then global scope and then in built-in scope.

# In[7]:


# global scope
x = "_global_x_"

def test():
    y = "_local_y_" # local to test function
    print(x)
    print(y)

test()
# print(y)    # Throws an error


# ### Question 6
# 
# What happens to variables in a local scope when the function call returns?
# 
# Solution:-
# 
# When the execution of the function returns, the local variables in the function scope are destroyed.
# 
# Even the parameters of the function are local to the scope of the function.

# ### Question 7
# 
# What is the concept of a return value? Is it possible to have a return value in an expression?
# 
# Solution:-
# 
# The return statement is used to return values from the function. Any remaining lines of code block after the return statement are not executed.

# In[9]:


def add_values(a, b):
    sum = a + b
    return sum  # explicit return statement

add_values(2, 11) 


# We can also return an expression as return value

# In[10]:


def add_values(a, b):
    return a + b  # an expression is evaluated first and then value is returned

add_values(2, 11)


# ### Question 8
# 
# If a function does not have a return statement, what is the return value of a call to that function?
# 
# Solution:-
# 
# We will check it using code

# In[11]:


def add_values(a, b):
    sum = a + b

print(add_values(2, 11))
print(type(add_values(2, 11)))


# As we can see if there is no explicit return statement, the function return None.

# ### Question 9
# 
# How do you make a function variable refer to the global variable?
# 
# Solution:-
# 
# We use global keyword before a variable to tell interpreter inside a function that we are using a global variable.
# 
# We use this keyword if we have to modify the global variable inside a function.

# In[12]:


# global variable
total_marks = 100

def test():
    global total_marks
    if total_marks>34:
        total_marks = 35

print(f'Total marks : {total_marks}')

# call function
test()

print(f'Total marks : {total_marks}')


# ### Question 10
# 
# What is the data type of None?
# 
# Solution:-

# In[13]:


help(None)


# In[14]:


type(None)


# In[ ]:


NoneType

None keyword is an object of data type NoneType.

Think it as of, we have a NoneType class and it has only one object that is None and None can be assigned to any object.


# ### Question 11
# 
# What does the sentence import areallyourpetsnamederic do?
# 
# Solution:-
# 
# This statement imports a module areallyourpetsnamederic, but as we see below there is no module named areallyourpetsnamederic in Python.

# In[15]:


import areallyourpetsnamederic

NOTE: If your import is failing due to a missing package, you can
manually install dependencies using either !pip or !apt.

To view examples of installing some common dependencies, click the
"Open Examples" button below.
# ### Question 12
# 
# If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 
# Solution:-
# 
# Any function in spam module can be called using format,
# 
# spam.<function-name>()
# 
# Therefore, bacon feature can be called using,
# 
# spam.bacon()

# ### Question 13
# 
# What can you do to save a programme from crashing if it encounters an error?
# 
# Solution:-
# 
# We can use try statement to test a code block and if it encounters an error an except block handles the error which avoids crashing a program.

# In[16]:


# without using try/except

def division(a, b):
    print(a/b)
    
division(10, 0)


# The above program is crashed!!!

# In[17]:


# Using try/except

def division(a, b):
    try:
        print(a/b)
    except Exception as e:
        print(Exception, e)

division(10, 0)


# ### Question 14
# 
# What is the purpose of the try clause? What is the purpose of the except clause?
# 
# Solution:-
# 
# As from the above example, the code block that can cause an error is handled with try/except clause without crashing of program.
# 
# If try block does not execute successfully the program will run except block.
