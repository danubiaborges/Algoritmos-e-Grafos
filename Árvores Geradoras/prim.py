import numpy as np

def prim(matriz):

    matriz = np.array(matriz)
    V = matriz.shape[0]
    v = 0

    S = [v]
    N = set(range(V))
    N.remove(v)
    T = []
    custoT = 0

    while len(T) < V - 1:
        pesoMin = float('inf')
        arestaMin = None

        for v in S:
            for u in N:
                if matriz[v][u] > 0 and matriz[v][u] < pesoMin:
                    pesoMin = matriz[v, u]
                    arestaMin = (v, u)

        v, u = arestaMin
        S.append(u)
        N.remove(u)
        T.append((v, u))
        custoT += pesoMin

    return T, custoT

entrada = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
              [4, 0, 8, 0, 0, 0, 0, 11, 0],
              [0, 8, 0, 7, 0, 4, 0, 0, 2],
              [0, 0, 7, 0, 9, 14, 0, 0, 0],
              [0, 0, 0, 9, 0, 10, 0, 0, 0],
              [0, 0, 4, 14, 10, 0, 2, 0, 0],
              [0, 0, 0, 0, 0, 2, 0, 1, 6],
              [8, 11, 0, 0, 0, 0, 1, 0, 7],
              [0, 0, 2, 0, 0, 0, 6, 7, 0]]

arestas, custo = prim(entrada)
saida = " ".join([f"({u}, {v})" for u, v in arestas]) + " " + str(custo)
print(saida)