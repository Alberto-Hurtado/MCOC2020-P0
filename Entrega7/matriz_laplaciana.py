import numpy as np
def matriz_laplaciana(N,dtype=np.float32):
	e =  np.eye(N,N,dtype=dtype) - np.eye(N,N,1,dtype=dtype)
	return e+e.T
