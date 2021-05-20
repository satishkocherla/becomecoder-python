def isfib(n):
    if n==0 or n==1:
        return True
    a,b=0,1
    while True:
        c=a+b
        if c==n:
            return True
        if c>n:
            print(b,c)
            if b-n <= c-n:
                print(b,end=" ")
            if b-n >= c-n:
                print(c,end=" ")
            return False
        a=b
        b=c
        

n=int(input())
print(isfib(n))

            
