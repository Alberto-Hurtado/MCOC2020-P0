from matplotlib import pyplot as plt
import numpy

names = ["timing_Ainv_b.txt","timing_npSolve.txt"]


for name in names:
	#Leer archivos de texto
	archivo=open(name)
	datos=numpy.loadtxt(archivo)

	#Traspasar texto a arreglos
	N=[]
	dt=[]
	for i in datos:
		N.append(i[0])
		dt.append(i[1])
	plt.loglog(N,dt,"-o",label=name)
	plt.ylabel("Tiempo transcurrido (s)")
	plt.xlabel("Tamaño matriz")
	plt.grid(True)
	plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000],[10,20,50,100,200,500,1000,2000,5000,10000])
	plt.yticks([10e1,10e0,10e-3,10e-6,10e-5,10e-2,10e-1,10e-4],["10 s","1 s","1 ms","1 us","10 us","10 ms","0.1 s","0.1 ms"])
plt.tight_layout()
plt.legend()
plt.savefig("timing_solve_laplaciana.png")
plt.show()