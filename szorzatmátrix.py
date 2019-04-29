
import numpy as np
n=np.random.randint(1,5,(2,4))
m=np.random.randint(1,5,(4,3))
print(n)
print(m)
for i in range(0,n.shape[0]):
    for j in range(0,n.shape[1]):
        print(n[i,j])

