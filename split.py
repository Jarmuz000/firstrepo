import numpy as np
import random as rand
tab1=np.array([[0,0,0],[0,0,0],[0,0,0]])
for x in range(3):
    for y in range(3):
        tab1[x][y]=rand.randint(0,10)
for y in range(3):
    for x in range(3):
         print(int(tab1[y][x]))
print()
for x in range(3):
       print(int(tab1[0][x]),int(tab1[1][x]),int(tab1[2][x]))
       print()
