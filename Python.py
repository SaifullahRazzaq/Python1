#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Assignment task 2

import sys;
a=sys.version
print("Your phython version is",a)


# In[5]:


#Assignment task 3

import datetime;
current_date=datetime.datetime.now();
print("Your current date is",current_date);


# In[10]:


#Assigmnet task 4
userinput=float(input("enter your radius"));
calculate_area=3.142*userinput*2;
print(calculate_area)


# In[15]:


#Assignment Task 5
firstname=(input("enter your first name"));
lastname=(input("enter your last name"));
full_name=lastname,firstname
print("===>",full_name);


# In[23]:


#Assignment Task 6

x = input("Type a number: ")
y = input("Type another number: ")

sum = int(x) + int(y)

print("The sum is: ", sum)

