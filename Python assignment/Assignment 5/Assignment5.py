#!/usr/bin/env python
# coding: utf-8

# In[1]:


# solution 1
def calculate_lcm(x, y):  
    # selecting the greater number  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2)) 


# In[4]:


# Solution 2
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

print("The H.C.F. is", compute_hcf(num1, num2))


# In[5]:


# Solution 3
dec = int(input("Enter Number: "))
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[10]:


# Solution 4
c = input("Enter")
# print the ASCII value of assigned character in c
print("The ASCII value of '" + c + "' is", ord(c))


# In[11]:


# Solution 5
first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")

