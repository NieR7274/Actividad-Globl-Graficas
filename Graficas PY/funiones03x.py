import numpy as np
import matplotlib.pyplot as plt

# Dominio y función exponencial
x_exp = np.linspace(-10, 10, 5000)  # dominio más amplio
y_exp = 0.3**x_exp

# Dominio y función inversa
x_inv = np.linspace(0.001, 100, 5000)  # dominio más amplio evitando cero
y_inv = np.log(x_inv)/np.log(0.3)

# Crear figura con dos subplots verticales
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

# --------------------
# Función exponencial
# --------------------
ax1.plot(x_exp, y_exp, color="blue", label="f(x) = 0.3^x", linewidth=2)
ax1.axhline(0, color="black", linestyle="--")
ax1.axvline(0, color="black", linestyle="--")
ax1.set_title("Función exponencial f(x) = 0.3^x")
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.set_xlim([-10, 10])
ax1.set_ylim([-1, 10])
ax1.grid(True, linestyle=':', linewidth=0.7)
ax1.legend()

# --------------------
# Función inversa
# --------------------
ax2.plot(x_inv, y_inv, color="green", label="f⁻¹(x) = log_0.3(x)", linewidth=2)
ax2.axhline(0, color="black", linestyle="--")
ax2.axvline(0, color="black", linestyle="--")
ax2.set_title("Función inversa f⁻¹(x) = log_0.3(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("f⁻¹(x)")
ax2.set_xlim([0, 100])
ax2.set_ylim([-10, 10])
ax2.grid(True, linestyle=':', linewidth=0.7)
ax2.legend()

plt.tight_layout()
plt.show()
