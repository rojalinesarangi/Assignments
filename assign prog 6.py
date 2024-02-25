#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# 
# Write a Python Program to Display Fibonacci Sequence Using Recursion?
# 
# *Solution*:-

# In[4]:


def fibonacci_series(n):
    if n<=1:
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2) 

n = int(input("Enter a whole number\t"))

if n<1:
    print("Invalid Input")
elif n==1:
    print(0)
else:
    print("Your fibonacci Sequence")
    for i in range(n):
        print(fibonacci_series(i))


# ### Question 2
# 
# Write a Python Program to Find Factorial of Number Using Recursion?
# 
# *Solution*:-

# In[6]:


def factorial(n):
    if n==1:
        return 1
    
    return n*factorial(n-1)

n = int(input("Enter a whole number\t"))
print(f"Factorial of {n} = {factorial(n)}")


# ### Question 3
# 
# Write a Python Program to calculate your Body Mass Index?
# 
# *Solution*:-

# In[8]:


def bmi(weight, height):
    return weight/(height**2)

weight = float(input("Enter weight in kgs\t"))
height = float(input("Enter height in meters\t"))

print(f"BMI Score is {bmi(weight, height)}")


# ### Question 4
# 
# Write a Python Program to calculate the natural logarithm of any number?
# 
# *Solution*:-
#     
# Natural logarithm : (Base e)

# In[9]:


import math

print(f"Natural logarithm of 16 is : {math.log(16)}")


# ### Question 5
# 
# Write a Python Program for cube sum of first n natural numbers?
# 
# *Solution*:-

# In[10]:


cube = lambda x : x**3

n = int(input("Enter your range."))
for i in range(1, n+1):
    print(f"Cube of {i} : {cube(i)}")


# In[ ]:




