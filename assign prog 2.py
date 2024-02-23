#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# 
# Write a Python program to convert kilometers to miles?
# 
# *Solution*:-

# In[1]:


# user input (kilometers)
kms = float(input("Enter kilometers value\t"))

# formula
miles = kms * 0.62137

print(f"{kms}Kms is equivalent to {miles:.3f} miles")


# ### Question 2
# 
# Write a Python program to convert Celsius to Fahrenheit?
# 
# *Solution*:-

# In[3]:


# user input (celsius)
c = float(input("Enter Celcius degrees\t"))

# formula
f = c * (9/5) + 32

print(f"{c}C is equivalent to {f:.3f}F")


# ### Question 3
# 
# Write a Python program to display calendar?
# 
# *Solution*:-

# In[10]:


# using built-in module
import calendar

# display month
year = 2021
month = 12

print(calendar.month(year,month))


# In[14]:


#display full year

year=2024

print(calendar.calendar(year))


# ### Question 4
# 
# Write a Python program to solve quadratic equation?
# 
# *Solution*:-

# The main aim is to find the roots of the equation which is, $$ax^2 + bx +c$$
# where, a, b, and c are coefficient and real numbers and also $a\ne0$ 
# 
# Using the Shridharacharya formula we find the roots of the equation.

# In[30]:


# user input two variables
a = int(input("Input first number, (0 not allowed)\t"))    
b = int(input("Input second number\t"))
c = int(input("Input third number\t"))

# calculate discriminant
dis = (b**2) - (4*a*c)

# finding 2 roots

import cmath

root1 = (-b + cmath.sqrt(dis))/(2*a)
root2 = (-b - cmath.sqrt(dis))/(2*a)

print(f"Roots of equation {a}x^2 + {b}x + {c} are,\n{root1}\n{root2}")


# ### Question 5
# 
# Write a Python program to swap two variables without temp variable?
# 
# *Solution*:-

# In[31]:


# user input two variables
a = int(input("Input first number\t"))
b = int(input("Input second number\t"))
print("--------------------")
print(f"Value of a = {a}, value of b = {b}")

# using tuple swap
a, b = b, a

print(f"After Swapped Operation\nValue of a = {a}, value of b = {b}")


# In[32]:


# user input two variables
a = int(input("Input first number\t"))
b = int(input("Input second number\t"))
print("--------------------")
print(f"Value of a = {a}, value of b = {b}")

# using arthematic operation
a = a+b
b = a-b
a = a-b

print(f"After Swapped Operation\nValue of a = {a}, value of b = {b}")


# In[ ]:




