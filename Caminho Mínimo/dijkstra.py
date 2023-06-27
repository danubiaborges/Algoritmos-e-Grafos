import numpy as np

def dijkstra(matriz, vOrigem, vDestino):
    custo = [0]
    rota = [0]

    for i in range(1, len(matriz)):
        custo.append(float('inf'))
        rota.append(0)
    
    A = list(range(len(matriz)))
    F = []

    while A != []:
        v = min(A, key = lambda x: custo[x])
        F.append(v)
        A.remove(v)
        N = list(set(A) - set(F))

        for u in N:
            if matriz[v][u] != -1 and custo[v] + matriz[v][u] < custo[u]:
                custo[u] = custo[v] + matriz[v][u]
                rota[u] = v

    caminhoMinimo = [vDestino]
    vAtual = vDestino
    while vAtual != vOrigem:
        vAtual = rota[vAtual]
        caminhoMinimo.insert(0, vAtual)

    return caminhoMinimo, custo[vDestino]

matrizAdj = np.array([[-1, 3, 8, 4, -1, 10], [ 3, -1, -1, 6, -1, -1], [ 8, -1, -1, -1, 7, -1], [ 4,  6, -1, -1,  1,  3], [-1, -1,  7,  1, -1, 1], [10, -1, -1,  3,  1, -1]])
origem = 0
destino = 5

caminhoMinimo, custo = dijkstra(matrizAdj, origem, destino)
print("Caminho minimo:", caminhoMinimo)
print("Custo minimo:", custo)
