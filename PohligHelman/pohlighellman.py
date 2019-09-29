#! /usr/bin/python
from functools import reduce
from math import log2, ceil
import time
mask1 = mask2 = polyred = None

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)
 
def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m
	
def crt(m, x):
 
    while True:
         
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] + \
                modinv(m[0],m[1]) * x[1] * m[0]
		
        temp2 = m[0] * m[1]
 
        
        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x 
 
        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m
 
        
        if len(x) == 1:
            break

    return x[0] # returns the remainder of the final equation

def addGF2(a,b):
	y = int(a,2) ^ int(b,2)
	return ('{0:b}'.format(y))
	
def setGF2(degree, irPoly):
    def i2P(sInt):
        """Konvertuje integer na binarne cislo (reprezentacia polynomu)"""
        return [(sInt >> i) & 1
                for i in reversed(range(sInt.bit_length()))]    
    
    global mask1, mask2, polyred
    mask1 = mask2 = 1 << degree
    mask2 -= 1
    polyred = reduce(lambda x, y: (x << 1) + y, i2P(irPoly)[1:])
		
def multGF2(p1, p2):
	"""Multiply two polynomials in GF(2^m)/g(x)"""
	p = 0
	while p2:
		if p2 & 1:
			p ^= p1
		p1 <<= 1
		if p1 & mask1:
			p1 ^= polyred
		p2 >>= 1
    
	return p & mask2	

def powerGF2(a,x):
	tmp=a
	result=1
	for i in range(ceil(log2(x) + 1)):
		if x & (1 << i):				
			result=multGF2(result, tmp) #result*=tmp
		tmp=multGF2(tmp, tmp)			#tmp=tmp**2
	
	return result
	
def PohligHellman(h, g, p,N,factorized_N):
	gl = [None]	* 12
	gh = [None] * 12
	table=[None] * 12
	tmp=[None] * 12
	j=0
	for i in factorized_N:
		q=i[0] 
		e=i[1]
		gl[j]=powerGF2(g,int((p-1)//pow(q,e,p)))
		gh[j]=powerGF2(h,int((p-1)//pow(q,e,p)))
		j+=1
	
	for i in range(0,len(factorized_N)):
		for a in range(1,p):
			if powerGF2(gl[i],a) == gh[i]:
				table[i]=a
				break
	
	j=0
	for i in factorized_N:	
		tmp[j]=i[0]**i[1]
		j+=1
	#print (table)
	#print (tmp)
	
	return crt(tmp,table)
	
	
if __name__ == "__main__":		
	gf2=1267650600228229401496703205765 #ireducibil polynom x^100 + x^8 + x^7 + x^2 + 1
	p=1267650600228229401496703205376 #2^100 
	N=p-1
	h=85425972786982054230523658528 # polynom x^96+x^92+x^90 +......
	factorized_N=[[3,1], [5,3], [11,1], [31,1], [41,1], [101,1], [251,1], [601,1], [1801,1], [4051,1], [8101,1], [268501,1]] #factorized 2^100 - 1
	setGF2(100, gf2) # Define binary field GF(2^100)/x^100 + x^8 + x^7 + x^2 + 1
	#print(bin(multGF2(0b1101, 0b1101)))
	start = time.time()
	result=PohligHellman(h,0b10,p,N,factorized_N) 
	end = time.time()
	print ("Finded expencial x= %d" % result)
	print ("h(x)=%d" % powerGF2(0b10,result))
	print ("Time elapsed %f" % (end-start))

