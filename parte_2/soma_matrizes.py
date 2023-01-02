def dimensoes(mat):

    return ([len(mat),
            len(mat[0]) 
            if len(mat) != 0 
            else 0])


def soma_matrizes(mat1, mat2):
    dM1 = dimensoes(mat1)
    dM2 = dimensoes(mat2)

    if (dM1[0] == dM2[0]) and (dM1[1] == dM2[1]):
        mat = []

        for i in range(dM1[0]):
            line = []
            for j in range(dM1[1]):
                line.append(mat1[i][j] + mat2[i][j])
            
            mat.append(line)
        
        return mat
    
    else:

        return False
