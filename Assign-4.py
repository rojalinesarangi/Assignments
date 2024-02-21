#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# 
# What exactly is []?
# 
# *Solution*:-
# 
# [] represents an empty list in Python.

# In[1]:


my_list = []
print(type(my_list))


# ### Question 2
# 
# In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
# (Assume [2, 4, 6, 8, 10] are in spam.)
# 
# *Solution*:-

# In[6]:


# define spam
spam = [2, 4, 6, 8, 10]

spam[2]='hello'
spam


# ### Question 3
# 
# Assuming,
# 
# spam = ['a', 'b', 'c', 'd']
# 
# What is the value of spam[int(int('3' * 2) / 11)]
# 
# *Solution*:-
# 
# Steps,
# 
# 1.spam[int(int('3'*2)/11)]
# 
# 2.spam[int(int('33')/11)]
# 
# 3.spam[int(33/11)]
# 
# 4.spam[int(3.0)]
# 
# 5.spam[3] = 'd'

# In[7]:


spam = ['a', 'b', 'c', 'd']
spam[int(int('3'*2)/11)]


# ### Question 5
# Assuming,
# 
# spam = ['a', 'b', 'c', 'd']. 
# What is the value of spam[:2]?
# 
# *Solution*:-
# 
# This is called string slicing.

# In[8]:


spam = ['a', 'b', 'c', 'd']
spam[:2]


# ### Question 6
# 
# Assuming,
# 
# bacon = [3.14, 'cat', 11, 'cat', True]
# What is the value of bacon.index('cat')?
# 
# *Solution*:-
# 
# Returns first occurance index.

# In[9]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')


# ### Question 7
# 
# Assuming,
# 
# bacon = [3.14, 'cat', 11, 'cat', True]                                                                                         
# How does bacon.append(99) change the look of the list value in bacon?
# 
# *Solution*:-

# In[11]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99)
bacon


# ### Question 8
# 
# Assuming,
# 
# bacon = [3.14, 'cat', 11, 'cat', True]                                                                                         
# How does bacon.remove('cat') change the look of the list in bacon?
# 
# *Solution*:-

# In[13]:


bacon = [3.14, 'cat', 11, 'cat', True]
print(f'original list:{bacon}')
print(f'new list:{bacon}')
bacon.remove('cat')


# ### Question 9
# 
# What are the list concatenation and list replication operators?
# 
# *Solution*:-
# 
# Operator used for list concatenation is +, whereas operator used for list replication is *.

# In[14]:


# list concatenation

list1 = ['hello', 'my', 'name']
list2 = ['is', 'tina']

list1 + list2


# In[15]:


# list replication

list = ['3', 'tom', True]

list*2


# ### Question 10
# 
# What is difference between the list methods append() and insert()?
# 
# *Solution*:-

# In[16]:


help(list.append)


# In[18]:


help(list.insert)


# Append inserts an element to the end of the list, whereas insert method make use of index parameter to insert an element in the list.

# In[20]:


my_list = [1, 2, 3, 5]

append1 = 6
insert1 = 4

# append operation
print(f"Original List : {my_list}")
my_list.append(append1)
print(f"New List : {my_list}")

# insert operation
print(f"Inserting value 4 at index no 3")
my_list.insert(3, insert1)
print(f"New List : {my_list}")


# ### Question 11
# 
# What are the two methods for removing items from a list?
# 
# *Solution*:-

# In[25]:


# define a list
list = ['cat', 12, True, 213.23, "dog"]

# using remove()
list.remove(True)
list


# In[26]:


# using del, removes specific index
del list[1]
list


# ### Question 12
# 
# Describe how list values and string values are identical.
# 
# *Solution*:-
# 
# We can use loops, concatenation, replication methods, slicing to both list values and string values.

# In[29]:


string = "mycat"
my_list = ['m', 'y', 'c', 'a', 't']


# In[34]:


# using length method
len(string), len(my_list)


# In[37]:


# slicing first 2 characters
string[:2], my_list[:2]


# In[38]:


# check if t in string and list
't' in string, 't' in my_list


# In[39]:


# concatination
string + 's', my_list + ['s']


# ### Question 13
# 
# What's the difference between tuples and lists?
# 
# *Solution*:-

# List-Lists are mutable and values can be modified. Better for insertion and deletion                                           
# Tuples-Tuples are immutable and values cannot be modified. Better for accessing value

# In[44]:


list = [1,2,3,4]
tuple = (1,2,3,4)


# In[45]:


list[0] = 100
list


# In[46]:


tuple[0] = 100
tuple


# In[47]:


# size allocated in memory difference
list.__sizeof__(), tuple.__sizeof__()


# ### Question 14
# 
# How do you type a tuple value that only contains the integer 42?
# 
# *Solution*:-

# In[49]:


tuple = (42,)
tuple


# ### Question 15
# 
# How do you get a list value's tuple form? How do you get a tuple value's list form?
# 
# *Solution*:-

# my_list = [1,2,3,4]                                                                                                             
# print(tuple(my_list))
# 
# (1, 2, 3, 4)
# 
# my_tuple = (1,2,3,4)                                                                                                           
# print(list(my_tuple))
# 
# [1, 2, 3, 4]
# 

# ### Question 16
# 
# Variables that contain list values are not necessarily lists themselves. Instead, what do they contain?
# 
# *Solution*:-
# 
# Variables do not store values directly.                                                                                         
# Python variables work with references to objects representing the values.
# 
# For example, we have
# 
# a = [1,2,3]
# 
# Python creates a new reference for a to point at the object representing the value [1,2,3] in the memory.
# 

# ### Question 17
# 
# How do you distinguish between copy.copy() and copy.deepcopy()?
# 
# *Solution*:-
# 
# Let's understand by an example,

# In[70]:


# import copy module
import copy

# initialize our list
my_list = [1, [2, 3], 4]


# In[71]:


copy_list = copy.copy(my_list)

print(id(my_list))
print(id(copy_list))

print(id(my_list[1]))
print(id(copy_list[1]))


# copy_list becomes new object but my_list[1] is same object as copy_list[1]

# In[72]:


deepcopy_list = copy.deepcopy(my_list)

print(id(my_list))
print(id(deepcopy_list))

print(id(my_list[1]))
print(id(deepcopy_list[1]))


# deepcopy_list becomes new object and my_list[1] is new object
