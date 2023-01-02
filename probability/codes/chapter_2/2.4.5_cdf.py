
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4,100)   #points on the x axis
print(x)

simlen = int(1e6)    #number of samples
print(simlen)

err = [] #declaring probability list

import subprocess
import shlex
#randvar = np.random.normal(0,1,simlen)

#randvar = np.loadtxt('uni.dat',dtype='double')
#end if

randvar = np.loadtxt('triangle.dat',dtype='double')
print(randvar)


for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
print(err_ind)
print(err_n)
print(err)	
plt.plot(x.T,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
plt.savefig('/home/mannava/latex/triangle_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
