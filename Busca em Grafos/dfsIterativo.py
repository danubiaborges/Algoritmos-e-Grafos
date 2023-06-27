def DFS(listaAdj, vertice):
    
    pilha = []
    pilha.append(vertice)
    visitados = []

    while pilha:
        vertice = pilha.pop()                                                   # Remove o vértice do topo da pilha
        if vertice not in visitados:
            visitados.append(vertice)                                           # Vértice visitado

            for item in reversed(listaAdj[vertice]):
                if item not in visitados:
                    pilha.append(item)                                          # Adiciona os vértices adj não visitados a pilha
                    
    x = listaAdj.keys()
    for item in x:
        if item not in visitados:
            visitados.append(item)                                              # Adiciona vértices desconexos

    return print(visitados)

DFS({0: [2, 4], 1: [2, 4], 2: [0, 1, 4], 3: [], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5]}, 0)
