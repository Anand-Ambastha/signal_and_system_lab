"""Experiment 9 (also CBS 2): Synthesis of a signal using the inverse DFT."""
import numpy as np
from common import save, plt

N = 64
fs = 64
n = np.arange(N)
t = n / fs

# Build the spectrum by hand: tones at 5 Hz (amp 1) and 12 Hz (amp 0.5, phase 90 deg)
X = np.zeros(N, dtype=complex)
X[5] = N / 2 * 1.0;                       X[N - 5] = np.conj(X[5])
X[12] = N / 2 * 0.5 * np.exp(1j * np.pi / 2)  # phase of a cosine
X[N - 12] = np.conj(X[12])

x_idft_manual = np.array([np.sum(X * np.exp(2j * np.pi * np.arange(N) * nn / N)) / N for nn in n]).real
x_ifft = np.fft.ifft(X).real
expected = 1.0 * np.cos(2 * np.pi * 5 * t) + 0.5 * np.cos(2 * np.pi * 12 * t + np.pi / 2)
print("Manual IDFT == np.fft.ifft :", np.allclose(x_idft_manual, x_ifft))
print("Synthesised == expected    :", np.allclose(x_ifft, expected))

fig, axs = plt.subplots(3, 1, figsize=(9, 9))
axs[0].stem(np.arange(N), np.abs(X)); axs[0].set(title="Designed spectrum |X[k]|", xlabel="k")
axs[1].stem(np.arange(N), np.angle(np.where(np.abs(X) > 1e-9, X, 0))); axs[1].set(title="Designed phase ∠X[k]", xlabel="k", ylabel="rad")
axs[2].plot(t, x_ifft, "o-", ms=3, label="IDFT synthesis"); axs[2].plot(t, expected, "--", label="expected")
axs[2].set(title="Synthesised time signal", xlabel="t (s)"); axs[2].legend()
for ax in axs: ax.grid(True)
save(fig, "exp09_inverse_dft.png")
