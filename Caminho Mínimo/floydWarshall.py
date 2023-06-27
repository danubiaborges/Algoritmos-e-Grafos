import numpy as np

def floydWarshall(matriz):

    n = len(matriz)
    D = np.copy(matriz)

    D[D == -1] = 999999

    for k in range(0, n):
        for v in range(0, n):
            for u in range(0, n):
                if D[v][u] > D[v][k] + D[k][u]:
                    D[v][u] = D[v][k] + D[k][u]
    
    D[D == 999999] = -1

    return D

matriz = np.array([[-1, 3, 8, 4, -1, 10], [ 3, -1, -1, 6, -1, -1], [ 8, -1, -1, -1, 7, -1], [4,  6, -1, -1,  1,  3], [-1, -1,  7,  1, -1, 1], [10, -1, -1,  3,  1, -1]])

resultado = floydWarshall(matriz)

print("A matriz de distancias:")
print(resultado.tolist())