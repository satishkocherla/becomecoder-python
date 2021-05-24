"""
n=int(input())#153
s=0
temp=n#153
while temp:#153   #15   #1
    digit=temp%10#3   #5   #1
    s=s+digit**3#0+3**3   #27+5**3   #152+1**3
    temp=temp//10#15   #1   #0

if s==n:
    print("is a armstrong number")
else:
    print("is not a armstrong number")
"""



def armstrong(n):
    temp=n
    dc=0
    while temp:
        r=n%10
        n=temp//10
        dc+=1
    print(dc)




n=int(input())
