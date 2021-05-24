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
def lcm(a,b):
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
    return res*a*b
           
a,b=map(int,input().split())
print(lcm(a,b))
