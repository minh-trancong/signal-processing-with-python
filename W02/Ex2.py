import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle("Đáp ứng biên độ")
w = np.linspace(0,2*np.pi,100)

# Hệ thứ nhất
z = np.cos(w) - np.sin(w)*1j
H_complex = 1/(1-0.87*z)
H = np.absolute(H_complex)
axs[0].plot(w, H)
axs[0].set_xticks([0, np.pi, np.pi*2])
labels = ['0', '$\pi$', '$2\pi$']
axs[0].set_xticklabels(labels)
# Hệ thứ 2
H2_complex = 1 - z
H2 = np.absolute(H2_complex)
axs[1].plot(w, H2)
axs[1].set_xticks([0, np.pi, np.pi*2])
axs[1].set_xticklabels(labels)
plt.show()
