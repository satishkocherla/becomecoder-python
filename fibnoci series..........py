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

"""
def gen_fib(f,l):
    a,b=0,1
    for i in range(0,l+1):
        c=a+b
        if c<=f and c>=l:
            print(c,end=" ")
        a=b
        b=c
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
    if f==c:
        print(True)
    else:
        print(False)
n=int(input())
f=int(input())#input
gen_fib(n)   #func call   gen_fib one arg


