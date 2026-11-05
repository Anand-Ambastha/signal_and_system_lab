"""Experiment 3: Linear convolution of two sequences (direct sum vs np.convolve)."""
import numpy as np
from common import save, plt

x = np.array([1, 2, 3, 4]);  nx = np.arange(0, len(x))
h = np.array([1, 1, 1]);     nh = np.arange(0, len(h))

def conv_manual(x, h):
    y = np.zeros(len(x) + len(h) - 1)
    for n in range(len(y)):
        for k in range(len(x)):
            if 0 <= n - k < len(h):
                y[n] += x[k] * h[n - k]
    return y

y = conv_manual(x, h)
y_np = np.convolve(x, h)
ny = np.arange(0, len(y))
print("x[n] =", x); print("h[n] =", h)
print("y[n] manual   =", y)
print("y[n] np.conv  =", y_np)
print("Match:", np.allclose(y, y_np))

fig, axs = plt.subplots(3, 1, figsize=(7, 8))
for ax, n_, s, t_ in zip(axs, [nx, nh, ny], [x, h, y], ["x[n]", "h[n]", "y[n] = x[n] * h[n]"]):
    ax.stem(n_, s); ax.set(title=t_, xlabel="n"); ax.grid(True)
save(fig, "exp03_linear_convolution.png")
