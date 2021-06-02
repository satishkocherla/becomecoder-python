import math as m
def isprime(num):
    s=int(m.sqrt(num))
    if n==1:
        return 0
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findprimes(n,data):
    s=[]
    d=[]
    for i in data:
        if isprime(i):
            s.append(i)
        else:
            d.append(i)
    return sum(s),sum(d)

n=int(input())
data=list(map(int,input().split()))
primes,nonprimes=findprimes(n,data)
print(*primes)
print(*nonprimes)
