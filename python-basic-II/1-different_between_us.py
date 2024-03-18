#!/usr/bin/python3

"""
    1. Write a Python function that takes a sequence of 
    numbers and determines whether all the numbers are 
    different from each other.
"""

def uniq_numbers(number_list=[]):

    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            if (number_list[i] == number_list[j]):
                return (False)

    return True


my_list = [11, 2, 3]

if (uniq_numbers(my_list)):
    print("The list contains uniq elements".format())
else:
    print("The list doesn't contains uniq elements".format())
