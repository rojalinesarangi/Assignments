#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# 
# Write a Python Program to Find the Factorial of a Number?
# 
# *Solution*

# In[1]:


def factorialofNumber(num):
    return 1 if (num==1 or num==0) else num * factorialofNumber(num-1)


# In[3]:


num = int(input("Enter Number : \t"))
print(f"Factorial of Input Number {num} is {factorialofNumber(num)}")


# Question 2
# 
# Write a Python Program to Display the multiplication Table?
# 
# *Solution*:-

# In[5]:


def multiplicationTable(num):
    for i in range(1, 11):
        print(f"{num}x{i}={num*i}")


# In[6]:


num = int(input("Enter Number : \t"))
multiplicationTable(num)


# Question 3
# 
# Write a Python Program to Print the Fibonacci sequence?
# 
# *Solution*

# In[7]:


def printFibonacciSeq(n):
    a = 0
    b = 1

    if n<1:
        print("Enter positive Number")
    elif n==1:
        print("Fibonacci Sequence : ")
        print(a)
    else:
        print("Fibonacci Sequence : ")
        for i in range(n):
            print(a)
            c = a+b
            a = b
            b = c


# In[8]:


printFibonacciSeq(10)


# Question 4
# 
# Write a Python Program to Check Armstrong Number?
# 
# *Solution*
# 
# Example of armstrong Number,

# In[9]:


153 == 1*1*1 + 5*5*5 + 3*3*3


# In[10]:


import math
def order(num):
    return int(math.log10(num))+1

def isArmstrong(num):
    n = order(num)
    s = 0
    temp = num

    while temp!=0:
        r = temp%10
        s += r**n
        temp = temp//10

    return s==num


# In[11]:


isArmstrong(153)


# Question 5
# 
# Write a Python Program to Find Armstrong Number in an Interval?
# 
# *Solution*

# In[12]:


lower_bound = 100
upper_bound = 1000


# In[13]:


for r in range(lower_bound, upper_bound+1):
    if isArmstrong(r):
        print(f"Number {r} is Armstrong Number")


# Question 6
# 
# Write a Python Program to Find the Sum of Natural Numbers?
# 
# *Solution*:-
# 
# Given a number n find sum of first n natural numbers.
# 
# n = 6
# 6+5+4+3+2+1 = 21

# In[14]:


def findSum(n) :
    return (n / 2) * (n + 1) if (n % 2 == 0) else ((n + 1) / 2) * n


# In[15]:


findSum(6)


# In[16]:


findSum(8)


# In[ ]:




