import numpy as np

print(np.zeros(10))

print(np.zeros((3,6)))


a = np.array([0,1])
b = np.array([2,3])

ab = np.stack((a,b))

print(np.stack((a,b)))
print(np.stack((a,b)).T)

ab = np.hstack((a,b))
print(ab)
