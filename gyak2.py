import sys
n=int(sys.argv[1])
for i in range(1,n+1):
    s=" "
    for j in range(1,i+1):
        s+=str(j)
        print(s)