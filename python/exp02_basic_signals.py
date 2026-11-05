"""Experiment 2: Unit step, unit impulse, ramp, exponential, parabolic and sinusoidal signals."""
import numpy as np
from common import save, plt

n = np.arange(-10, 11)
t = np.linspace(-2, 4, 1000)

step = (n >= 0).astype(float)
impulse = (n == 0).astype(float)
ramp = np.where(n >= 0, n, 0)
expo = np.exp(0.2 * n)
parab = np.where(n >= 0, n ** 2 / 2, 0)

fig, axs = plt.subplots(3, 2, figsize=(11, 9))
for ax, y, title in zip(axs.flat[:5], [step, impulse, ramp, expo, parab],
                        ["Unit step u[n]", "Unit impulse δ[n]", "Unit ramp r[n]",
                         "Exponential e^{0.2n}", "Parabolic n²/2 · u[n]"]):
    ax.stem(n, y); ax.set(title=title, xlabel="n", ylabel="Amplitude"); ax.grid(True)
axs.flat[5].plot(t, np.sin(2 * np.pi * 1 * t)); axs.flat[5].set(title="Sinusoid sin(2πt)", xlabel="t (s)")
axs.flat[5].grid(True)
save(fig, "exp02_basic_signals.png")

# Continuous-time sinusoid variations
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.plot(t, np.sin(2 * np.pi * t), label="sin(2πt)")
ax.plot(t, np.cos(2 * np.pi * t), label="cos(2πt)")
ax.plot(t, 2 * np.sin(4 * np.pi * t), label="2 sin(4πt)")
ax.set(title="Sinusoidal signals", xlabel="t (s)", ylabel="Amplitude"); ax.legend(); ax.grid(True)
save(fig, "exp02_sinusoids.png")
