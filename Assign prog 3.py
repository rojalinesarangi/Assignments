#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# 
# Write a Python Program to check if a number is positive, negative or zero?
# 
# *Solution*:-

# In[1]:


def checkNumber(num):
    if num<0:
        return "Negative"
    elif num>0:
        return "Positive"
    
    return "Zero"


# In[3]:


num = float(input("Enter Number : \t"))
print(f"Input Number {num} is {checkNumber(num)}")


# ### Question 2
# 
# Write a Python Program to check if a number is Odd or Even?
# 
# *Solution*:-

# In[14]:


def checkEvenOdd(num):
    return 'Odd' if num%2 else 'Even'


# In[5]:


num = float(input("Enter Number : \t"))
print(f"Input Number {num} is {checkEvenOdd(num)}")


# Question 3
# 
# Write a Python Program to check leap year?
# 
# *Solution*:-

# This question depends on corner use cases,
# 
# 1996, 2000 is a leap year. 1900, 1800 are not leap year.

# In[6]:


def checkLeapYear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))


# In[7]:


year = int(input("Enter year : \t"))
isleapyear = 'yes' if checkLeapYear(year) else 'no'

print(f"Is input year {year} a leap year : {isleapyear}")


# Question 4
# 
# Write a Python program to check Prime Number?
# 
# *Solution*:-
# 
# A number that is divisible only by itself and 1 that means a prime number has only 2 factors 1 and itself.

# In[8]:


def isPrime(num):
    if num>1:
        for i in range(2, int(num**(1/2)) + 1):
            if num%i==0:
                return False
        return True
    else:
        return False


# In[10]:


num = int(input("Enter a whole number : \t"))
isprimeno = 'yes' if isPrime(num) else 'no'

print(f"Is input num {num} a prime number : {isprimeno}")


# In[11]:


num = int(input("Enter a whole number : \t"))
isprimeno = 'yes' if isPrime(num) else 'no'

print(f"Is input num {num} a prime number : {isprimeno}")


# ### Question 5
# 
# Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
# 
# *Solution*:- 
# 
# We will use above function to check if number is prime number or not.

# In[15]:


for i in range(1, 10001):
    if isPrime(i):
        print(i, end=" ")

