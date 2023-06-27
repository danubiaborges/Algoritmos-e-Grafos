def temposVertices(listaAdj, v):

    def dfs_visit(vertice, tempo):
        tempo += 1
        td[vertice] = tempo
        for adjacente in listaAdj[vertice]:
            if adjacente not in td:
                tempo = dfs_visit(adjacente, tempo)
        tempo += 1
        tt[vertice] = tempo
        return tempo

    td = {}
    tt = {}

    if v not in listaAdj:
        return {}

    tempo = 0
    tempo = dfs_visit(v, tempo)

    for vertice in listaAdj:
        if vertice not in td:
            tempo = dfs_visit(vertice, tempo)

    return {vertice: f'{td[vertice]}/{tt[vertice]}' for vertice in listaAdj}


# listaAdj = {0: [1, 4], 1: [2, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}
# v = 0

# resultado = temposVertices(listaAdj, v)
# print(resultado)
