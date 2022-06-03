from scipy.signal import freqz
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.grid'] = True

fig, axs = plt.subplots(5)
plt.subplots_adjust(hspace=0.75)

N = 1024
t = np.linspace(0,1.1,N)
Fs = 1000
n = t*Fs
x = 4 + np.cos(250*np.pi*t - np.pi/4) - 3*np.cos((2000*np.pi)/3 * t)
axs[0].plot(t,x,linewidth=0.75)
axs[0].set_title('Input signal')

# Tính phổ
X = np.fft.fft(x, N)
X.resize(512)
w = np.linspace(0,np.pi,512)
axs[1].plot(w,abs(X))

b = [1,1,1]
a = [3,0,0]
w, H = freqz(b,a)
f = w/(2*np.pi)
axs[2].plot(w,abs(H))

y = signal.lfilter(b, a, x)
axs[3].plot(t,y)


plt.show()