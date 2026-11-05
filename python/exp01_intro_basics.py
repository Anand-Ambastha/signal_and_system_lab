"""Experiment 1: Introduction to MATLAB and its basic commands (Python/NumPy equivalent)."""
import numpy as np
from common import OUT, save, plt

lines = []
def show(label, value):
    s = f"{label}:\n{value}\n"
    print(s); lines.append(s)

a = 5; b = 3
show("a + b, a - b, a * b, a / b, a ** b", (a + b, a - b, a * b, a / b, a ** b))
v = np.array([1, 2, 3, 4, 5])
show("Row vector v", v)
show("Column vector v.T", v.reshape(-1, 1))
show("linspace(0, 1, 5)", np.linspace(0, 1, 5))
show("arange(0, 10, 2)", np.arange(0, 10, 2))
A = np.array([[1, 2], [3, 4]]); B = np.array([[5, 6], [7, 8]])
show("Matrix A", A)
show("A @ B (matrix product)", A @ B)
show("A * B (element-wise)", A * B)
show("Transpose of A", A.T)
show("Inverse of A", np.linalg.inv(A))
show("Determinant of A", np.linalg.det(A))
show("zeros(2,3)", np.zeros((2, 3)))
show("ones(2,3)", np.ones((2, 3)))
show("eye(3)", np.eye(3))
show("Complex number z = 3+4j: abs, angle(rad)", (abs(3 + 4j), np.angle(3 + 4j)))
show("sum, mean, max of v", (v.sum(), v.mean(), v.max()))
show("v[1:4] (slicing)", v[1:4])

x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(x, np.sin(x), label="sin(x)"); ax.plot(x, np.cos(x), "--", label="cos(x)")
ax.set(title="Basic plotting", xlabel="x", ylabel="y"); ax.grid(True); ax.legend()
save(fig, "exp01_basic_plot.png")
(OUT / "exp01_output.txt").write_text("\n".join(lines))
