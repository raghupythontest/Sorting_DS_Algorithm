def toh(n,a,b,c):
    if n>0:
        toh(n-1,a,c,b)
        print(f"from {a} to {c}")
        toh(n-1,b,a,c)
toh(2,a='a',b='b',c='c')