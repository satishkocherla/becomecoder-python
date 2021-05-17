"""
def gen_fib(n,l,u):
    a,bc,=0,1,0
    print(a,b,c,end=" ")
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
    
n,l,u=map(int,input().split())   #input
gen_fib(n,l,u)   #func call   gen_fib one arg
"""


def gen_fib(l,f):
    if l==0:
        print(a,b,end=" ")
    if l==1:
        print(b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        if c<l and c>f:
            print(c,end=" ")
    
f,l=map(int,input().split())   #input
gen_fib(f,l)   #func call   gen_fib one arg



"""
def gen_fib(n):
    a,b=0,1
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    
n=int(input())   #input
gen_fib(n)   #func call   gen_fib one arg

"""
