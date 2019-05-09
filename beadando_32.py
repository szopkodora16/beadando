try:
    n=int(input("addj meg egy számot"))
    for i in range(1,n+1):
        s=" "
        for j in range(1,i+1):
            s+=str(j)
        a=s[::-1]
        s+=a[1:]
        print("{:^100}".format(s))
except ValueError:
    print("Nem számot adtál meg")