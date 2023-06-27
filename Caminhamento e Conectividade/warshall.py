def warshall(matriz):
    
    n = len(matriz)
    R = np.copy(matriz)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if R[i][j] == 1 or (R[i][k] == 1 and R[k][j] == 1):
                    R[i][j] = 1
                else:
                    R[i][j] = R[i][j]
    return print(R)