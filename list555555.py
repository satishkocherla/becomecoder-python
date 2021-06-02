from math import *
def sums(n):
    k=0
    while n:
        r=n%10
        n=n//10
        k=k+r
    return k
def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=sums(data[i])
    return data
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)
