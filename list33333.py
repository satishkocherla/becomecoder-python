"""
import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def countprimes(n,data):
    c=0
    for i in data:
        if isprime(i):
            c+=1
    return c 




    
n=int(input())
data=list(map(int,input().split()))
c=countprimes(n,data)
print(c)

"""
import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findprimes(n,data):
    s=[]
    for i in data:
        if isprime(i):
            s.append(i)
    return s

n=int(input())
data=list(map(int,input().split()))
primes=findprimes(n,data)
print(*primes)

