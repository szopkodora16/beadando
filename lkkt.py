def lkkt(a,b):
    if a>b:
        a,b=b,a
    x=0
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            x=i
    return x
print(lkkt(4,6))

