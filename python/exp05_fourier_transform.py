"""Experiment 5: Magnitude and phase spectrum of a signal using the Fourier transform."""
import numpy as np
from common import save, plt

fs = 1000
t = np.arange(0, 1, 1 / fs)
x = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t + np.pi / 4)

N = len(x)
X = np.fft.fftshift(np.fft.fft(x)) / N
f = np.fft.fftshift(np.fft.fftfreq(N, 1 / fs))
mag = np.abs(X)
phase = np.angle(np.where(mag > 1e-6, X, 0))   # suppress numerical-noise phase

print("Dominant frequencies (Hz):", f[(mag > 0.1) & (f > 0)])
fig, axs = plt.subplots(3, 1, figsize=(9, 9))
axs[0].plot(t[:200], x[:200]); axs[0].set(title="Signal x(t) (first 0.2 s)", xlabel="t (s)")
axs[1].plot(f, mag); axs[1].set(title="Magnitude spectrum |X(f)|", xlabel="f (Hz)", xlim=(-200, 200))
axs[2].plot(f, phase); axs[2].set(title="Phase spectrum ∠X(f)", xlabel="f (Hz)", ylabel="rad", xlim=(-200, 200))
for ax in axs: ax.grid(True)
save(fig, "exp05_fourier_transform.png")

# Rectangular pulse: sinc-shaped spectrum
T = 0.1
t2 = np.arange(-1, 1, 1 / fs)
p = (np.abs(t2) <= T / 2).astype(float)
P = np.fft.fftshift(np.fft.fft(p)) / fs
f2 = np.fft.fftshift(np.fft.fftfreq(len(p), 1 / fs))
fig, axs = plt.subplots(3, 1, figsize=(9, 9))
axs[0].plot(t2, p); axs[0].set(title="Rectangular pulse", xlabel="t (s)")
axs[1].plot(f2, np.abs(P)); axs[1].set(title="Magnitude |P(f)| (sinc)", xlabel="f (Hz)", xlim=(-100, 100))
axs[2].plot(f2, np.angle(np.where(np.abs(P) > 1e-6, P, 0))); axs[2].set(title="Phase", xlabel="f (Hz)", xlim=(-100, 100))
for ax in axs: ax.grid(True)
save(fig, "exp05_rect_pulse_spectrum.png")
