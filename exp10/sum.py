import numpy as np

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]

res = np.add(arr1,arr2)
print()
print("Sum of two arrays:" , res)
print()

print("sum of elements of the array: ",np.sum(arr1))
print()


mat1 = [[1,2,3],
        [1,2,3]]
print("Square root of two dimensional arrays")
print(np.sqrt(mat1))
print()
print("Sum of each column of a 2d array: ")
print(np.add(mat1,mat1))
print()

print("Sum of each rows of the 2d array: ")
for i in mat1:
    print(np.sum(i))
print()

print("Transpose of a Matrix: ")
print(np.transpose(mat1))