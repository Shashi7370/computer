# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 00:28:17 2023

@author: shash
"""

# List in python
l=[1,2,3,4,5,6]
l2=[1,2,3,[4,5,6]]
print(l[2])
print(l2[3][1])
l3=[1,2,"Hello",[2,3,4]]
print(l3[2])
print(l3[0:2])
print(l3[1: ])
print(l[0: :2])
print(l[-1: :-1])


# List Iteration in python
l=[10,20,30,40,50,60]
t=len(l)
print(t)
for n in range(t):
    print(l[n])
for a in l:
    print(a)
# reverse
for n in range(t-1,-1,-1):
    print(l[n])
l1=[10,20,30,40,50,60,70,80,90]
le=len(l1)
print(le)
for b in range(le):
    print(b,l1[b])
    
# List comprehension
l=[]
for a in range(1,101):
    # print(a)
    l.append(a)
print(l)

n=[m for m in range(1,101)]
print(n)

s="hello"
d=[g for g in s]
print(d)