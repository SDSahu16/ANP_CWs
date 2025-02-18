import numpy as np

# Create two matrixces and print their sum,

matrix1 = np.array([[1,2,3],[4,5,6]])
matrix2 = np.array([[2,5,8],[3,7,9]])
print("Addition and Subtraction: \n----------------------------------------")
print("Given Matrices are :\n..................................")
print("Matrix 1 : \n", matrix1)
print("Matrix 2 : \n", matrix2)
print("Sum of the matrices : \n", matrix1 + matrix2)

# calculate difference of two matrices

print("Difference between the matrices: \nMatrix 2 - Matrix 1 = \n", matrix2 - matrix1)
print("----------------------------------------------------------------------")

# calculate product of two matrices

matrix3 = np.array([[1,2,3],[2,3,6]])
matrix4 = np.array([[9,2],[8,6],[7,3]])
print("Multiplication\n---------------------")
print("Given matrices for the Product operation are : \n..................................................")
print("Matrix 3 : \n", matrix3)
print("Matrix 4 : \n", matrix4)
print("Product of matrix1 with matrix2 : \n", np.dot(matrix3,matrix4))