#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 21:08:55 2018

@author: brianhumphreys
"""

#import flint as ft
import numpy as np

'''
These are the functions that I personally wrote and tested 
'''
#inputs a negative number and modulus p. Converts negative to corresponding positive value in mod p space
def convert_neg(neg, p):
    if neg < 0:
        
        neg = abs(neg)
        
        neg = neg % p
        
        return p - neg
    else:
        return neg
    
def multiply_mod_neg_one(num, p):
    return p - num
#############################################
#            MATRICIES AAAAAAA              #
############################################


#Inputs : Numpy matrix - A, integer modulus p 
#Output : Numpy matrix - A^-1 (A inverse)
def create_inverse(in_matrix, p):
    #returns (m, n) tuple of matrix with (m x n) dimmensions
    x_dim, y_dim = in_matrix.shape

    #checks if the matrix is square, if not, exit
    if x_dim != y_dim:
        raise Exception("Non-square matrix is non-invertible")

    #real code to create inverse
    else:
        identity_mat = np.identity(x_dim)
        identity_mat = np.array(identity_mat)
        print(identity_mat)
        identity_mat.astype(int)
        print(in_matrix)
        
    #perform RREF operations in a modular space
    for x in range(x_dim):
        #find mod inverse to
        
        print("==================\n", "diag: ", x, "\n=====================")
        scalar = modinv(in_matrix[x][x], p)
        
        in_matrix[x] = (in_matrix[x] * scalar) % p
        identity_mat[x] = (identity_mat[x] * scalar) % p
        
        
        for y in range(y_dim):
            
            
            
            # row reduction operation 
            if (x != y) and (in_matrix[y][x] != 0):
                
                
                print("------------------------\n", "position: ", x, y, "\nbefore negative:", in_matrix[y], "\n")
                
                reductor_scalar = multiply_mod_neg_one(in_matrix[y][x], p) 
                
                print("negative value:", reductor_scalar,"\n")
                
                print("Before operation:\n", in_matrix, "\n")
                
                print("\n", (in_matrix[x] * reductor_scalar) % p, "\n")
                in_matrix[y] = (in_matrix[y] + ((in_matrix[x] * reductor_scalar) % p)) % p
                identity_mat[y] = (identity_mat[y] + ((identity_mat[x] * reductor_scalar)% p)) % p
                
                print("After operation:\n", in_matrix, "\n")
                
    print(identity_mat)
                
    
                
                
                
            
        
        
        


#def perform_operation()
    

'''
Stack overflow functions that implement basic number theory programs
'''

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    

def modinv(a, m):
    if a < 0:
        a = convert_neg(a)
    g, x, y = egcd(a, m)
    if g != 1:
        print ("g is : ", g)
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def matrix_cofactor(matrix):
    C = np.zeros(matrix.shape)
    nrows, ncols = C.shape
    for row in range(nrows):
        for col in range(ncols):
            minor = matrix[np.array(list(range(row))+list(range(row+1,nrows)))[:,np.newaxis],
                           np.array(list(range(col))+list(range(col+1,ncols)))]
            C[row, col] = (-1)**(row+col) * np.linalg.det(minor)
    return C

### ---------- TESTING ---------- ###

#test = convert_neg(-20, 101)
#modinv(-20, 101)
#modinv(test, 101)

my_mat = np.array([[1, 0, 2, 1],
                   [1, 1, 1, 0],
                   [0, 1, 2, 1],
                   [1, 0, 1, 2]])
print(np.linalg.det(my_mat))

x = np.array([[1,2,3],
              [4,5,6],
              [8,9,3]])




create_inverse(my_mat, 2017)
#convert_neg()


'''
matrix = np.array([[5, 3], [-3, 5]])

matrix_cofactor = matrix_cofactor(matrix)
print("cofactor: ", matrix_cofactor)
print("determinant: ", np.linalg.det(matrix))
print("det inv: ", modinv(np.linalg.det(matrix), 101))

inverse = modinv(np.linalg.det(matrix), 101) * matrix_cofactor

print(inverse)'''

