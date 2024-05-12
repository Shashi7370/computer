# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:09:08 2023

@author: shash
"""

# Function in List
# Delete element from List - del, pop(), remove(), clear() - pop return value but del not return value
l=[20,30,50,60]
print(l)
del(l[1])
print(l)

l2=[20,30,50,60]
l2.pop(2)
print(l2)

l3=[20,30,50,60]
l3.remove(50)
print(l3)

l4=[20,30,50,60]
l4.clear()
print(l4)

# Update Element from List - insert(index,value), append(), extend()
l=[20,30,50,60,70]
l[1]=25
print(l)

l1=[20,50,60,80,90]
l1.insert(1,40)
print(l1)

l2=[10,30,40,60,80,92]
l2.append(50)
print(l2)
l3=[10,20,30,40]
n=[50,60]
l3.append(n)
print(l3)

l4=[10,20,30]
n=[50,60]
l4.extend(n)
print(l4)