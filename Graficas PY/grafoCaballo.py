import networkx as nx
import matplotlib.pyplot as plt

def knight_moves(pos, n=4):
    """
    Genera los movimientos válidos de un caballo
    desde una posición (fila, columna) en un tablero n×n.
    """
    (i, j) = pos
    moves = [
        (i+2, j+1), (i+2, j-1),
        (i-2, j+1), (i-2, j-1),
        (i+1, j+2), (i+1, j-2),
        (i-1, j+2), (i-1, j-2),
    ]
    return [(r, c) for (r, c) in moves if 1 <= r <= n and 1 <= c <= n]

# Crear el grafo
G = nx.Graph()
n = 4
labels = {}

# Crear nodos con nombres estilo ajedrez (a1..d4)
for fila in range(1, n+1):       # filas = 1..n
    for col in range(1, n+1):    # columnas = 1..n
        node = (fila, col)
        label = chr(96+col) + str(fila)   # ej. (1,1)->"a1", (4,4)->"d4"
        G.add_node(node)
        labels[node] = label

# Añadir aristas de movimientos del caballo
for node in G.nodes:
    for move in knight_moves(node, n):
        G.add_edge(node, move)

# Posición de cada nodo según tablero de ajedrez (columna = x, fila = y)
pos = { (fila, col): (col, fila) for (fila, col) in G.nodes }

# Dibujar tablero en blanco y negro
plt.figure(figsize=(6, 6))
for fila in range(1, n+1):
    for col in range(1, n+1):
        color = "white" if (fila+col) % 2 == 0 else "lightgray"
        plt.gca().add_patch(plt.Rectangle((col-0.5, fila-0.5), 1, 1, facecolor=color))

# Dibujar grafo encima del tablero
nx.draw(G, pos, with_labels=True, labels=labels,
        node_size=800, node_color="skyblue", font_size=10, font_weight="bold",
        edge_color="black")

# Ajustar límites
plt.xlim(0.5, n+0.5)
plt.ylim(0.5, n+0.5)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.title("Knight Graph sobre tablero 4x4 (orientación ajedrez)")
plt.show()
