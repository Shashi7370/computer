# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:14:10 2023

@author: shash
"""

# List :- List is an ordered sequence of items
L=[1,2,3.2,'sk']
print(L,type(L))
L[1]=10
L[2]=12
print(L,type(L))


# Tupple :-Same as a list
T=(5,'shashikant',20)
print(T,type(T))


# Dictionary:- Dictionary is an unordered collection of Key-value pairs
# d={1,'value','key',2}
# print(d,type(d))........This is a set
d={1:'value','key':2}
print(d,type(d))
d1={'course_name':'Python','Course_duration':'3 months'}
print(d1,type(d1))
print(d1['course_name'])
print(d['key'])
print(d[1])


# Set :- A set is an unordered collection of items
s={1,3,4,5,'hii'}
print(s,type(s))