import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(3)
fig.suptitle("Convolution")
# Vẽ x(n)
n = np.arange(-9,10,1)
print("n: ",n)
u = 1 * (n>=0)
x = np.power(0.8,n)*u
axs[0].set_title('x(n)')
axs[0].stem(n,x)
print(x)
# Vẽ h(n)
h = u
axs[1].set_title('h(n)')
axs[1].stem(n,h)
print(h)
# Vẽ y(n)
y = np.convolve(x,h,'same')
print(y)
axs[2].set_title('y(n)')
axs[2].stem(n,y)
plt.show()
