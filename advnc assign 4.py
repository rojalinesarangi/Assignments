#!/usr/bin/env python
# coding: utf-8

# Q1. Which two operator overloading methods can you use in your classes to support iteration?
# 
# ANSWER:

# The following are the two operator overloading methods that you can use in your classes to support iteration are:
# 
# 1)`__iter__` : The `__iter__` method will always return the iterator object itself. We can initialize variables in this method.
# 
# 2)`__next__` : The `__next__` method is created to return the next element from the iterator. To reach the end we must raise the     StopIteration error in this method.
# 
# For Example:

# In[2]:


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
 
 
for num in Counter(5, 15):
    print(num)


# Q2. In what contexts do the two operator overloading methods manage printing?
# 
# ANSWER:
#     
# The following are the two operator overloading methods that manage prinintg:
# 
# 1)`__str__` : The `__str__` method produces a user-friendly result. You can override the __str__ method and implement it according to your need. This method is used to obtain a textual representation of an object that the user can understand. The following method gets invoke when we pass the variable to the print() function or the str() function.
# 
# 2)`__repr__` : The `__repr__` method produces a developer-friendly result. You should not override the __repr__ method. This method is mainly used by developers while debugging. The following method invokes the output when we type the variable’s name or the object in the interactive python console.
# 
# So, the following methods `__str__` and `__repr__`  defines how the object is presented “textually”. These methods are implemented in the class that produces the objects.
# 
# For Example:

# In[4]:


# Example 1

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        myString = "Name: {} , Age: {}".format(self.name, self.age)
        return myString


student1 = Student("ABC XYZ", 23)
myStr = str(student1)
print("The string representation of student object is:")
print(myStr)


# In[5]:


# Example 2

import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))


# In[6]:


# Example 3

class Fruit:
    def __init__(self, name):
        self.name = name
banana = Fruit("Banana")
print(banana)


# In[7]:


class Fruit:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'I am a {self.name}'
    
    def __repr__(self):
        return f'Fruit("{self.name}")'
    
banana = Fruit("Banana")
print(banana)


# In[8]:


print(banana.__str__())


# In[9]:


print(banana.__repr__())


# Q3. In a class, how do you intercept slice operations?
# 
# ANSWER:
# 
# You can intercept slice operations using the `__getitem__` method. The `__getitem__` method is used for accessing list items, array elements, dictionary entries etc. slice() is a constructor in Python that creates slice object to represent set of indices that the range(start, stop, step) specifies. `__getitem__` method can be implement in a class, and the behavior of slicing can be defined inside it.
# 
# Syntax:

# `__getitem__`(slice(start, stop, step))

# Parameter:
#     
# slice() : constructor to create slice object.
# 
# start : An integer number specifying start index.It is optional and default is 0.
# 
# stop : An integer number specifying end index.
# 
# step : An integer number specifying the step of slicing. It is optional and default is 1.
# 
# For Example:

# In[11]:


# abcde is string can be 
# an array as well.

sliced ='abcde'.__getitem__(slice(0, 2, 1)) 
print(sliced)


# Q4. In a class, how do you capture in-place addition?
# 
# ANSWER:
#     
# **In-place operation** is an operation that changes directly the content of a given linear algebra, vector, matrices(Tensor) without making a copy. The operators which helps to do the operation is called in-place operator.
# 
# **Eg**: `a+= b` is equivalent to `a= operator.iadd(a, b)`.
# 
# To capture in-place addition, the `iadd()` in-place operator is used:
# 
# This function is used to assign the current value and add them. This operator does x+=y operation. In case of strings, numbers assigning is not performed.
# 
# For Example:

# In[12]:


import operator
a =operator.iadd(7, 3);
print ("The result after adding : ", end="")
print(a)


# Q5. When is it appropriate to use operator overloading?
# 
# ANSWER:
# 
# Operator overloading is used when we want to use an operator other than its normal operation to have different meaning according to the context required in user defined function.
# 
# For Example:

# In[14]:


class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages+other.pages
b1 = Book(100)
b2 = Book(200)
print(f'Total Number of Pages: {b1+b2}')


# In[ ]:




