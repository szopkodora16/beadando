def lnko(a,b):
    if b>a:
        c=a
        a=b
        b=c
    elif a==b:
        return a
    while b>0:
        t=b
        b=a%b
        a=t
    return a
print(lnko(15,35))