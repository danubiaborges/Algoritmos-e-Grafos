def criaListaAdjacencias(matriz):

    listaAdj = {}                                           # dicionário vazio que será preenchido com as listas de adj
    for i in range(len(matriz)):
        lista = []
        for j in range(len(matriz[i])):
                        while matriz[i][j] >= 1:
                           lista.append(j)                  # adicionando arestas
                           matriz[i][j] -= 1
        listaAdj[i] = lista
    return print(listaAdj)

def tipoGrafo(listaAdj):

    laco = False 
    arestaMult = False
    direcionado = False

    # for para verificar as características do grafo
    for x in listaAdj:
        for y in listaAdj:
            if y in  listaAdj[x] and x == y:
                laco = True
            if y in listaAdj[x] and not (x in listaAdj[y]):
                    direcionado = True
            if listaAdj[x].count(y) > 1:                            # verificando se possui arestas multiplas
                arestaMult = True 
 
    if not laco and not arestaMult and not direcionado:            # verificando se o grafo não possuí arestas multiplas e nem laços: GRAFO SIMPLES
        return print(0)        # simples 
    if not laco and arestaMult and direcionado:                    # verificando se o grafo possuí arestas multiplas e não possuí laços: MULTIGRAFO
        return print(21)       # multigrafo dirigido
    if not laco and arestaMult and not direcionado:                # verificando se o grafo possuí arestas multiplas e não possuí laços: MULTIGRAFO
        return print(20)       # multigrafo 
    if laco and not direcionado:                                   # verificando se o grafo não possuí arestas multiplas e possuí laços: PSEUDOGRAFO
        return print(30)       # pseudografo        
    if laco and direcionado :                                      # verificando se o grafo não possuí arestas multiplas e possuí laço: PSEUDOGRAFO
        return print(31)       # pseudografo dirigido          
    if direcionado and not laco and not arestaMult:                # verificando se o grafo é direcionado: DÍGRAFO
        return print(1)        # dígrafo
    
def calcDensidadeLista(listaAdj):
    
    densidade = 0
    qtdVertices = len(listaAdj)
    qtdArestas = 0


    #calcula quantidade de arestas
    for vi in range(0, qtdVertices):                    # para cada vértice vi
        qtdArestas += len(listaAdj[vi])                 # soma a quantidade de arestas
    densidade = qtdArestas / (qtdVertices  * (qtdVertices - 1)) 
    densidadeFormat = "{:.3f}".format(densidade)        # precisão de 3 casas decimais
    return print(float(densidadeFormat))

def insereAresta(listaAdj, vi, vj):

    listaAdj[vi].append(vj) # adiciona aresta ao vértice vi
    listaAdj[vi].sort()
    listaAdj[vj].append(vi) # adiciona aresta ao vértice vj
    listaAdj[vj].sort() 
    return print(listaAdj)

def insereVerticeLista(listaAdj):

    size = len(listaAdj)
    listaAdj[size] = []    
    return print(listaAdj)

def removeArestaLista(listaAdj, vi, vj):

    listaAdj[vi].remove(vj)
    if vi in listaAdj[vj]:
        listaAdj[vj].remove(vi)
    return print(listaAdj)

def removeVerticeLista(listaAdj, vi):

    del listaAdj[vi]                                     # deleta vértice da lista de adjacencia
    for v in listaAdj:
        for v2 in listaAdj[v]:                           # no caso de arestas multiplas, remover ambas
            if vi in listaAdj[v]:
                listaAdj[v].remove(vi)                   # remove cada aresta que contenha o vértice excluído 
    return print(listaAdj)

def verificaAdjacenciaLista(listaAdj, vi, vj):

    verticesAdj = False
    if vj in listaAdj[vi]:                              # se houver vj em vi adjacencia como true
        verticesAdj = True
    else:
        verticesAdj = False
    return print(verticesAdj)