# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:01:13 2023

@author: shash
"""

# Simple Calculator in python
a=float(input("Enter the value of a :-"))
b=float(input("Enter the value of b :-"))
opr=input("Enter the operator is :- ")
if opr=="+":
    print(a+b)
elif opr=="-":
    print(a-b)
elif opr=="*":
    print(a*b)
elif opr=="/":
    print(a/b)
else:
    print("sorry invalid oprator")