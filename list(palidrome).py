from math import *
def palin(n):
    temp=n
    k=0
    while n:
        r=n%10
        n=n//10
        k=k*10+r
    return k==temp
def sumofdigits(n,data):
    j=0
    for i in range(len(data)):
        if palin(data[i]):
            j+=1
    return j
n=int(input())
data=list(map(int,input().split()))
print(sumofdigits(n,data))

