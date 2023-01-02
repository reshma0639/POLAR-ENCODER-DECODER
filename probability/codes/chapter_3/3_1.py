import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # diagonal covariance
A = 5
A1=10**(0.1*A);
x=np.linspace(-10,10,10)
simlen = int(5000)
n1, n2 = np.random.multivariate_normal(mean, cov, simlen).T
values = [-1, 1]
probabilities = [0.5, 0.5]
X=np.random.choice(values, simlen, p=probabilities)
print(X);
y1 = A1*X+n1
print(y1)
plt.scatter( X, y1)
plt.legend(['$\mathbf{x} = \mathbf{s}_0$','$\mathbf{x} = \mathbf{s}_1$'])
plt.xlabel("$y_1$")
plt.ylabel("$y_2$")
plt.savefig('/home/mannava/latex/3.pdf')
plt.axhline(y = 0, color = 'b', linestyle = '-')
plt.show()
