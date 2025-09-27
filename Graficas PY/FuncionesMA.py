import numpy as np
import matplotlib.pyplot as plt

# Dominio para funciones
x = np.linspace(-3, 3, 800)

# Funciones a mostrar
y_cubica = x**3           # f(x) = x^3  -> inyectiva (pasa la prueba horizontal)
y_parabola = x**2         # f(x) = x^2  -> no inyectiva (no pasa la prueba horizontal)

# Circulo (no es funcion segun la prueba vertical)
theta = np.linspace(0, 2*np.pi, 400)
r = 1.0
x_circ = r * np.cos(theta)
y_circ = r * np.sin(theta)

# Seno (ejemplo de funcion que no es globalmente invertible)
x_sin = np.linspace(-2*np.pi, 2*np.pi, 1000)
y_sin = np.sin(x_sin)

# Crear figura con 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Pruebas graficas: vertical y horizontal", fontsize=14)

# Funcion cubica (pasa la prueba horizontal)
ax = axes[0, 0]
ax.plot(x, y_cubica, label="y = x^3")
ax.hlines(1.0, -3, 3, colors="red", linestyles="--", label="y=1")
ax.set_title("Funcion cubica")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.legend(); ax.grid(True)

# Parabola (no pasa la prueba horizontal)
ax = axes[0, 1]
ax.plot(x, y_parabola, label="y = x^2")
ax.hlines(1.0, -3, 3, colors="red", linestyles="--", label="y=1")
ax.set_title("Parabola")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.legend(); ax.grid(True)

# Circulo (falla la prueba vertical)
ax = axes[1, 0]
ax.plot(x_circ, y_circ, label="x^2 + y^2 = 1")
ax.vlines(0.5, -1.5, 1.5, colors="magenta", linestyles="--", label="x=0.5")
ax.set_title("Circulo")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_aspect("equal", "box")
ax.legend(); ax.grid(True)

# Seno (funcion, pero no inyectiva globalmente)
ax = axes[1, 1]
ax.plot(x_sin, y_sin, label="y = sin(x)")
ax.hlines(0.5, x_sin.min(), x_sin.max(), colors="red", linestyles="--", label="y=0.5")
ax.vlines(0.1, -1.5, 1.5, colors="green", linestyles=":", label="x=0.1")
ax.set_title("Seno")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.legend(); ax.grid(True)

# Ajustes finales
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
