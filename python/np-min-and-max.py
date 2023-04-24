import numpy as np

n, m = [int(x) for x in input().strip().split()]
#array = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])

coms = []

for x in input().strip().split() : 
    int(x)
for _ in range(n):

      
    coms.append([int(x)])

arr=np.array(coms)
print(np.max(np.min(arr, axis = 1)))

