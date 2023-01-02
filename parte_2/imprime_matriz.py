def imprime_matriz(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j == len(mat[i]) - 1:
                print(mat[i][j])
            else:
                print(mat[i][j], end=" ")

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
