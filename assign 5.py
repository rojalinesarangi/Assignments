#!/usr/bin/env python
# coding: utf-8

# ### Question 01
# What does an empty dictionary's code look like?
# 
# *Solution*:-

# In[3]:


dict = {}
dict


# ### Question 02
# 
# What is the value of a dictionary value with the key 'foo' and the value 42?
# 
# *Solution*:-

# In[4]:


dict1 = {'foo' : 42}

print(dict1)
print(f"Values of dictionary : {dict1.values()}")


# ### Question 03
# What is the most significant distinction between a dictionary and a list?
# 
# *Solution*:-

# Dictionaries are unordered collection of data points. It uses key, value structure to store the values.
# 
# Lists have ordered items.

# In[5]:


list1 = [1,2,3,4]
list1


# In[6]:


dict2 = {'foo' : 43, 'la' : 42, 'a':1}
dict2


# ### Question 04
# 
# What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# 
# *Solution*:-

# In[7]:


# initialize dict
my_dict = {'bar' : 100}
my_dict


# In[8]:


# accessing key 'foo'
my_dict['foo']


# ### Question 05
# 
# If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 
# *Solution*:-
# 
# dict.keys() returns a list of keys of the dictionary.

# In[10]:


# initialize dictionary
my_dict = {'dog': 1, 'cat': 2, 'parrot': 4}


# In[11]:


'cat' in my_dict


# In[12]:


'cat' in my_dict.keys()


# Maybe the difference is between time to access a key.

# ### Question 06
# 
# If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 
# *Solution*:-
# 
# 'cat' in spam checks if 'cat' key is present in dictionary or not.
# 
# 'cat' in spam.values() check 'cat' value in any of the key of spam.

# In[13]:


# initialize dictionary
my_dict = {'dog': 1, 'cat': 2, 'parrot': 4}


# In[14]:


'cat' in my_dict


# In[15]:


my_dict.values()


# In[16]:


'cat' in my_dict.values()


# ### Question 07
# 
# What is a shortcut for the following code?
# 
# if 'color' not in spam:
#     spam['color'] = 'black'
#     
# *Solution*:-

# In[17]:


help(dict.setdefault)


# In[18]:


spam = {}
spam.setdefault('color', 'black')


# In[19]:


spam


# ### Question 08
# 
# How do you "pretty print" dictionary values, using which module and function?
# 
# *Solution*:-
# 
# Using "json" module.

# In[20]:


my_dict = {'a' : {'name': 'Anne', 'Age': 22}, 'b' : {'name': 'Luke', 'Age': 55}}


# In[21]:


print(my_dict)


# In[23]:


import json

print(json.dumps(my_dict, indent=4))

