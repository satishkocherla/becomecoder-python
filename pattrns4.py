"""
n=int(input())
j=5
for i in range(1,n+1):
    for k in range(1,n+1):
        if i%2==0:
            print(k,end=" ")
        else:
            print(i,end=" ")
    print()
"""


"""
n=int(input())
j=5
for i in range(1,n+1):
    for k in range(1,n+1):
        if i%2==1:
            print(k,end=" ")
        else:
            print(j,end=" ")
            j-=1
    j=5
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for k in range(1,n+1):
        if k==1:
            print(i,end=" ")
        else:
            print(k,end=" ")
    print()
"""

n=int(input())
for i in range(1,n+1):
    for k in range(n,0,-1):
        if i%2==0:
            print(i,end=" ")
        else:
            print(k,end=" ")
    print()
