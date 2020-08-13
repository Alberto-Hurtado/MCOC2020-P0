from scipy import matrix, rand,linalg
import scipy
import numpy
from time import perf_counter

casos = [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000,
    2000, 5000, 10000]
for casoN in range(11)[1:]:
	dtype="half"
	bits = 16
	archivo=open(f'timing_inv_caso_2_{dtype}_{casoN}.txt','w')
	for N in casos:

		A = numpy.half(numpy.random.rand(N,N))
	
		t1 = perf_counter()
		C = linalg.inv(A, overwrite_a=False)
		t2 = perf_counter()
	
		dt = t2 - t1
		
		size = 2* (N**2) * bits/8 #2 matrices (A,A.I), N**2, 8 Bytes por float -> 8 bits = 1 byte
		#1 KB 10e3 Bytes
		#1 MB 10e6 Bytes
		#1 GB 10e9 Bytes

		string=f'{N} {dt} {size}\n'
		archivo.write(string)
		archivo.flush()
		#A[0,0].name
	archivo.close()
	print(f"Caso n={casoN}")#Microsegundos = us = s/10e6