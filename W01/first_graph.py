import matplotlib.pyplot as plt
import math

# Xung đơn vị
n = range(-5, 6, 1)
y = []
for i in n:
    tmp = (1 if i==0 else 0)
    y.append(tmp)
print(n)
print(y)
#Vẽ đồ thị
plt.title('Xung đơn vị')
plt.xlabel('n')
plt.ylabel('δ(n)')
plt.stem(n, y)
plt.show()

#Tín hiệu bậc đơn vị
un = []
for i in n:
    tmp = (1 if i>=0 else 0)
    un.append(tmp)
print(un)
plt.title('Tín hiệu bậc đơn vị')
plt.xlabel('n')
plt.ylabel('u(n)')
plt.stem(n, un)
plt.show()

#Tín hiệu hàm mũ
en = []
a = 0.5
for i in n:
    tmp = a**i
    en.append(tmp)
print(en)
plt.title('Tín hiệu hàm mũ')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.stem(n, en)
plt.show()

#Tín hiệu tuần hoàn
xn = []
N = 6
n = range(30)
n0 = 3
for i in range(len(n)):
    tmp = math.sin(2*math.pi*(i+n0)/N)
    xn.append(tmp)
print(xn)
plt.title('Tín hiệu tuần hoàn')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.stem(n, xn)
plt.show()