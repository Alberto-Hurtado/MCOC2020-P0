# MCOC2020-P0
Marca/modelo: Acer Nitro 5 AN515-52

Tipo: Notebook

Año adquisición: 2020

Procesador:

Marca/Modelo: Intel® Core™ i5 - 8300H
Velocidad Base: 2.30 GHz
Velocidad Máxima: 4 GHz 
Numero de núcleos: 4
Humero de hilos: 8
Arquitectura: ?
Set de instrucciones: ?

Tamaño de las cachés del procesador

L1: 256 kB
L2: 1.0 MB
L3: 8.0 MB

Memoria

Total: 8 GB
Tipo memoria: DDR4 SDRAM
Velocidad 2667 MHz
Numero de (SO)DIMM: ?

Tarjeta Gráfica

Marca / Modelo: Nvidia GeForce® GTX 105
Memoria dedicada: Hasta 4GB
Resolución: 1920 x 1080

Disco 1:

Marca: Intel
Tipo: HDD
Tamaño: 932 GB
Particiones: 1
Sistema de archivos: ?

Dirección MAC de la tarjeta wifi: ?

Dirección IP (Interna, del router): ?

Dirección IP (Externa, del ISP): ?

Proveedor internet: VTR Banda Ancha S.A.

# Desempeño MATMUL

1.- La forma base del grafico adjunto (Grafico 1) no difiere mucho de la del profesor, a diferencia que los procesos evaluados en mi computador, demoran menos en relacion a los del profesor.

2.- Esto puede ser porque cuando hice estos procesos, fuera de los procesos basicos, no habia ningun otro proceso corriendo en el computador.

3.-

4.- Python 3.8

5.- NumPy 1.19.1

6.- Se adjunta imagen del uso de procesadores. (Foto 1)

# Desempeño de INV
1.- Yo creo que el algoritmo usado es el "Método de Newton", ya que es el único que se muestra de forma iterativa, lo que es mucho más eficiente para un computador resolver númericamente.

2.- Incide en la capacidad que tiene cada procesador de almacenar memoria, ya que si la matriz excede el tamaño de memoria del procesador, esta tendrá que ser almacenada en la RAM y si tampoco cabe en la RAM, esta tendría que ser alacenada en el disco duro, lo que haría muchisimo más lento el proceso.

# Entrega 6
Por lo visto en el grafico de desempeño de Ax = b se ve una mejor consistencia y mejor desempeño en el caso que se asume en que la matriz es definida positiva y sobre escribiendo la matriz A (assume_a='pos' , overwrite_a=True).
La diferencia apreciada entre sobre escribir la matriz y no hacerlo, en el caso de la matriz de N=10000, es de casi 1 ms, por lo que podría decir que es una diferencia despreciable con relacion a los otros casos.
Curiosamente en el caso de sobre escribir solo el vector b, el desempeño empeora con relacion a la misma funcion con los parametros predeterminados.

# Entrega 7
1.- El uso de matrices dispersas tiene un claro beneficio sobre las matrices llenas despues de los ~300 elementos, viendose una disminucion en el tiempo requerido para los calculos.

2.- Al ver en mas detalle los graficos, se puede apreciar que son cuadraticamente asintóticos en casi todos los casos. Los casos de linalg.solve o linalg.inv para las matrices llenas se puede apreciar una mayor cercanía con el orden cúbico.

3.- 

4.- 
