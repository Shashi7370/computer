# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:35:05 2023

@author: shash
"""

# Program to convert string to string in List

n=input("Enter the value :-")
print(n)
a=n.split()
print(a)

l=[]
for b in range(3):
    n=input("Enter the value"+str(b)+":-")
    print(n)
    l.append(n)
print(l)