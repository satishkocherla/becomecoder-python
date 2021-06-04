def original(n,data):
    a=[]
    for i in data:
        if i not in a:
            a.append(i)
    return a
n=int(input())
c=0
data=list(map(int,input().split()))
d=original(n,data)
print(*d)

for i in range(len(d)):
    if data[i]==d[i]:
        c+=1
print(c)
"""
10
4 3 1 2 5 3 2 6 7 6
output:
4 3 1 2 5 6 7
"""
