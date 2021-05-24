"""
n=int(input("enter the number:"))
sum=0
for i in range(1,n):
      if n%i==0:
          sum=sum+i 
if sum==n:
      print("perfect number")
else:
    
      print("not perfect number")




"""



"""
def isperf(num):
      s=0
      for i in range(1,num):
            if num%i==0:
                  s+=i
      return s==num



num=int(input())
print(isperf(num))
"""


import math as m


def isperfect(n):
      res=1
      s=int(m.sqrt(n))
      for i in range(1,s+1):
            
      
