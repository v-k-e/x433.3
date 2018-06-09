
import numpy as np

# 1. Include a section with your name
_myName = 'Vinodkumar Elangovan'

# 2. Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
A = np.matrix(np.reshape(np.random.random(15), (3,5)))
print('\nInitial content in A:\n', A)

# 3. Find the size and length of matrix A
print('\nSize of A: ', A.shape)
print('Length of A: ', A.size)

# 4. Resize (crop/slice) matrix A to size (3,4)
A = A[:,0:4]
print('\nContent in A after slicing to (3,4):\n', A)

# 5. Find the transpose of matrix A and assign it to B
B = A.T
print('\nContent of B (A transpose):\n', B)

# 6. Find the minimum value in column 1 of matrix B (check the properties of a matrix – ‘B.min()’)
print('\nMinimum value in first column of B: ', B[:,0].min())

# 7. Find the minimum and maximum values for the entire matrix A
print('\nMinimum value in entire A: ', A.min())
print('Maximum value in entire A: ', A.max())

# 8. Create vector X (an array) with 4 random numbers
X = np.random.random(4)
print('\nContent of vector X:\n', X)

# 9. Create a function and pass vector X and matrix A in it
# 10. In the new function multiply vector X with matrix A and assign the result to D
# (note: you may get an error! … think why and fix it. Recall matric manipulation in class!)
def multiplyVectorWithMatrix(vec, mtx):
    # first, make sure we got a vector and matrix as input
    if (vec.ndim == 1) and (mtx.ndim == 2):
        if (vec.shape[0] == mtx.shape[0]):
            product = vec * mtx
        elif (vec.shape[0] == mtx.T.shape[0]):
            # as an alternative, if matrix transpose is suitable, multiply with that
            print("Multiplying vector with the matrix's transpose...")
            product = vec * mtx.T
        else:
            print('Unable to multiply input vector and matrix!')
    else:
        print('Expecting vector and matrix as input!')
        
    return product

print()
D = multiplyVectorWithMatrix(X, A)
print('Content in D (product of vector and matrix):\n', D)

# 11. Create a complex number Z with absolute and real parts != 0
Z = 3 + 4j

# 12. Show its real and imaginary parts as well as it’s absolute value
print('\nComplex number parts - Real: {0}, Imaginary: {1}, Absolute: {2}'.format(Z.real, Z.imag, abs(Z)))

# 13. Multiply result D with the absolute value of Z and record it to C
C = D * abs(Z)
print('\nResult of multiplying D with abs of complex number:\n', C)

# 14. Convert matrix B from a matrix to a string and overwrite B
B = B.__str__()
print("\nB's type is now '" + B.__class__.__name__ + "' and its value is \n" + B)

# 15. Display a text on the screen: ‘Your Name is done with HW2‘
print('\n' + _myName + ' is done with HW2')