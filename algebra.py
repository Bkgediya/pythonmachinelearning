a = [1,2,3,7]

print("a :",a)

A = [[1,2,3,4],
     [5,4,-9,6],
     [1,-2,7,6]]


print("A :",A)

import numpy as np

a = np.array([1,3,7,2])
print("a => ",a)


A = np.array([[1,2,3,4],
        [5,4,-9,6],
        [1,-2,7,6]])

print("A :",A)


a1 =  np.array([[0,1],[-2,-3]])

a2 =  np.array([[0,1],[-2,-3]])

c = a1+a2
print(c)

dot = a1.dot(a2)
print(dot)

trans = A.transpose()
print(trans)


#Vectors
#=========

print(np.array([1,2,3,4]))


#matrix
#======


print(np.matrix([[1,2,3],[4,5,6]]))


#linear algebra (numpy.linalg)

#Matrix Addition
A = np.matrix([[0,1],[-2 ,-3]])

B = np.matrix([[1,0 ],[3,-2]])
c = A + B
print("matrix addition is :",c)


#substraction
A = np.matrix([[0,1],[-2 ,-3]])

B = np.matrix([[1,0 ],[3,-2]])

C = A - B
print("And the substration is : ",C)

#matrix multiplication

A = np.matrix([[0,1],[-2 ,-3]])

B = np.matrix([[1,0 ],[3,-2]])

C = A * B

print("And the multiplication is \n: ",C)

#Transpose
np.transpose(A)

#determinant
#for determinant we need to import linalg from numpy


import numpy.linalg as la

A = A = np.matrix([[1,2],[3 ,4]])
Adet = la.det(A)

print("Deteminant of A is \n",Adet)


A = A = np.matrix([[1,2],[3 ,4]])
Ainverse = la.inv(A)

print("Inverse of A is \n",Ainverse)

#solving the linear equation for square matrix

A = np.matrix([[1,2],[3 ,4]])
b = np.array([[5],[6]])

x = Ainverse.dot(b)
print("The solve of linear equatino : \n",x)

x = np.linalg.solve(A,b)
print("The solve of linear equatino : \n",x)




#solving least-squares best “solution” of the system/equation for non square matrix

A = np.array([[1,2] ,
 [3,4],
[7,8]])

b = np.array([[5],[6],[9]])

x = np.linalg.lstsq(A,b,rcond= None)[0]
print(x)

A = np.matrix([[0,1],[-2 ,-3]])

B = np.matrix([[1,0 ],[3,-2]])

c = np.add(A,B)
print("np.add \n",c)

A = np.matrix([[0,1],[-2 ,-3]])

B = np.matrix([[1,0 ],[3,-2]])

c = np.multiply(A,B)
print("np.multiply \n",c)
