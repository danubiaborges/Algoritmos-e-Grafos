def BFS(listaAdj, inicio):
    
    visitados = []                             # Lista dos vértices visitados
    fila = []                                   # Lista dos vértices que serão explorados
    fila.append(inicio)                          # Inserindo o vértice inicial na lista

    while fila:
        vertice = fila.pop(0)                   # Removendo o primeiro elemento da lista
        if vertice not in visitados:
            visitados.append(vertice)           # Vértice visitado
            
            # Adicionamos os vértices adj não visitados:
            for adjacente in listaAdj[vertice]:
                if adjacente not in visitados and adjacente not in fila:
                    fila.append(adjacente)

    # Resolvendo o problema do Teste 5, em que o vértice 3 é desconexo:
    vertices = list(listaAdj.keys())
    for vertice in vertices:
        if vertice not in visitados:
            fila.append(vertice)
            while fila:
                vDesconexo = fila.pop(0)
                visitados.append(vDesconexo)
                for adjacente in listaAdj[vDesconexo]:
                    if adjacente not in visitados and adjacente not in fila:
                        fila.append(adjacente)
                        
    return print(visitados)

BFS({0: [2, 4], 1: [2, 4], 2: [0, 1, 4], 3: [], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5]}, 0)
