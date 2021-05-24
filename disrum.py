"""
def disrum(n):
    s=0
    i=1
    while n:
        r=n%10
        n=n//10
        s=s+pow(r,i)
        i+=1
    return s
n=int(input())
t=n
s=0
while n:
        r=n%10
        n=n//10
        s=s*10+r


print(t==disrum(s))
"""
"""
def disrum(n):
    i=0
    temp=n
    s=0
    while n:
        n=n//10
        i+=1
    n=temp
    while temp:
        r=temp%10
        temp=temp//10
        s=s*10+r
        i-=1
    return s==n

n=int(input())
print(disrum(n))
"""

