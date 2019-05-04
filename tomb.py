import numpy as np
try:
    n=int(input("adj meg egy számot."))
    ls=[]
    while n!=0:
        ls.append(n)
        n=int(input("adj meg egy számot."))
    tomb=np.array(ls)
    print(tomb)

except ValueError:
    print("Nem szám.")