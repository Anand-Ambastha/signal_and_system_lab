"""Experiment 7 (also CBS 1): Sampling theorem - under-sampling, Nyquist-rate and over-sampling."""
import numpy as np
from common import save, plt

f_sig = 10                                     # Hz, message frequency
t = np.linspace(0, 0.5, 5000)
x = np.cos(2 * np.pi * f_sig * t)

def sinc_reconstruct(ts, xs, t, fs):
    """Ideal reconstruction: x(t) = sum x[n] sinc(fs*t - n)."""
    return np.array([np.sum(xs * np.sinc(fs * tt - np.arange(len(xs)))) for tt in t])

cases = [("Under-sampling  fs = 15 Hz (< 2fm)", 15),
         ("Nyquist rate    fs = 20 Hz (= 2fm)", 20),
         ("Over-sampling   fs = 100 Hz (> 2fm)", 100)]
fig, axs = plt.subplots(3, 2, figsize=(12, 10))
for i, (title, fs) in enumerate(cases):
    n = np.arange(0, int(0.5 * fs) + 1)
    ts = n / fs
    xs = np.cos(2 * np.pi * f_sig * ts)
    # pad samples on both sides to reduce edge effects of the truncated sinc sum
    xr = sinc_reconstruct(ts, xs, t, fs)
    axs[i, 0].plot(t, x, label="original"); axs[i, 0].stem(ts, xs, linefmt="r-", markerfmt="ro", basefmt=" ")
    axs[i, 0].set(title=title, xlabel="t (s)"); axs[i, 0].grid(True)
    axs[i, 1].plot(t, x, "--", label="original"); axs[i, 1].plot(t, xr, label="reconstructed")
    axs[i, 1].set(title="Reconstruction (sinc interpolation)", xlabel="t (s)"); axs[i, 1].legend(); axs[i, 1].grid(True)
    err = np.sqrt(np.mean((x[1000:4000] - xr[1000:4000]) ** 2))
    print(f"fs = {fs:3d} Hz -> RMS error (middle of record) = {err:.4f}")
save(fig, "exp07_sampling_theorem.png")

# Aliasing spectrum view
fig, axs = plt.subplots(1, 2, figsize=(11, 3.8))
for ax, fs in zip(axs, [15, 100]):
    ts = np.arange(0, 2, 1 / fs); xs = np.cos(2 * np.pi * f_sig * ts)
    X = np.abs(np.fft.rfft(xs)) / len(xs); f = np.fft.rfftfreq(len(xs), 1 / fs)
    ax.stem(f, X); ax.set(title=f"Spectrum of samples, fs = {fs} Hz", xlabel="f (Hz)"); ax.grid(True)
    print(f"fs = {fs} Hz, apparent peak at {f[np.argmax(X)]:.1f} Hz")
save(fig, "exp07_aliasing_spectrum.png")
