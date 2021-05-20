def isfib(n):
    if n==0 or n==1:
        return True
    a,b=0,1
    f=0
    while True:
        c=a+b
        a=b
        b=c
        f+=1
        if c==n:
            break
            print(f)
        if c>n:
            return False
        a=b
        b=c
        
        print(f)

n=int(input())
print(isfib(n))

            
