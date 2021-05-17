n=int(input())
sum=0
k=0
n=k

while n!=0:
    r=n%10
    sum=sum+(r*10)
    n=n//10
if n==k:
    print("palindrome")
else:
    print("not palindrome")
