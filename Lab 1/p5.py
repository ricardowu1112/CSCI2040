#!/usr/bin/env python
# coding: utf-8

# In[25]:


import getpass
import string


alpha = [char for char in string.ascii_letters]
num = [str(x) for x in range(11)]

def first_try(n):
    first_input = getpass.getpass("Please input your password: ")
    while True:
        if((len(first_input) >= 8) and any(char in first_input for char in alpha) and any(char in first_input for char in num)):
            break
        else:
            print("Invalid input.")
            first_input = getpass.getpass("Please try again: ")
    return first_input


def second_try(first_input):
    count = 0
    second_input = getpass.getpass("Please input again to confirm your password: ")
    while True:
        if(first_input == second_input):
            break
        else:
            print("Those passwords did not match.")
            count += 1
        if(count >= 3):
            print("Those passwords did not match. Please set your password next time. Program ends.")
            return False
        second_input = getpass.getpass("Please try again: ")
    return first_input == second_input


while True:
    password = first_try(1)
    if(second_try(password) == True):
        print("Successfully set your password!")
    break

