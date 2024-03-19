#!/usr/bin/python3

import sys
import locallib

negcounter = 0
poscounter = 0

result = {}
double = []
negnumbers = []
posnumbers = []
intlist = [1, -6, 4, 2, -1, 2, 0, -2, 0]
listcpy = intlist[:]

# Verification, stop the program, if it don't get negative and positive values!
for i in intlist:
    if (i < 0):
        negcounter += 1
    elif (i > 0):
        poscounter += 1
    else:
        pass

if not poscounter or not negcounter:
    sys.exit(1)

# Verification of double element in the given list
for i in range(len(intlist)):
    for j in range(i + 1, len(intlist)):
        if intlist[i] == intlist[j] and not locallib.issavedin(double,\
                intlist[i]):
            double.append(intlist[i])

# Deleting all the doubled values from the list
for i in double:
    listcpy.remove(i)

# Slicing the table in two different part
for i in listcpy:
    if (i < 0):
        negnumbers.append(i)
    elif (i >= 0):
        posnumbers.append(i)
    else:
        pass

# Find the right combinations
for i in range(len(negnumbers)):
    result.update({negnumbers[i] : locallib.findnumbercombination(listcpy, negnumbers[i])})

# Print the answer on the STDOUT
for key, value in result.items():
    print(f"{key} : {value}\n\n")
