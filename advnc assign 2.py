#!/usr/bin/env python
# coding: utf-8

# Q1. What is the relationship between classes and modules?
# 
# ANSWER:

# The relationship between classes and modules is as follows:-
# 
# A class is used to define a blueprint for a given object, whereas a module is used to reuse a given piece of code inside another program.
# 
# A class can have its own instance, but a module cannot be instantiated. We use the ‘class’ keyword to define a class, whereas to use modules, we use the ‘import’ keyword.
# 
# We can inherit a particular class and modify it using inheritance. But while using modules, it is simply a code containing variables, functions, and classes.
# 
# Modules are files present inside a package, whereas a class is used to encapsulate data and functions together inside the same unit.

# Q2. How do you make instances and classes?
# 
# ANSWER:

# Creating instances -
# 
# To create instances of a class, you call the class using class name and pass in whatever arguments its __ init __ method accepts.
# 
# For Example:

# In[ ]:


This would create first object of Employee class

emp1 = Employee("Zara", 2000) 


# Here, emp1 is the instance of the Employee class with attributes 'Zara' and '2000'
# 
# Creating Classes -
# 
# To create classes, the keyword 'class' is used immediately followed by the name of the class.
# 
# For Example:

# In[6]:


class Employee:
    def __init__(self, name ,salary):
        self.name = name
        self.salary = salary


# Q3. Where and how should be class attributes created?
# 
# ANSWER:

# Class Attributes are unique to each class. Each instance of the class will have this attribute. It’s sometimes used to specify a defualt value that all objects should have after they’ve been instantiated.
# 
# Here, our class attribute is species.
# 
# For example:

# In[7]:


class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Q4. Where and how are instance attributes created?
# 
# ANSWER:

# This __ init __ is called the initializer. It is automatically called when we instantiate the class. It’s job is to make sure the class has any attributes it needs. It’s sometimes also used to make sure that the object is in a valid state when it’s instantiated, like making sure the user didn’t enter a negative age for the dog.
# 
# We have to include the self parameter so that our initializer has a reference to the new object being instantiated.

# Q5. What does the term "self" in a Python class mean?
# 
# ANSWER:

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# 
# For Example:

# In[10]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)
    def myfunc1(xyz):    
        print("I am ", xyz.age, "years old")

p1 = Person("Tina", 36)
p1.myfunc()
p1.myfunc1()


# Q6. How does a Python class handle operator overloading?
# 
# ANSWER:

# Python Classes handle operator overloading by using special methods called Magic methods. these special methods usually begin and end with __ (double underscore).
# 
# Magic methods for basic arithmetic operators are:
# 
# __ add __()
# 
# __ sub __()
# 
# __ mul __()
# 
# __ div __()

# Q7. When do you consider allowing operator overloading of your classes?
# 
# ANSWER:

# When we want to have different meaning for the same operator accroding to the context we use operator overloading.

# Q8. What is the most popular form of operator overloading?
# 
# ANSWER:

# The operator overloading in Python means provide extended meaning beyond their predefined operational meaning. Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists. We can achieve this as the "+" operator is overloaded by the "int" class and "str" class. The user can notice that the same inbuilt operator or function is showing different behaviour for objects of different classes. This process is known as operator overloading.
# 
# Suppose the user has two objects which are the physical representation of a user-defined data type class. The user has to add two objects using the "+" operator, and it gives an error. This is because the compiler does not know how to add two objects. So, the user has to define the function for using the operator, and that process is known as "operator overloading". The user can overload all the existing operators but they cannot create any new operator. Python provides some special functions, or we can say magic functions for performing operator overloading, which is automatically invoked when it is associated with that operator. Such as, when the user uses the "+" operator, the magic function __ add __ will automatically invoke in the command where the "+" operator will be defined.
# 
# For Example:

# In[15]:


class example:  
    def __init__(self, X):  
        self.X = X  
   
    # adding two objects  
    def __add__(self, U):  
        return self.X + U.X  
    
object_1 = example(int(input("Please enter the value:  "))) 
object_2 = example(int(input("Please enter the value:  ")))  

print ("Sum : ", object_1 + object_2)

object_3 = example(str(input("Please enter the value:  "))) 
object_4 = example(str(input("Please enter the value:  "))) 

print ("String Concatenation : ", object_3 + object_4) 


# Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code?
# 
# ANSWER:

# The two most important concepts to grasp in order to comprehend Python OOP code are:
# 
# -Classes
# 
# -Objects
# 
# Along with the above mentioned concepts, the following concepts are also important to grasp in Python OOP:
# 
# -Polymorphism
# 
# -Encapsulation
# 
# -Inheritance
# 
# -Data Abstraction

# In[ ]:




