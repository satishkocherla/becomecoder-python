"""
def total_marks(n,data):
    res=0
    for i in data:
        res+=i
    return res


n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)

"""
def total_data(n,data):
    data=[]
    ec=0
    oc=0
    for i in data:
        if i%2:
            ec+=1
        else:
            oc+=1
    return ec,oc
n=int(input())
data=list(map(int,input().split()))
total=total_data(n,data)
print(total)
