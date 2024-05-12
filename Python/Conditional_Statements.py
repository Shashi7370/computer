# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:43:39 2023

@author: shash
"""

# Conditional Statement in python (if, if  Else),if elif else
# if
a=20
if a%2==0:
    print("Even Number")
    
a=int(input("Enter the value of a:-"))
if a%2==0:
    print(a,"Even Number")

# if else
a=int(input("Enter the value of a:-"))
if a%2==0:
    print("Even Number")
else:
    print("Odd Number")
    
a=int(input("Enter the value of a:-"))
if a%2==0:
    print(a,"Even Number")
else:
    print(a,"Odd Number")    
    
# if elif else Statement
per=int(input("Enter the value of per:-"))
if per>=60:
    print("first Div")
elif per>=48:
    print("Second divsion")
elif per>35:
    print("3rd Div")
else:
    print("Fail")
    