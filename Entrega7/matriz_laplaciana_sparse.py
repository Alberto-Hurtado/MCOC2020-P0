import numpy as np
from scipy import sparse as spa
def matriz_laplaciana_sparse(N,dtype=np.float32):
	e =  spa.eye(N,N,dtype=dtype) - spa.eye(N,N,1,dtype=dtype)
	return e+e.T
