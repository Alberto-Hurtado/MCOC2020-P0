from matplotlib import pyplot as plt
import numpy

names = [#"timing_scipy_matmul.txt",
		 #"timing_scipy_matmul_spa.txt",
		 #"timing_scipy_linalg.txt",
		 #"timing_scipy_linalg_spa.txt",
		 "timing_scipy_inv.txt",
		 "timing_scipy_inv_spa.txt"
	]
names_asem = [
		 #"timing_scipy_matmul_asem.txt",
		 #"timing_scipy_matmul_spa_asem.txt",
		 #"timing_scipy_linalg_asem.txt",
		 #"timing_scipy_linalg_spa_asem.txt",
		 "timing_scipy_inv_asem.txt",
		 "timing_scipy_inv_spa_asem.txt"
		 ]

N0=10000


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
		dt0=i[1]
	plt.subplot(2,1,1)
	plt.loglog(N,dt,"-o",label=name)
	plt.ylabel("Tiempo solucion")
	plt.xlabel("Tamaño matriz")
	plt.grid(True)
	xticks=[10,20,50,100,200,500,1000,2000,5000,10000,30000]
	plt.xticks(xticks,xticks)
	plt.yticks([1e1,1e0,1e-3,1e-6,1e-5,1e-2,1e-1,1e-4],["10 s","1 s","1 ms","1 us","10 us","10 ms","0.1 s","0.1 ms"])
x=numpy.linspace(10000,1)
plt.loglog(x,dt0*x**0,'--',label="Constante")
plt.loglog(x,(dt0/ N0**2)*x**2,'--',label="O(N2)")
plt.loglog(x,(dt0/ N0**3)*x**3,'--',label="O(N3)")
plt.loglog(x,(dt0/ N0**4)*x**4,'--',label="O(N4)")
plt.loglog(x,(dt0/ N0**5)*x**5,'--',label="O(N5)")
for name in names_asem:
	#Leer archivos de texto
	archivo=open(name)
	datos=numpy.loadtxt(archivo)

	#Traspasar texto a arreglos
	N=[]
	dt=[]
	for i in datos:
		N.append(i[0])
		dt.append(i[1])
		dt0=i[1]
	plt.subplot(2,1,2)
	plt.loglog(N,dt,"-o",label=name)
	plt.ylabel("Tiempo ensamblado")
	plt.xlabel("Tamaño matriz")
	plt.grid(True)
	xticks=[10,20,50,100,200,500,1000,2000,5000,10000,30000]
	plt.xticks(xticks,xticks)
	plt.yticks([1e1,1e0,1e-3,1e-6,1e-5,1e-2,1e-1,1e-4],["10 s","1 s","1 ms","1 us","10 us","10 ms","0.1 s","0.1 ms"])
x=numpy.linspace(10000,1)
plt.loglog(x,dt0*x**0,'--',label="Constante")
plt.loglog(x,(dt0/ N0**2)*x**2,'--',label="O(N2)")
plt.loglog(x,(dt0/ N0**3)*x**3,'--',label="O(N3)")
plt.loglog(x,(dt0/ N0**4)*x**4,'--',label="O(N4)")
plt.loglog(x,(dt0/ N0**5)*x**5,'--',label="O(N5)")
plt.tight_layout()
plt.legend()
#plt.savefig("timing_solve_laplaciana.png")
plt.show()