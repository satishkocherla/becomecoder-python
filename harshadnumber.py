def harshad(n):
    a=n
    s=0
    while n:
        r=n%10
        n=n//10
        s=s+r
    if a%s==0:
        return True
    return False
n=int(input())
print(harshad(n))
