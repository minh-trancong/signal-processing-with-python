import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
# Tín hiệu sin rời rạc hóa
n = np.arange(0,512,1)
F = 300
x = np.sin(2*np.pi*F*n/1500)
axs[0].plot(n,x)

# Phổ biên độ
X = [0]*512
for f in range(512):
    X[f] = 0
    for i in n:
        X[f] += x[i] * np.exp(-1j*2*np.pi*f*i/1500)
    X[f] = np.absolute(X[f])
axs[1].plot(n,X)
freq = np.arange(0,512,1)
Y = np.array([np.abs(np.sum(x * np.exp(-1j*2*np.pi*f*n/1500))) for f in freq])
axs[1].plot(n,Y)
plt.grid()
plt.show()