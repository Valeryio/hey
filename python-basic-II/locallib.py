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


def issavedin(the_list, word):
    """
        This function determines if a word is savved in a
        dictionnary
    Args:
        dict: a list of words
        word: a word
    Returns:
        Return True of False
    """
    if len(the_list) == 0:
        return False

    for i in the_list:
        if (i == word):
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
