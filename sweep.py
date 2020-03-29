import time
import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())
import numpy as np
start_time = time.time()
n=int(input('N = '))
a=[0]*(n-1)
c=[0]*(n-1)
b=[0]*n
f=[0]*n

for i in range(n-1):
   	c[i]=int(input('Input C[%i] '%i))
for i in range(n-1):
   	a[i]=int(input('Input A[%i] '%i))
for i in range(n):
	b[i]=int(input('Input B[%i] '%i))
for i in range(n):
   	f[i]=int(input('Input F[%i] '%i))
a, b, c, f = list(map(lambda k_list: list(map(float, k_list)), (a, b, c, f)))
alpha=[0]*n
gamma=[0]*n
beta=[0]*n
phi=[0]*n

gamma[0] = b[0]
alpha[0] = -c[0] / gamma[0]
beta[0] = f[0] / gamma[0]
x = [0.0]*n

for i in range (1, n-1):
	gamma[i] = b[i] + a[i - 1] * alpha[i - 1]
	alpha[i] =-c[i] / gamma[i]
	beta[i] = (f[i] - a[i - 1] * beta[i - 1]) / gamma[i]
	
gamma[n - 1] = b[n- 1] + a[n - 2] * alpha[n - 2]
beta[n - 1] = (f[n - 1] - a[n- 2] * beta[n- 2]) / gamma[n- 1]

x[n - 1] = beta[n - 1]

for i in reversed(range(0,n-1)):
	x[i] = alpha[i] * x[i + 1] + beta[i]
x[0] = alpha[0] * x[1] + beta[0]

for i in range(n):
	print('x[%i] = %f' % (i, x[i]))


phi[0] = f[0] - b[0]*x[0] - c[0]*x[1]
print('Residual: %f' %phi[0])

for i in range(1,n-1):
	#for j in range (i,i+3)
	phi[i] = f[i] - b[i]*x[i] - c[i]*x[i+1] - a[i-1]*x[i-1]
	print('Residual: %f' %phi[i])

phi[n-1] = f[n-1] - a[n-2]*x[n-2] - b[n-1]*x[n-1]
print('2^Residual: %f' %(2**phi[n-1])

print("--- %s seconds ---" % (time.time() - start_time))

