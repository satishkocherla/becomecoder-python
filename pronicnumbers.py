"""
def ispronic(n):
    for i in range(1,n//2+1):
        print(i)
        if i*(i+1)==n:
            return True
    return False


n=int(input())
print(ispronic(n))
        
"""


from math import*

def ispronic(n):
    i=int(sqrt(n))
    print(i)
    return i*(i+1)==n


n=int(input())
print(ispronic(n))
        


