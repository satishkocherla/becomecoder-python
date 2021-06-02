from math import *
def rev(n):
    k=0
    while n:
        r=n%10
        n=n//10
        k=k*10+r
    return k
def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=rev(data[i])
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)
