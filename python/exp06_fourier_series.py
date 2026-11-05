"""Experiment 6: Magnitude and phase spectra of a periodic signal using the Fourier series."""
import numpy as np
from common import save, plt

T0 = 1.0
fs = 5000
t = np.arange(0, 2 * T0, 1 / fs)
tp = np.arange(0, T0, 1 / fs)
x_one = np.where(tp < T0 / 2, 1.0, -1.0)         # one period of a square wave
K = 20
k = np.arange(-K, K + 1)
# Exponential Fourier series coefficients c_k = (1/T0) * integral x(t) e^{-j k w0 t} dt
w0 = 2 * np.pi / T0
c = np.array([np.trapezoid(x_one * np.exp(-1j * kk * w0 * tp), tp) / T0 for kk in k])
print("c1 =", np.round(c[K + 1], 4), "(theory: -j*2/pi = %.4fj)" % (-2 / np.pi))

fig, axs = plt.subplots(2, 1, figsize=(9, 7))
axs[0].stem(k, np.abs(c)); axs[0].set(title="Magnitude spectrum |c_k|", xlabel="harmonic k")
axs[1].stem(k, np.angle(np.where(np.abs(c) > 1e-3, c, 0))); axs[1].set(title="Phase spectrum ∠c_k", xlabel="harmonic k", ylabel="rad")
for ax in axs: ax.grid(True)
save(fig, "exp06_fourier_series_spectra.png")

# Reconstruction with increasing number of harmonics (Gibbs phenomenon)
orig = np.where((t % T0) < T0 / 2, 1.0, -1.0)
fig, axs = plt.subplots(2, 2, figsize=(11, 7))
for ax, N in zip(axs.flat, [1, 3, 9, 49]):
    kk = np.arange(-N, N + 1)
    ck = np.array([np.trapezoid(x_one * np.exp(-1j * q * w0 * tp), tp) / T0 for q in kk])
    xr = np.real(sum(ck[i] * np.exp(1j * kk[i] * w0 * t) for i in range(len(kk))))
    ax.plot(t, orig, "k--", lw=0.8); ax.plot(t, xr); ax.set(title=f"Harmonics up to k = ±{N}", xlabel="t (s)"); ax.grid(True)
save(fig, "exp06_fourier_series_reconstruction.png")
