#!/usr/bin/env python
# coding: utf-8

# In[4]:


## Solution1
def length_calculation(num_val):
   length = 0
   while(num_val != 0):
      length = length + 1
      num_val = num_val//10
   return length
my_num = 192
remaining = sum_val = 0
len_val = length_calculation(my_num)
print("A copy of the original number is being made...")
num_val = my_num
while(my_num > 0):
   remaining = my_num%10
   sum_val = sum_val + int(remaining**len_val)
   my_num = my_num//10
   len_val = len_val - 1
if(sum_val == num_val):
   print(str(num_val) + " is a disarium number !")
else:
   print(str(num_val) + " isn't a disarium number")


# In[8]:


#Solution 2
def calculateLength(n):  
    length = 0;  
    while(n != 0):  
        length = length + 1;  
        n = n//10;  
    return length;  
   
#sumOfDigits() will calculates the sum of digits powered with their respective position  
def sumOfDigits(num):  
    rem = sum = 0;  
    len = calculateLength(num);  
      
    while(num > 0):  
        rem = num%10;  
        sum = sum + (rem**len);  
        num = num//10;  
        len = len - 1;  
    return sum;  
    
result = 0;  
   
#Displays all disarium numbers between 1 and 100  
print("Disarium numbers between 1 and 100 are");  
for i in range(1, 101):  
    result = sumOfDigits(i);  
      
    if(result == i):  
        print(i), 


# In[9]:


# solution 3
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num = int(input("Enter a number"));    
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);    
     
#Happy number always ends with 1    
if(result == 1):    
    print(str(num) + " is a happy number");    
#Unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print(str(num) + " is not a happy number");   


# In[11]:


# Solution 4
def check_happy_num(my_num):
   remaining = sum_val = 0
   while(my_num > 0):
      remaining = my_num%10
      sum_val = sum_val + (remaining*remaining)
      my_num = my_num//10
   return sum_val
print("The list of happy numbers between 1 and 100 are : ")
for i in range(1, 101):
   my_result = i
   while(my_result != 1 and my_result != 4):
      my_result = check_happy_num(my_result)
   if(my_result == 1):
      print(i)


# In[10]:


# Solution 5
my_num = int(input("Enter a number"))
remaining = sum_val = 0
print("A copy of the number to be checked is being made...")
my_num_copy = my_num;
while(my_num > 0):
   remaining = my_num%10;
   sum_val = sum_val + remaining;
   my_num = my_num//10;
if(my_num_copy % sum_val == 0):
   print(str(my_num_copy) + " is a Harshad number");
else:
   print(str(my_num_copy) + " isn't a Harshad number");


# In[13]:


# Solution 6
def isPronicNumber(num):
    flag = False;
    
    for j in range(1, num+1):
        #Checks for pronic number by multiplying consecutive numbers
        if((j*(j+1)) == num):
            flag = True;
            break;
    return flag;
 
#Displays pronic numbers between 1 and 100
print("Pronic numbers between 1 and 100: ");
for i in range(1, 101):
    if(isPronicNumber(i)):
        print(i),
        print(" "),

