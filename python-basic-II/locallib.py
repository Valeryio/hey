#!/usr/bin/python3

import random
import sys

"""
    Write a Python program that creates all possible 
    strings using the letters 'a', 'e', 'i', 'o', and 'I'.
    Ensure that each character is used only once.
"""

def factorial(x):
    """
        This function returns the factorial of a number
    Args:
        x: an integer

    Return:
        An integer
    """
    if (x == 1):
        return x
    return x * factorial(x - 1)


def issavedin(the_list, x):
    """
        This function determines if a word is savved in a
        dictionnary
    Args:
        dict: a list of words
        x: a word, or a number
    Returns:
        Return True of False
    """
    if len(the_list) == 0:
        return False

    for i in the_list:
        if (i == x):
            return True
    return False


def string_anagram(basicset):
    """
        This function returns a set of all combinations of
        a word. An anagram
    Args:
        basicset: a word
    Returns:
        A dict of element
    """

    basicset = list(basicset)
    numberstringcomb = factorial(len(basicset))
    stringslist = {}
    
    while (len(stringslist) < numberstringcomb):
        random.shuffle(basicset)

        if not issavedin(stringslist, str(basicset)):
            stringslist[len(stringslist)] = ''.join(basicset)

    return stringslist


def removealloccurences(the_list, x):
    """
        This function removes all the elements in a list
    Args:
        the_list: the list of element
        x: the element to remove
    Returns:
        Nothing
    """
    while x in the_list:
        the_list.remove(x)


def findnumbercombination(the_list, x):
    """
        This function takes a list, and find all the combination
        of two elements that could cancel the digit x
    Args:
        the_list: the list of element
        x: the element to remove
    Returns:
        A dictionnary with all the combination that of two elements
        that could cancel the number x
    """

    dictofcombinations = []

    for i in range(len(the_list)):
       # print("L'index : {:d}".format(x))
        for j in range(i + 1, len(the_list)):
            #print(f"NOus avons : {i} + {j}")
           # print(f"NOus avons : {the_list[i]} + {the_list[j]} + {x} =\
            #        {the_list[i] + the_list[j]}")
            if  (the_list[i] + the_list[j] + x) == 0:
               # print(f"NOus avons : {the_list[i]} + {the_list[j]} + {x} = 0")
                dictofcombinations.append([x, the_list[i], the_list[j]])

    return (dictofcombinations)
