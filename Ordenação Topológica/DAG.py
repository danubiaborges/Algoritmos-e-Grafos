def verificaDAG(listaAdj):

    def DFS(v, visitados, pilha):
        visitados.add(v)
        pilha.add(v)

        if v in listaAdj:
            for adj in listaAdj[v]:
                if adj not in visitados:
                    if DFS(adj, visitados, pilha):
                        return True
                elif adj in pilha:
                    return True

        pilha.remove(v)
        return False

    visitados = set()
    pilha = set()

    for v in listaAdj:
        if v not in visitados:
            if DFS(v, visitados, pilha):
                return print('NÃO DAG')

    return print('DAG')

# listaAdj = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
# resultado = verificaDAG(listaAdj)
# print(resultado)