#!/usr/bin/env python
# coding: utf-8

# ### Question 01
# 
# What are escape characters, and how do you use them?
# 
# *Solution*:-
# 
# An escape character is a backslash \ followed by the character you want to insert.

# In[1]:


print('I'm Pretty Sure 'Exploring' Is Code')


# In[2]:


print('I\'m Pretty Sure \'Exploring\' Is Code')


# ### Question 02
# 
# What do the escape characters n and t stand for?
# 
# *Solution*:-
#     
# \n : New line escape character                                                                                                 
# \t : Tab space escape character

# In[4]:


# Use of \n
print("Hello!!!\nI'm tina.")


# In[5]:


# Use of \t
print("Hello!!!\tI'm tina.")


# ### Question 03
# 
# What is the way to include backslash character in a string?
# 
# *Solution*:-
# 
# A blackslash character can be introduced with double blackslash characters.

# In[6]:


# Using single backslash character
print('\')


# In[7]:


print('\\')


# ### Question 04
# 
# The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
# 
# *Solution*:-
# 
# Because the complete string is enclosed under double quotes.

# In[10]:


# if string was enclosed in single quotes it would have been a problem
print('Howl's Moving Castle')


# Question 05
# 
# How do you write a string of newlines if you don't want to use the n character?
# 
# *Solution*:-
#     
# By default print statements add a new line character at the end of the string. We have to use multiline approach.

# In[11]:


print("Hello")
print("World")


# ### Question 06
# 
# What are the values of the given expressions?
# 
# 'Hello, world!'[1]                                                                                                             
# 'Hello, world!'[0:5]                                                                                                           
# 'Hello, world!'[:5]                                                                                                             
# 'Hello, world!'[3:]                                                                                                             
#     
# *Solution*:-
# 

# In[12]:


s = "Hello, world!"


# In[13]:


s[1]


# In[14]:


s[0:5]


# In[15]:


s[:5]


# In[16]:


s[3:]


# ### Question 07
# 
# What are the values of the following expressions?
# 
# 'Hello'.upper()                                                                                                                 
# 'Hello'.upper().isupper()                                                                                                       
# 'Hello'.upper().lower()                                                                                                         
#     
# *Solution*:-

# In[17]:


s = "Hello"


# In[18]:


s.upper()


# In[19]:


s.upper().isupper()


# In[20]:


s.upper().lower()


# ### Question 08
# 
# What are the values of the following expressions?
# 
# *Solution*:-

# _*'Remember, remember, the fifth of July.'.split()                                                                             
#     '-'.join('There can only one.'.split())*_

# In[22]:


'Remember, remember, the fifth of July.'.split()


# In[23]:


'-'.join('There can only one.'.split())


# ### Question 09
# 
# What are the methods for right-justifying, left-justifying, and centering a string?
# 
# *Solution*:-

# In[24]:


help(str.rjust)


# In[25]:


s = "hello"
length = 10
fillchars = "$"

print(s.rjust(length, fillchars))


# In[26]:


help(str.ljust)


# In[27]:


s = "hello"
length = 10
fillchars = "$"

print(s.ljust(length, fillchars))


# In[28]:


help(str.center)


# In[29]:


s = "hello"
length = 10
fillchars = "$"

print(s.center(length, fillchars))


# Question 10
# 
# What is the best way to remove whitespace characters from the start or end?
# 
# *Solution*:-
#     
# using .strip() function

# In[31]:


help(str.strip)


# In[33]:


s = "  Hello, I'm Tina. " 


# In[34]:


print(len(s))
print(s)


# In[35]:


# remove whitespaces
s = s.strip()


# In[36]:


print(len(s))
print(s)


# In[ ]:




