#!/usr/bin/env python
# coding: utf-8

# ### 1. What is the concept of an abstract superclass? 
# 
# ANSWER:

#  In Python, abstraction can be achieved by using abstract classes and interfaces.
# 
# A class that consists of one or more abstract method is called the abstract class. Abstract methods do not contain their implementation. Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass. Abstraction classes are meant to be the blueprint of the other class. An abstract class can be useful when we are designing large functions. An abstract class is also helpful to provide the standard interface for different implementations of components. Python provides the abc module to use the abstraction in the Python program. Let's see the following syntax.
# 
# Syntax
# 
# from abc import ABC                                                                                                             
# class ClassName(ABC):

# In[1]:


from abc import ABC, abstractmethod
class Animal(ABC):
 
    def move(self):
        pass
 
class Human(Animal):
 
    def move(self):
        print("I can walk and run")
 
class Snake(Animal):
 
    def move(self):
        print("I can crawl")
 
class Dog(Animal):
 
    def move(self):
        print("I can bark")
 
class Lion(Animal):
 
    def move(self):
        print("I can roar")
         
# Driver code
R = Human()
R.move()
 
K = Snake()
K.move()
 
R = Dog()
R.move()
 
K = Lion()
K.move()


# ### 2. What happens when a class statement's top level contains a basic assignment statement?
# 
# ANSWER:

# When a Class statement's top level contains a basic assignment statement, its usually treated as a class attribute or class level variable.
# 
# Whereas assignment statements inside methods are treated as instance attributes or local attributes.
# 
# When an instance of a class is created a single copy of class attributes is maintained and shared to all instances of class. whereas each instance object maintains its own copy of instance variables.

# In[2]:


class Person:
    species = 'Homesapiens' # class attribute
    def __init__(self,name,gender):
        self.name = name # instance attributes
        self.gender = gender


# ### 3. Why does a class need to manually call a superclass's __ init __ method?
# 
# ANSWER:

# If a child class has $__init__$ method, then it will not inherit the $__init__$ method of the parent class. In other words the $__init__$ method of the child class overrides the $__init__$ method of the parent class. So we have to manually call a parent superclass's $__init__$ using super() method.
# 
# For Example:

# In[4]:


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age       
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
emp_1 = Employee('XYZ',28,20000)
print(emp_1.__dict__)


# ### 4. How can you augment, instead of completely replacing, an inherited method?
# 
# ANSWER:

# super() method can be used to augment, instead of completely replacing, an inherited method.
# 
# For Example:

# In[5]:


class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
class Employee(Person):
    def __init__(self,name,gender,salary):
        super().__init__(name,gender) 
        self.salary = salary
emp_1 = Employee('XYZ ABC','Female',10000)
print(emp_1.__dict__)   


# ### 5. How is the local scope of a class different from that of a function?
# 
# ANSWER:

# Local scope of a class is a variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# 
# For Example:
# 
# A variable created inside a function is available inside that function:

# In[7]:


def myfunc():
  x = 300
  print(x)

myfunc()


# Whereas for a function of a class, as explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
# 
# For Example: 
# 
# The local variable can be accessed from a function within the function:

# In[8]:


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# In[ ]:




