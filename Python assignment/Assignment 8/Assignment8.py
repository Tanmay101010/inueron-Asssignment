#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Solution 1
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)


# In[1]:


## Solution 2
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 

for i in range(len(A)):
 
 
    for j in range(len(B[0])):
 
      
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)


# In[2]:


## Solution 3
N = 4
 

def transpose(A):
 
 for i in range(N):
  for j in range(i+1, N):
   A[i][j], A[j][i] = A[j][i], A[i][j]
 

A = [ [1, 1, 1, 1],
 [2, 2, 2, 2],
 [3, 3, 3, 3],
 [4, 4, 4, 4]]
 
transpose(A)
 
print("Modified matrix is")
for i in range(N):
 for j in range(N):
  print(A[i][j], " ", end='')
 print()


# In[3]:


## Solution 4
def Func(S):
  W = S.split(" ")
  for i in range(len(W)):
     
      # convert all the words into lowercase
      W[i]=W[i].lower() 
  S = sorted(W)
  print(' '.join(S))
 
# Driver code
S = "the Quick brown fox jumPs over the lazY Dog"
 
# function call
Func(S)


# In[4]:


## Solution 5
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

