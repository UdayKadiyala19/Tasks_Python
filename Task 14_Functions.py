#!/usr/bin/env python
# coding: utf-8

# 
# 1. 
# 
#    - Create a lambda function that takes two arguments and returns their sum.
#    - Create another lambda function that takes a single argument and returns its square.
#    - Use the `lambda` functions to calculate the sum and square of various numbers and print the results.
# 
# 2. 
#    - Define a list of integers.
#    - Use the `filter` function to create a new list that contains only the even numbers from the original list.
#    - Use the `filter` function again to create a new list that contains only numbers greater than 10 from the original list.
#    - Print both filtered lists.
# 
# 3. 
#    - Define a list of strings where each string represents a number (e.g., `["1", "2", "3"]`).
#    - Use the `map` function to convert each string to an integer and store the result in a new list.
#    - Use the `map` function again to square each integer in the new list and store the result in another new list.
#    - Print both new lists.
# 
# 4. 
#    - Create a list of dictionaries, where each dictionary represents a person with keys "name" and "age". Example: ` [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, ...]`
#    - Use the `filter` function to create a new list that contains only the people who are older than 25.
#    - Use the `map` function to create a new list that contains the names of the filtered people.
#    - Print the list of names.
# 
# 5. 
#    - Create a program that reads a list of numbers from the user (you can use the `input` function for this).
#    - Use `map` and `filter` functions to perform the following operations:
#      - Square each number.
#      - Filter out numbers that are not divisible by 3.
#    - Print the result.
# 

# 
# 1. 
# 
#    - Create a lambda function that takes two arguments and returns their sum.
#    - Create another lambda function that takes a single argument and returns its square.
#    - Use the `lambda` functions to calculate the sum and square of various numbers and print the results.

# In[5]:


add= lambda x,y:x+y
add(2,3)


# In[6]:


square= lambda n: n**2
square(6)


# In[14]:


add1 = lambda *n:sum(n)
square1 = lambda m: m*m

print(add1(1,2,3,4))
print(square1(1))


# 2. 
#    - Define a list of integers.
#    - Use the `filter` function to create a new list that contains only the even numbers from the original list.
#    - Use the `filter` function again to create a new list that contains only numbers greater than 10 from the original list.
#    - Print both filtered lists.

# In[30]:


List1= [1,2,3,4,5,6,7,8,11,15,100,90]

def fun(n):
    if n%2==0:
        return n
    
def fun2(n):
    if n>10:
        return n
    
New_list1= list(filter(fun,List1))
New_list2= list(filter(fun2,List1))


# In[31]:


New_list1


# In[32]:


New_list2


# 3. 
#    - Define a list of strings where each string represents a number (e.g., `["1", "2", "3"]`).
#    - Use the `map` function to convert each string to an integer and store the result in a new list.
#    - Use the `map` function again to square each integer in the new list and store the result in another new list.
#    - Print both new lists.

# In[73]:


string1 = ["1","2","3","5","10","11"]

New_list1 = list(map(int,string1))


# In[74]:


New_list1


# In[98]:


def fun(n):
    
    return n*n

New_list2= list(map(fun,New_list1))


# In[99]:


New_list2


# 4. 
#    - Create a list of dictionaries, where each dictionary represents a person with keys "name" and "age". Example: ` [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, ...]`
#    - Use the `filter` function to create a new list that contains only the people who are older than 25.
#    - Use the `map` function to create a new list that contains the names of the filtered people.
#    - Print the list of names.

# In[29]:


List= [{"name":"Uday","age":22},{"name":"Sathish","age":21},{"name":"Raju","age":29},{"name":"Rani","age":30}]

def fun(n):
    if n["age"]>25:
        return n

list1= list(filter(fun,List))
list1


# In[33]:


def fun1(n):
    return {"name":n["name"]}

list(map(fun1,list1))


# 5. 
#    - Create a program that reads a list of numbers from the user (you can use the `input` function for this).
#    - Use `map` and `filter` functions to perform the following operations:
#      - Square each number.
#      - Filter out numbers that are not divisible by 3.
#    - Print the result.

# In[34]:


list1=[]
n= int(input("Enter the list size:"))

for i in range(1,n+1):
    A= int(input(f"input{i}::  "))
    list1.append(A)
print(list1)

def num(n):
    return n**2

def num2(n):
    return n%3 != 0

square= list(map(num,list1))

not_divisible= list(filter(num2,list1))


# In[35]:


square


# In[36]:


not_divisible


# In[ ]:




