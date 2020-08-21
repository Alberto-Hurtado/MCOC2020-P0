from scipy import matrix, rand,sparse, linalg
from matriz_laplaciana import matriz_laplaciana
from matriz_laplaciana_sparse import matriz_laplaciana_sparse
from scipy.sparse import linalg as splinalg
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
    2000, 5000, 10000, 30000]

names = ["timing_scipy_matmul.txt",
		 "timing_scipy_matmul_spa.txt",
		 "timing_scipy_linalg.txt",
		 "timing_scipy_linalg_spa.txt",
		 "timing_scipy_inv.txt",
		 "timing_scipy_inv_spa.txt"
	]
names_asem = ["timing_scipy_matmul_asem.txt",
		 "timing_scipy_matmul_spa_asem.txt",
		 "timing_scipy_linalg_asem.txt",
		 "timing_scipy_linalg_spa_asem.txt",
		 "timing_scipy_inv_asem.txt",
		 "timing_scipy_inv_spa_asem.txt"
		 ]
files = [open(name,"w") for name in names]
files_asem = [open(name,"w") for name in names_asem]

Ncorridas=10

for N in casos:
	print(f"N= {N}")
	dts=numpy.zeros((Ncorridas,len(files)))
	dts_asem=numpy.zeros((Ncorridas,len(files)))
	for casoN in range(Ncorridas):
		print(f"i = {casoN}")

		#Scipy A@B llena
		t1_asem=perf_counter()
		A = matriz_laplaciana(N,dtype=numpy.double)
		B = matriz_laplaciana(N,dtype=numpy.double)
		t2_asem=perf_counter()
	
		t1 = perf_counter()
		C=A@B
		t2 = perf_counter()
		dts[casoN][0] = t2 - t1
		dts_asem[casoN][0] = t2_asem - t1_asem

		#scipy A@B sparse
		t1_asem=perf_counter()
		A = matriz_laplaciana_sparse(N,dtype=numpy.double)
		B = matriz_laplaciana_sparse(N,dtype=numpy.double)
		t2_asem=perf_counter()
	
		t1 = perf_counter()
		C=A@B
		t2 = perf_counter()
		dts[casoN][1] = t2 - t1
		dts_asem[casoN][1] = t2_asem - t1_asem

		#linalg.solve(A,b)
		t1_asem=perf_counter()
		A = matriz_laplaciana(N,dtype=numpy.double)
		b= numpy.ones(N)
		t2_asem=perf_counter()
	
		t1 = perf_counter()
		X = linalg.solve(A,b)
		t2 = perf_counter()
		dts[casoN][2] = t2 - t1
		dts_asem[casoN][2] = t2_asem - t1_asem

		#SciPy solve sparse
		t1_asem=perf_counter()
		A = matriz_laplaciana_sparse(N,dtype=numpy.double)
		b= numpy.ones(N)
		t2_asem=perf_counter()
	
		t1 = perf_counter()
		X = splinalg.spsolve(A,b)
		t2 = perf_counter()
		dts[casoN][3] = t2 - t1
		dts_asem[casoN][3] = t2_asem - t1_asem

		#SciPy inv A
		t1_asem=perf_counter()
		A = matriz_laplaciana(N)
		t2_asem=perf_counter()
	
		t1 = perf_counter()
		X = linalg.inv(A)
		t2 = perf_counter()
		dts[casoN][4] = t2 - t1
		dts_asem[casoN][4] = t2_asem - t1_asem

		#SciPy inv A sparse
		t1_asem=perf_counter()
		A = matriz_laplaciana_sparse(N)
		t2_asem=perf_counter()
	
		t1 = perf_counter()
		X = splinalg.inv(A)
		t2 = perf_counter()
		dts[casoN][5] = t2 - t1
		dts_asem[casoN][5] = t2_asem - t1_asem


		[name.flush() for name in files]
		[name_asem.flush() for name_asem in files_asem]
		#print(dts[casoN])

	dts_mean=[numpy.mean(dts[:,j]) for j in range(len(files))]
	[files[i].write(f"{N} {dts_mean[i]}\n") for i in range(len(files))]
	dts_mean_asem=[numpy.mean(dts_asem[:,j]) for j in range(len(files_asem))]
	[files_asem[i].write(f"{N} {dts_mean_asem[i]}\n") for i in range(len(files_asem))]
[name.close() for name in files]
[name.close() for name in files_asem]