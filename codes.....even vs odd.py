"""
n=int(input())
oc=s=ec=0
while(n):
    r=n%10
    n=n//10
    s=s*10+r
n=s
r=0
while(n):
    r=n%10
    n=n//10
    if(r%2==0):
        ec=ec*10+r
    else:
        oc=oc*10+r
print(ec)
print(oc
"""
"""
n=int(input())
ec=0
oc=0
i=j=1
while(n):
    r=n%10
    n=n//10
    if(r%2==0):
        ec=r*j+ec
        j*=10
    else:
        oc=r*i+oc
        i*=10
print(ec)
print(oc)
"""

"""
n,sv,rv=map(int,input().split())
nn=0
c=1
while(n):
    r=n%10
    n=n//10
    if(r==sv):
        r=rv
    nn=nn+r*c
    c=c*10
print(nn)
"""

"""

n,sv,rv=map(int,input().split())
nn=c
temp=n
c=0
while(n):
    r=n%10
    n=n//10
    c+=1

n=temp
c-=1
while n>0:
    r=n//pow(10,c)
    n=n%pow(10,c)
    c-=1
    if(r%sv==0):
        r=rv
        rv+=1
        if(rv==10):
            rv=1
    nn=nn*10+r

print(nn)

"""

"""
n=int(input())
l=n%10
temp=n//10
c=0
while n:
    r=n%10
    n=n//10
    c=c+1
temp=temp*10+r
temp=temp%pow(10,c-1)
temp=l*pow(10,c-1)+temp

print(temp)

"""
"""

n=int(input())
l=n%10
temp=n//10
c=0
while n:
    r=n%10
    n=n//10
    c=c+1
m=temp%pow(10,c-2)
f=r
print(f,l,m)
"""
"""
n=int(input())
min=n%10
max=n%10
minc=0
maxc=0
while(n):
    r=n%10
    n=n/10
    if r==min:
        minc+=1
    elif r<min:
        min=r
        minc=1
    if r==max:
        maxc+=1
    elif r<max:
        max=r
        maxc=1
print(minc,maxc)
"""

"""
def sum(a,b,c):
    print(a,b,c)
    res=a+b+c
    return res

    
x=int(input())
y=int(input())
z=int(input())
r=sum(a=x,c=z,b=y)     #func call  sum(a,b)
print(r)
"""

"""
from main_funs import*
def pow(n,p=2):
    res=n**p
    return res
n=int(input())
p=int(input())
print(f.pow(n,p))
print(f.pow(n))
print(f.sum(n,p))


"""
def gen_fib(n):
    a,b=0,1
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    
n=int(input())
gen_fib(n)


