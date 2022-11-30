#!/usr/bin/env python
# coding: utf-8

# In[4]:


### Solution 1
KM = float(input("Enter KM Values"))
Miles = (0.621371)*KM
print(KM,"Kilometer in mileS will be",Miles)


# In[6]:


### Solution 2
Celsius = float(input("Enter temprature in celsius : "))
Fahrenheit = (Celsius * 1.8)+32
print("Temperature in Fahrenheit : ", Fahrenheit)


# In[8]:


### Solution 3
import calendar
Year = int(input("Enter year: "))
Month = int(input("Enter month: "))
calendar = calendar.month(Year,Month)
print(calendar)


# In[9]:


## Solution 4
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[11]:


## Solution 5
a = 5
b = 6 

a = a^b
b = a^b
a = a^b
print(a)
print(b)

