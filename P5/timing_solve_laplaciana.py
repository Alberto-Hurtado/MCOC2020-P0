from scipy import matrix, rand,linalg
from matriz_laplaciana import matriz_laplaciana
import numpy
from time import perf_counter

casos = [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000]
    #2000, 5000, 10000]

names = ["timing_Ainv_b.txt","timing_npSolve.txt"]
files = [open(name,"w") for name in names]

Ncorridas=5

for N in casos:
	dts=numpy.zeros((Ncorridas,len(files)))
	for casoN in range(Ncorridas):

		#A invertido @ b
		A = matriz_laplaciana(N)
		b= numpy.ones(N)
	
		t1 = perf_counter()
		C = linalg.inv(A)
		X=C@b
		t2 = perf_counter()
		dts[casoN][0] = t2 - t1
		#files[0].write(f'{N} {t2 - t1}\n')

		#scipy.solve(A,b)
		A = matriz_laplaciana(N)
		b= numpy.ones(N)
	
		t1 = perf_counter()
		X = linalg.solve(A,b)
		t2 = perf_counter()
		dts[casoN][1] = t2 - t1
		#files[1].write(f'{N} {t2 - t1}\n')

		[name.flush() for name in files]

	dts_mean=[numpy.mean(dts[:][j]) for j in range(len(files))]
	[files[i].write(f"{N} {dts_mean[i]}\n") for i in range(len(files))]
[name.close() for name in files]