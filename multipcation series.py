"""
a,b=map(int,input().split())
c=0
while True:
    if a%2:
        c=c+b
    if a==0:
        break
    a=a//2
    b=b*2
print(c)
"""


"""
def mul(a,b,c=0):
    while a:
        if a%2:
            c=c+b
        a=a//2
        b=b*2
    return c

(

a,b=map(int,input().split())
c=mul(a,b)
print(c)
"""


n=int(input())
while n!=1:
    print(n)
    if n%2==1:
        n=3*n+1
    else:
        n=n//2
print(n,end=" ")
        
