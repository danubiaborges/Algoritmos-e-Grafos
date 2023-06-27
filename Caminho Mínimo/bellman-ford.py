def bellmanFord(matriz, vOrigem, vDestino):

    n = len(matriz)
    custo = [float('inf')] * n
    rota = [0] * n
    custo[vOrigem] = 0

    for i in range(n):
        for v in range(n):
            for u in range(n):
                if matriz[v][u] != -1 and custo[u] > custo[v] + matriz[v][u]:
                    custo[u] = custo[v] + matriz[v][u]
                    rota[u] = v

    for v in range(n):
        for u in range(n):
            if matriz[v][u] != -1 and custo[u] > custo[v] + matriz[v][u]:               
                return False

    caminhoMinimo = []
    vAtual = vDestino
    while vAtual != vOrigem:
        caminhoMinimo.append(vAtual)
        vAtual = rota[vAtual]
    caminhoMinimo.append(vOrigem)
    caminhoMinimo.reverse()

    return caminhoMinimo, custo[vDestino]

entrada = [[-1,6,-1,7,-1], [-1,-1,5,8,-4], [-1,-2,-1,-1,-1], [-1,-1,-3,-1,9], [2,-1,7,-1,-1]]
vOrigem = 0
vDestino = 4

resultado = bellmanFord(entrada, vOrigem, vDestino)
print(resultado)