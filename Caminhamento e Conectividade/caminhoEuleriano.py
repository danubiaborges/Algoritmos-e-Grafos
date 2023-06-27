def caminhoEuleriano(matriz):
    
    matriznp = np.array(matriz)
    n = len(matriznp)
    total = 0
    i = 0
    
    while (total <= 2) and (i < n):
        grau = np.sum(matriznp[i])
        if grau % 2 != 0:
            total += 1
        i += 1
    if total > 2:
        return print (False)
    else:
        return print (True)