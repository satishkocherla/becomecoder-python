"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""


"""
n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    t=1
    for j in range(1,i+1):
        print(t,end=" ")
        if t==0:
            t=1
        else:
            t=0
                
    print()
"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if 1==j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
