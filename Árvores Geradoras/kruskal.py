import numpy as np

def kruskal(matriz):
    
    H = []
    for v in range(len(matriz)):
        for u in range(len(matriz[v])):
            if matriz[v][u] != 0:
                H.append((v, u, matriz[v][u]))

    H.sort(key=lambda x: x[2])

    parent = list(range(len(matriz)))
    altura = [0] * len(matriz)

# retorna a raiz do conjunto que o vértice x pertence
    def raiz(x):
        if parent[x] != x:
            parent[x] = raiz(parent[x])
        return parent[x]

# une os conjuntos que os vértices x e y pertencem
    def uniao(x, y):
        raizX = raiz(x)
        raizY = raiz(y)
        if altura[raizX] < altura[raizY]:
            parent[raizX] = raizY
        elif altura[raizX] > altura[raizY]:
            parent[raizY] = raizX
        else:
            parent[raizY] = raizX
            altura[raizX] += 1

    T = []
    custo = 0

    for x, y, peso in H:
        if raiz(x) != raiz(y):
            T.append((x, y))
            custo += peso
            uniao(x, y)
            if len(T) == len(matriz) - 1:
                break

    if len(T) == len(matriz) - 1:
        return print(T, custo)



matriz = np.array([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])

H, custo = kruskal(matriz)
print("H:", H)
print("Custo:", custo)