def bitwise(n):
    s=0
    while s<=n:
        s<<=1
    return(s-1)^n
