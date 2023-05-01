import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()


A = fig.add_subplot(1, 2, 1)
A.grid(color="k", linestyle="dotted")
A.set_title("np.sin(2*x)", fontsize=8)
A.set_xlabel("x", fontsize=4)
A.set_ylabel("y", fontsize=14)

B = fig.add_subplot(1, 2, 2)
B.grid(color="k", linestyle="dotted")
B.set_title("np.exp(np.sin(2*x))", fontsize=8)
B.set_xlabel("x", fontsize=4)
B.set_ylabel("y", fontsize=14)


x = np.arange(0, 100, 0.01)

y1 = np.sin(2*x)
y2 = np.exp(np.sin(2*x))


A.plot(x, y1)
B.plot(x, y2)
plt.show()
