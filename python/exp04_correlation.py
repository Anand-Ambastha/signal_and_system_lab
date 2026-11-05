"""Experiment 4: Autocorrelation and cross-correlation of sequences."""
import numpy as np
from common import save, plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 1, 0, 3, 1, 4])

rxx = np.correlate(x, x, mode="full")
rxy = np.correlate(x, y, mode="full")
lags = np.arange(-(len(x) - 1), len(x))
print("x =", x); print("y =", y)
print("Autocorrelation Rxx =", rxx)
print("Cross-correlation Rxy =", rxy)
print("Rxx peak at lag", lags[np.argmax(rxx)], "(value = energy =", np.sum(x**2), ")")

fig, axs = plt.subplots(2, 2, figsize=(10, 7))
axs[0, 0].stem(x); axs[0, 0].set_title("x[n]")
axs[0, 1].stem(y); axs[0, 1].set_title("y[n]")
axs[1, 0].stem(lags, rxx); axs[1, 0].set(title="Autocorrelation Rxx[l]", xlabel="lag l")
axs[1, 1].stem(lags, rxy); axs[1, 1].set(title="Cross-correlation Rxy[l]", xlabel="lag l")
for ax in axs.flat: ax.grid(True)
save(fig, "exp04_correlation.png")
