#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 18:03:55 2018

@author: brianhumphreys
"""

import math
import random
import modular
import numpy as np
from sympy import sieve



#set values
prime = 2017
g = 5
#y = 8500
#a = 7
#b = 31
#aPC = []
#bPC = []
#aval = 0
#bval = 0
#expList = []
#primeCountMatrix = []

#set empty prime list
S = [2,3,7,9,11,]

def set_s(largestPrime, base):
    primeList = sieve.primerange(2, largestPrime+1)
    if base in primeList:
        primelist.remove(primeList.index(base))
    
    
#function for finding a list of prime factors
def getPrimeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
        
def isSmooth(n):
    
    #1 cannot be smooth
    if n == 1:
        return False
    
    #get a list of prime factors to check smoothness with
    factors = getPrimeFactors(n)
    
    #check to see if smooth
    for i in range(len(factors)):
        if factors[i] not in S:
            return False
    return True

def countPrimeFactors(n):
    
    #initialize list with zeros
    primeCount = []
    for i in range(len(S)):
        primeCount.append(0)
        
    #add number of each primes into primeCount indexes
    for i in range(len(n)):
        if n[i] in S:
            primeCount[S.index(n[i])] += 1
    return primeCount
            

def generateSmoothAlpha(expList):
    smooth = False
    uniqueExp = True
    
    x = 0

    while ( (not smooth) and uniqueExp):
        uniqueExp = False
        
        #randomly generate unique exponent
        x = random.randint(1, prime)
        if x not in expList:
            uniqueExp = True
        
        #check if value obtained from exp is smooth
        y = pow(g, x) % prime
        smooth = isSmooth(y)
    
    #print(y)
    return x, y
        
#main code
def buildMatrix():
    expList = []
    primeCountMatrix = []
    for i in range(len(S)): 
        
        #get list of exponents
        exponent, g_to_the_x = generateSmoothAlpha(expList)
        
        expList.append(exponent)
        #print(expList)
        
        #get lists of prime counts then input into matrix
        
        primelist = getPrimeFactors(g_to_the_x)
        matrow = countPrimeFactors(primelist)
        primeCountMatrix.append(matrow)
        #print("Matrix: \n", primeCountMatrix)
    return primeCountMatrix
    

def isMatrixDependent(matrix):
    
    #find determinant
    det = numpy.linalg.det(matrix)
    print ("Matrix Determinant is : ", det)
    
    #if determinant is equal to 0, it is dependent
    if(det == 0):
        return True
    else:
        return False

def findIndependentMatrix():
    dependent = True
    while(dependent):
        matrix = []
        
        matrix = buildMatrix()
        print(matrix)
        dependent = isMatrixDependent(matrix)
        print(dependent)
    
def modularInverseMatrix(in_matrix, p):
    co_factor_matrix = modular.matrix_cofactor(in_matrix)
    co_factor_det    = int(numpy.linalg.det(co_factor_matrix))
    print ("Cofactor determinant is :", co_factor_det)
    mod_inv          = modular.modinv(co_factor_det, p)

    return_matrix    = mod_inv * co_factor_matrix
    print(return_matrix)
    return return_matrix


def prepareForRREF(matrix):
    
    #set identity properties
    identitySize = len(matrix)
    fieldMatrix = []
    
    for i in identitySize:
        
        for j in identitySize:
            fieldMatrix.append(matrix[i][j])
            
        for j in identitySize:
            if i == j:
                fieldMatrix.append(1)
            else:
                fieldMatrix.append(0)
                
    print(fieldMatrix)
    return fieldMatrix
        
        
        
'''
print("beginning")
#findIndependentMatrix()



matrix = np.array([[1, 0, 2, 1],
                  [1, 1, 1, 0],
                  [0, 1, 2, 1],
                  [1, 0, 1, 2]])

y = np.array([130, 1874, 1130, 1874])

#modularInverseMatrix(matrix, prime)
print(numpy.linalg.det(matrix_cofactor(matrix)))'''


    


    
    
    
    


'''      
DLP = True
while(DLP):
    
    DLP = False
    
    #get a value
    #a = random.randint(1,100)
    aval = pow(g,a) % prime
    
    #find the prime factors and add up the quantity of each one
    primeFactorList = prime_factors(aval)
    countPrimeFactors(primeFactorList, aPC)
    
    #check to see if the number is smooth
    for i in range(len(primeFactorList)):
        
        if primeFactorList[i] not in S:
            DLP = True
            print("not smoothe")
            
DLP = True       
while(DLP):
    
    DLP = False
    #b = random.randint(1,100)
    bval = pow(g,b) % prime
    
    primeFactorList = prime_factors(bval)
    countPrimeFactors(primeFactorList, bPC)
    
    
    for i in range(len(primeFactorList)):
        if primeFactorList[i] not in S:
            DLP = True
            print("not smoothe")
   

'''


'''
x = np.array([aPC, bPC])  
y = np.array([a,b])
z = np.linalg.solve(x,y)

print(z)

for i in range(len(z)):
    if z[i] < 0:
        z[i] = z[i] % (prime - 1)

print(z)
'''


  
        
        