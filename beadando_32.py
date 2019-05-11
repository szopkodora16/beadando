import sys
try:
    n=int(sys.argv[1])
    for i in range(1,n+1):
        s=" "
        for j in range(1,i+1):
            s+=str(j)
        a=s[::-1]
        s+=a[1:]
        print("{:^40}".format(s))
except ValueError:
    print("Nem számot adtál meg!")