def DFS(listaAdj, vertice):
    
    visitados = []

    def DFSrecursivo(v):
        
        visitados.append(v)                     # Marca o v como visitado

        for adjacente in listaAdj[v]:
            if adjacente not in visitados:
                DFSrecursivo(adjacente)         #Chamada recursiva

    if vertice not in visitados:
        DFSrecursivo(vertice)                   # Chama a função recursiva para o v inicial

    return print(visitados)