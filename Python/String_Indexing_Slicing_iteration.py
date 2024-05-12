# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:46:10 2023

@author: shash
"""

# String indexing - always count 0index
s="Shashikant KUmar Amba" 
print(s[5])
print(s[-2])


# String Slicing
s="Shashikant KUmar Amba" 
print(s[0:5])
print(s[0::2])

# Reverse Slicing
print(s[-1::-2])
print(s[-1::-1])


# String iteration in python
s="Shashikant KUmar Amba" 
t=len(s)
print(t)
for a in range (t):
    print(a)
    print(s[a])
