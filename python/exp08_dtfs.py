"""Experiment 8: DTFS coefficients of a periodic discrete-time signal."""
import numpy as np
from common import save, plt

N = 8
n = np.arange(N)
x = np.array([1, 2, 3, 4, 4, 3, 2, 1], dtype=float)      # one period

k = np.arange(N)
a = np.array([np.sum(x * np.exp(-2j * np.pi * kk * n / N)) / N for kk in k])   # DTFS: a_k = (1/N) sum x[n] e^{-j2pi kn/N}
print("DTFS coefficients a_k:"); print(np.round(a, 4))
print("Check against FFT/N:", np.allclose(a, np.fft.fft(x) / N))

x_rec = np.real(np.array([np.sum(a * np.exp(2j * np.pi * k * nn / N)) for nn in n]))
print("Reconstruction x[n] =", np.round(x_rec, 4), "| match:", np.allclose(x, x_rec))

fig, axs = plt.subplots(3, 1, figsize=(8, 9))
axs[0].stem(np.arange(-N, 2 * N), np.tile(x, 3)); axs[0].set(title="Periodic signal x[n] (3 periods)", xlabel="n")
axs[1].stem(k, np.abs(a)); axs[1].set(title="Magnitude |a_k|", xlabel="k")
axs[2].stem(k, np.angle(np.where(np.abs(a) > 1e-9, a, 0))); axs[2].set(title="Phase ∠a_k", xlabel="k", ylabel="rad")
for ax in axs: ax.grid(True)
save(fig, "exp08_dtfs.png")
