#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Solution 1
import array as ar

def SumofArray(arr):
    sum=0
    n = len(arr)
    for i in range(n):
        sum = sum + arr[i]
    return sum
  
a = ar.array('i',[10, 21, 12, 13])
   
print ('Sum of the array is ', SumofArray(a) ) 


# In[10]:


## Solution 2

def largest(arr,n):
   
   max = arr[0]

   for i in range(1, n):
      if arr[i] > max:
         max = arr[i]
   return max

arr = [23,1,32,67,2,34,12]
n = len(arr)
Ans = largest(arr,n)
print ("Largest element given in array is",Ans)


# In[11]:


## Solution 3

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

 

arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))


# In[12]:


## SOlution 4
def rvereseArray(arr, start, end):
    while start < end :
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] =temp
        start += 1
        end -= 1
  

def printArray(arr, n) :
    for i in range(n):
        print(arr[i], end = " ")
  
  
# Function to left rotate
# arr[] of size n by k */
def splitArr(arr, k, n):
    rvereseArray(arr, 0, n - 1)
    rvereseArray(arr, 0, n - k - 1)
    rvereseArray(arr, n - k, n - 1)
  

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
k = 2
splitArr(arr, k, n)
printArray(arr, n)


# In[13]:


## Solution 5
def ismonotone(a):
    n=len(a) #size of array
    if n==1:
        return True
    else:
       
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

A = [6, 5, 4, 2]
print(ismonotone(A))
b = [6, 2, 4, 2]
print(ismonotone(b))
c=[4,3,2]
print(ismonotone(c))
d=[1]
print(ismonotone(d))

