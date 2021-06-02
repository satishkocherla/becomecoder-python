"""
n=int(input())
data=[0 for i in range(n)]


for i in range(n):
    val=int(input())
    data[i]
print(data)
"""


"""
n=int(input())
data=list(map(int,input().split()))

for i in range(n):
    print(data[i],end=" ")
"""
"""
n=int(input())
data=list(map(int,input().split()))

for i in range(n):
    print(i,end=" ")
"""
n=int(input())
data=list(map(int,input().split()))
res=0
for i in range(n):
    res=res+i
print(res)
