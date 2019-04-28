n=int(input("Addj meg egy számot."))
m=int(input("Addj meg egy másik számot."))
for i in range(1,m+1):
    if m%i==0 and n%i==0:
        print(i)