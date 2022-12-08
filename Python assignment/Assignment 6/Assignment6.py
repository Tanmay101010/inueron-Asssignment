#!/usr/bin/env python
# coding: utf-8

# In[1]:


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[4]:


### Solution 2
 
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 15

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[14]:


### Solution 3
def BMI(height, weight): 
  bmi = weight/(height/100)**2 
  return bmi 
height = float(input("Enter height in CM "))
weight = float(input("Enter weight In KG "))
bmi = BMI(height, weight) 
print("The BMI is", bmi)
print("Health status = ",end="")
if (bmi < 18.5): 
  print("Underweight") 
elif ( bmi >= 18.5 and bmi < 24.9): 
  print("Healthy") 
elif ( bmi >= 24.9 and bmi < 30): 
  print("Overweight") 
elif ( bmi >=30): 
  print("Suffering from Obesity")


# In[15]:


### Solution 4
import math as m
print(m.log(10))


# In[29]:


### Solution 5

# Returns the sum of series
def sumOfSeries(N):
    x = (N * (N + 1)  / 2)
    return (int)(x * x)

  
N = int(input("Enter number: "))
print(sumOfSeries(N))


# In[ ]:




