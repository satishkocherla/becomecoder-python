"""
from math import*

n=int(input())
s=int(sqrt(n))
c=0
for i in range(1,s+1):
    if n%i==0:
        if i==n//i:
            c+=1
        else:
            c+=2
print(c)
"""


