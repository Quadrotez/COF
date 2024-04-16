def series(n):
    s = 0
    while n!=0:
        s+=n*(n-1)
        n-=1
    return s