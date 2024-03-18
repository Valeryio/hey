#!/usr/bin/python3

import sys
import locallib

"""
    Write a Python program that creates all possible 
    strings using the letters 'a', 'e', 'i', 'o', and 'I'.
    Ensure that each character is used only once.
"""

for i in range(1, len(sys.argv)):

    if (sys.argv[i].isdigit()):
        print("Sorry the caracter {:s}, is not a string!".format(sys.argv[i]))
    
    else:
        anagramsdict = []
        anagramdict = locallib.string_anagram(sys.argv[i])

        print("-" * (len(sys.argv[1]) + 12))
        print('|' + " "*3 + "x : " + sys.argv[i] + " "*3 + '|')
        print("-" * (len(sys.argv[1]) + 12))

        for i in range(len(anagramdict)):
            print('|' + (" "*3) + str(i) + " : " + str(anagramdict[i]) + " "*3 + '|')

        print("-" * (len(sys.argv[1]) + 12))
