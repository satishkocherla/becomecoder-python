def count_num_fingers(n):
    r=n%8
    if r==0:
        return 2
    if r<5:
        return r
    else:
        return 10-r



n=int(input())
print(count_num_fingers(n))
        
