"""Experiment 10: Numerical verification of Fourier transform properties (DFT-based)."""
import numpy as np
from common import save, plt

N = 256
n = np.arange(N)
rng = np.random.default_rng(0)
x1 = rng.standard_normal(N); x2 = rng.standard_normal(N)
F = np.fft.fft
results = []

def check(name, lhs, rhs):
    err = np.max(np.abs(lhs - rhs))
    ok = err < 1e-9
    results.append((name, err, ok))
    print(f"{name:<32s} max error = {err:.2e}   {'VERIFIED' if ok else 'FAILED'}")

a, b = 2.5, -1.3
check("Linearity", F(a * x1 + b * x2), a * F(x1) + b * F(x2))

m = 17
check("Circular time shift", F(np.roll(x1, m)), F(x1) * np.exp(-2j * np.pi * np.arange(N) * m / N))

k0 = 9
check("Frequency shift (modulation)", F(x1 * np.exp(2j * np.pi * k0 * n / N)), np.roll(F(x1), k0))

check("Time reversal", F(x1[(-n) % N]), F(x1)[(-n) % N])

check("Conjugation", F(np.conj(x1 + 1j * x2)), np.conj(F(x1 + 1j * x2))[(-n) % N])

circ = np.real(np.fft.ifft(F(x1) * F(x2)))
direct = np.array([np.sum(x1 * x2[(m_ - n) % N]) for m_ in n])
check("Convolution (time -> product)", circ, direct)

check("Multiplication (time -> conv)", F(x1 * x2),
      np.array([np.sum(F(x1) * F(x2)[(kk - n) % N]) for kk in n]) / N)

check("Parseval (energy)", np.sum(np.abs(x1) ** 2), np.sum(np.abs(F(x1)) ** 2) / N)

check("Conjugate symmetry (real x)", F(x1), np.conj(F(x1)[(-n) % N]))

# Visual: time shift leaves magnitude unchanged, changes phase linearly
fig, axs = plt.subplots(2, 1, figsize=(9, 6))
sig = np.exp(-0.5 * ((n - 100) / 8) ** 2)
axs[0].plot(np.abs(F(sig))[:40], label="original"); axs[0].plot(np.abs(F(np.roll(sig, 30)))[:40], "--", label="shifted by 30")
axs[0].set(title="Magnitude is unchanged by a time shift", xlabel="k"); axs[0].legend()
axs[1].plot(np.unwrap(np.angle(F(sig)))[:40], label="original"); axs[1].plot(np.unwrap(np.angle(F(np.roll(sig, 30))))[:40], "--", label="shifted by 30")
axs[1].set(title="Phase changes linearly with shift", xlabel="k", ylabel="rad"); axs[1].legend()
for ax in axs: ax.grid(True)
save(fig, "exp10_time_shift_property.png")

fig, ax = plt.subplots(figsize=(9, 4))
ax.bar([r[0] for r in results], [max(r[1], 1e-17) for r in results], color=["g" if r[2] else "r" for r in results])
ax.set_yscale("log"); ax.set(title="Max error per property (all should be ~1e-13 or lower)", ylabel="error")
plt.setp(ax.get_xticklabels(), rotation=35, ha="right")
save(fig, "exp10_property_errors.png")
