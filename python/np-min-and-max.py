import numpy as np


n, m = [int(x) for x in input().strip().split()]

print(n, m)

for _ in range(n):
    x = [int(input().strip().split())]
arr = np.array(x)
print(arr)
#array = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])
#print(np.max(np.min(array, axis = 1)))