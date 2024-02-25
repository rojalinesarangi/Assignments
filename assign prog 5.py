#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# 
# Write a Python Program to find LCM?
# 
# *Solution*:-

# $ axb = LCM(a,b) x HCF(a,b) $

# In[5]:


def hcf(a,b):
    if b==0:
        return a
    return hcf(b, a%b)


# In[7]:


def lcm(a,b):
    return (a/hcf(a,b))*b


# In[8]:


a = 20
b = 15

lcm(a,b)


# ### Question 2
# 
# Write a Python Program to find HCF?
# 
# *Solution*:-

# In[10]:


def hcf(a,b):
    if b==0:
        return a
    return hcf(b, a%b)


# In[11]:


a = 20
b = 15

hcf(a,b)


# ### Question 3
# 
# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# 
# *Solution*:-

# In[12]:


# decimal to binary
def decimal_to_binary(dec):
    print(f"{dec} in Binary : {bin(dec)}")
  
# decimal to octal
def decimal_to_octal(dec):
    print(f"{dec} in Octal : {oct(dec)}")
  
# decimal to hexadecimal
def decimal_to_hexadecimal(dec):
    print(f"{dec} in Hexadecimal : {hex(dec)}")


# In[13]:


dec = 32
decimal_to_binary(dec)
decimal_to_octal(dec)
decimal_to_hexadecimal(dec)


# ### Question 4
# 
# Write a Python Program To Find ASCII value of a character?
# 
# *Solution*:-

# In[18]:


character = 'A'
ord(character)


# In[19]:


character = "|"
ord(character)


# ### Question 5
# 
# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# 
# *Solution*:-

# In[20]:


def calculator(v1, v2, operator):
    if operator=="+":
        return v1 + v2
    elif operator=="-":
        return v1 - v2
    elif operator=="*":
        return v1*v2
    elif operator=="/":
        if v2==0:
            print("Denominator is 0, NOT VALID")
            return v1
        else:
            return v1/v2


# In[21]:


while True:
    try:
        v1_input = float(input("Enter First Value : "))
    except Exception as e:
        print("INVALID INPUT")
        continue
    
    operator_input =  input("Enter Operator : ")
    
    if operator_input not in ("+", "-", "*", "/"):
        print("INVALID INPUT. You can only use +, -, *, /")
        continue
    
    try:
        v2_input = float(input("Enter Second Value : "))
    except Exception as e:
        print("INVALID INPUT")
        continue
    
    print(f"Result : {calculator(v1_input, v2_input, operator_input)}")

    o_input = input("Wanna do calculation again? {y/n} : ")
    if o_input=='n':
        break


# In[ ]:




