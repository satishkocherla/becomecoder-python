"""
def findmin(n,data):
    d=data[0]
    a=[]
    ct=0
    for i in data:
        if d==i:
            ct+=1
        if d>i:
            d=i
            ct=1
    for i in range(n):
        if d==data[i]:
            a.append(i)
    return d,ct,a
        


n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)

"""
def findmin(n,data):
    d=min(data)
    a=[]
    ct=data.count(d)
    for i in range(n):
        if d==data[i]:
            a.append(i)
    return d,ct,a
        


n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)

