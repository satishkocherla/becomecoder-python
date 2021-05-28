n=int(input())
t=1
for i in range(1,n+1):
    for k in range(1,n+1):
        print(t,end=" ")
        if t==0:
            t==1
        else:
            t==0
    print()
