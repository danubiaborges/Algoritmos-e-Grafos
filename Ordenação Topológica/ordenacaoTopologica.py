
def ordenacaoTopologica(listaAdj):

    def DFS(v, visitados, ordem):
        visitados.add(v)
        if v in listaAdj:
            for adj in listaAdj[v]:
                if adj not in visitados:
                    DFS(adj, visitados, ordem)
        ordem.append(v)

    visitados = set()
    ordem = []

    for v in listaAdj.keys():
        if v not in visitados:
            DFS(v, visitados, ordem)

    return print (list(reversed(ordem)))

# listaAdj = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
# ordenacao = ordenacaoTopologica(listaAdj)
# print(ordenacao)