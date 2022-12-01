#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Solution 1
.
def fact(n):

    f = 1

    for i in range(1,n+1):
        f = f * i
    return f


x = int(input("Enter a number:" ))

result = fact(x)


print(result)


# In[5]:


# Solution 2
n = int(input("Enter the number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)


# In[8]:


num = int(input("Enter a number: "))
n1,n2 = 0,1
sum = 0
for i in range(0, num):
    print(sum, end= " ")
    n1 = n2
    n2 = sum
    sum = n1 + n2


# In[10]:


## Solution 3
number = int(input('Enter any positive number : '))

def check_armstrong(num):
    if num in range(1,10):
        return True

    order = len(str(num))
    sum = 0
    original = num
    while num>0:
        digit = num % 10
        sum += digit ** order
        num = num // 10
    if sum == original:
        return True
    return False

if check_armstrong(number):
    print('number is armstrong')
else:
    print('number is not armstrong')


# In[12]:


##Solution 4
lower = int(input("enter lower"))
upper = int(input("enter upper"))

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# In[14]:



num = int(input("Enter number"))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0

   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

