#!/usr/bin/env python
# coding: utf-8

# 17. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list. Use list comprehension to solve this problem.
# 
# Example:
# 
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# Output: [2, 4, 6, 8, 10]

# In[1]:


def even_number(input_list):
    return [ num for num in input_list if num % 2 == 0]


# In[2]:


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = even_number(input_list)
print(number)


# 18.Implement a decorator function called ‘timer’ that measures the execution time of a function. The ‘timer’ decorator should print the time taken by the decorated function to execute. Use the ‘time’ module in Python to calculate the execution time.
# 
# Example:
# 
# import time
# 
# @timer
# def my_function():
#     # Function code goes here
#     time.sleep(2)
# 
# my_function()
# 
# Output:
# "Execution time: 2.00123 seconds"

# In[9]:


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the decorated function
        end = time.time()  # Record the end time
        execution = end - start  # Calculate the execution time
        print(f"Execution : {execution_time:.5f} seconds")  # Print the execution time
        return result  # Return the result of the decorated function

    return wrapper


# In[13]:


@timer
def my_function():
    # Function code goes here
    time.sleep(2)


# In[16]:


my_function()


# In[ ]:




