# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 23:37:34 2023

@author: shash
"""

# =============================================================================
# Opetators in Python
# =============================================================================

a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(5**2)
print(5**3)
print(10//3)
print(15//3)

# =============================================================================
# Assignment Opetator
# =============================================================================

x = 10
print(x)
x = x+5
print(x)
x+=5
print(x)
x-=5
print(x)
x=x-5
print(x)

# comparison_Operator

x=10
y=20
print(x==y)
print(x!=y)
print(x>y)

# Logical Operator and, or, not

print(x==10 and x<y)
print(x==y and x<y)
print(x==y or x<y)
print(not x==10)

# Membership Operators

x="Hello"
print('H' in x)
print('h' in x)
l=[10,20,30,40,50]
print(l)
print(60 in l)
print(50 in l)
print(60 not in l)

# Identity Operators

x=10
y=20
print(x is y)
print(x is y, x==y)
print(x is not y, x!=y)


# Bitwise Operator

x=10
Y=8
print(bin(x))
print(bin(y))
