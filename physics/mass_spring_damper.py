# reference https://haizairenmei.com/2019/11/11/mass-spring-damper/

import matplotlib.pyplot as plt

gx = []
gt = []

dt = 0.1
k = 0.3			# spring constant
m = 1.0  # mass
c = 0.1  # damping coefficient

x = 0.1  # displacement
v = 0			# velocity
for i in range(int(100/dt)):
    t = i*dt # tをdtずつ増加

    x += dt*(v)  # xをdxずつ増加
    v += dt/m*(-k*x - c*v)  # vをdvずつ増加

    gx.append(x)
    gt.append(t)

plt.plot(gt, gx)
plt.title('mass spring damper')
plt.xlabel('time')
plt.ylabel('x')

plt.show()
