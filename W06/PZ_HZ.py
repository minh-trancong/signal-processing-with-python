from scipy.signal import tf2zpk
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100)
# x(n) = y(n) - 3y(n-1) + 2y(n-2)
a = [1,-3,2]
b = [1,0,0]
z, p, k = tf2zpk(b,a)
plt.plot(p.real,p.imag,'x')
plt.plot(z.real,z.imag,'o',markerfacecolor='None')
plt.text(0.05,0.05,'2',fontsize=10);
plt.plot(np.cos(x),np.sin(x))
plt.ylim(-3,3)
plt.xlim(-3,3)
plt.grid()
plt.show()