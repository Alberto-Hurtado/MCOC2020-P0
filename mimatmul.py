from numpy import *

def mimatmul(A,B):
	C=zeros((len(A),len(A[0])))

	Xdim=len(A[0])
	Ydim=len(B[0])

	for i in range(Xdim):
		for j in range(Ydim):
			for r in range(Xdim):
				C[i][j] += A[i][r]*B[r][j]
	return C