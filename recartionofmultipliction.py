"""
def mul(a,b):
    if a==0:
        return 0
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return mul(a//2,b*2)





a,b=map(int,input().split())
print(mul(a,b))
        
 """


"""
def fib(a,b,d,num):
    if d>num:
        return
    if d==1:
        print(a,end=" ")
    if d==2:
        print(b,end=" ")
        d+=1
    print(a+b,end=" ")
    fib(b,a+b,d+1,num)




num=int(input())
fib(0,1,1,num-1)
    
"""


def fib(a,b,i,num):
    if i>num:
        return
    if i==1 and i<=num:
        print(a,end=" ")
        i+=1
    if i==2 and i<=num:
        print(b,end=" ")
        i+=1
    #if i<=num:
    print(a+b,end=" ")
    fib(b,a+b,i+1,num)




num=int(input())
fib(0,1,1,num)
    
