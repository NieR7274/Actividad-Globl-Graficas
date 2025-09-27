import numpy as np
import matplotlib.pyplot as plt

# Elegir valor de nivel c
c = 4.0                # ejemplo: c>0 => esfera de radio sqrt(c)
r = np.sqrt(c)

# Parámetros esféricos
phi = np.linspace(0, np.pi, 200)      # polar
theta = np.linspace(0, 2*np.pi, 400)  # azimutal
phi, theta = np.meshgrid(phi, theta)

# Coordenadas (x,y,z) de la esfera de radio r
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Dibujo 3D
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride=4, cstride=4, linewidth=0, alpha=0.9, cmap='viridis')

# Estética
ax.set_box_aspect([1,1,1])           # ejes con misma escala
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title(f'Superficie de nivel S_c: x^2 + y^2 + z^2 = {c} (r = {r:.3f})')

# Opcional: mostrar ejes y malla
ax.grid(False)
plt.tight_layout()
plt.show()
