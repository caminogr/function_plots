import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()


A = fig.add_subplot(1, 2, 1)
A.grid(color="k", linestyle="dotted")
A.set_title("A", fontsize=16)
A.set_xlabel("x", fontsize=4)
A.set_ylabel("y", fontsize=14)

B = fig.add_subplot(1, 2, 2)
B.grid(color="k", linestyle="dotted")
B.set_title("B", fontsize=16)
B.set_xlabel("x", fontsize=4)
B.set_ylabel("y", fontsize=14)


x = np.arange(-1, 1, 0.01)
rand = random_values = np.array([np.random.default_rng(
    seed=abs(int(val*100))).random() for val in x])

y1 = rand * 0.8 * np.exp(-1 * x)
y2 = rand * 0.8 * np.exp(-4 * x)

print(random_values)


A.plot(x, y1)
B.plot(x, y2)
plt.show()
