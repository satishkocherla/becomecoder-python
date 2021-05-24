"""
a,b=map(int,input().split())
res=1
t=2
while True:
    if a%t==0 and b%t==0:
        res=res*t
        a//=t
        b//=t
    else:
        t+=1
    if a<t or b<t:
        break
print(res*a*b)
"""

"""
def lcm(a,b):
    res=1
    t=2
    while a>=t and b>=t:
        if a%t==0 and b%t==0:
            a//=t
            b//=t
            res=res*t
        else:
            t+=1
    return res*a*b
           
a,b=map(int,input().split())
print(lcm(a,b))
"""

"""
def lcm(a,b):
    t=2
    if a<t and b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return t*lcm(a,b)
           
a,b=map(int,input().split())
print(lcm(a,b))
"""

def lcm(a,b):
    m=max(a,b)
    while True:
        print(m)
        if m%a==0 and m%b==0:
            return m
        else:
            m+=1



a,b=map(int,input().split())
print(lcm(a,b))

    
