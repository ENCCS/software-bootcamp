#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

print("\nArgument List:", str(sys.argv))

print("This is the name of this program:", sys.argv[0])

print("This is the input argument(s) for this programe", list(sys.argv[1:]), end='\n\n')

print("Number of elements including the name of this program:", len(sys.argv))
print("Number of elements excluding the name of this program:", (len(sys.argv)-1), end='\n\n')

if (len(sys.argv)-1) >= 2:
    print("\tThere are two or more arguments.")
    print("\tThe addition of the first two elements is ", sys.argv[1] + sys.argv[2])
    print("\t", type(sys.argv[1]), type(sys.argv[2]))
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        print("\tThe addition of the first two element is ", eval(sys.argv[1]) + eval(sys.argv[2]))
elif (len(sys.argv)-1) == 1:
    print("There is only one input argument.")
else:
    print("There is no input argument")
print()
