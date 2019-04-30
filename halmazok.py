import random
x=set(range(0,37))
x.add("00")
print(x)
ls=[]
for i in x:
    ls.append(i)
print(ls)
x=random.choice(ls)
print(x)
if x%2==0:
    print("E")
if x%2!=0:
    print("O")
piros={1,3,5,7,9,12,14,16,18,19,21,22,25,27,30,32,34,36}
if x in piros:
    print("R")
else:
    print("B")
if x>=0 and x<=18:
    print("S")
else:
    print("G")
