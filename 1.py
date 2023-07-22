import numpy as np

def star_trace(t, R, r, theta):
    x = (R - r) * np.cos(theta) + r * np.cos((R - r) * t / r)
    y = (R - r) * np.sin(theta) - r * np.sin((R - r) * t / r)
    return x, y

t = np.linspace(0, 2 * np.pi, 100)
R = 10
r = 1
theta = np.pi / 4
x, y = star_trace(t, R, r, theta)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Star Trace')
plt.show()
