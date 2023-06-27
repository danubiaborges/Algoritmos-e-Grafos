def classificaArestas(listaAdj, v):

# Inicializando variáveis
    cor = {}    # dicionário p/ guardar a cor de cada v;
    pai = {}    #dicionário p/ guardar o pai de cada v;
    tempo = 0
    descoberta = {}      # tempo de descoberta;
    fim = {}      # tempo finalização de cada v;
    tipo = {}

    for u in listaAdj.keys():
        cor[u] = 'branco'
        pai[u] = None
        descoberta[u] = 'N/A'
        fim[u] = 'N/A'

# Definindo a função auxiliar DFS
    def DFS(u):
        nonlocal tempo
        cor[u] = 'cinza'
        tempo += 1
        descoberta[u] = tempo
        for v in listaAdj[u]:
            if cor[v] == 'branco':
                tipo[(u,v)] = 'Tree'
                pai[v] = u
                DFS(v)
            elif cor[v] == 'cinza':
                tipo[(u,v)] = 'Back'
            elif descoberta[u] < descoberta[v]:
                tipo[(u,v)] = 'Forward'
            else:
                tipo[(u,v)] = 'Cross'
        cor[u] = 'preto'
        tempo += 1
        fim[u] = tempo

# Chamando a DFS para cada vértice que ainda não foi visitado
    for u in listaAdj.keys():
        if cor[u] == 'branco':
            DFS(u)

# Mostrando o resultado
    result = ''
    for (u,v) in tipo.keys():
        result += str(u) + ' ' + str(v) + ' ' + tipo[(u,v)] + '\n'
    return result

# v = 0
# print(classificaArestas(listaAdj, v))