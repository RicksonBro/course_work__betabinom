from scipy.stats import betabinom
import matplotlib.pyplot as plt
import numpy as np

f = open('distribution.txt')
line = f.readline()
while line:
    print (line),
    line = f.readline()
f.close()
n, a, b = 10.0, 0.35, 0.35
mean, var, skew, kurt = betabinom.stats(n, a, b, moments='mvsk')

x = np.arange(0, 50, 1)
y = betabinom.pmf(x, n, a, b)
plt.plot(x, betabinom.cdf(x, n, a, b), ms=8, label='betabinom cdf')
plt.xlim([0, 10])
plt.plot(x, betabinom.pmf(x, n, a, b), ms=8, label='betabinom pmf')

print("Distribution : \n", x)
plt.show()