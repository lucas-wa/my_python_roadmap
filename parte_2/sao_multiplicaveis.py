def dimensoes(mat):

    return ([len(mat),
            len(mat[0]) 
            if len(mat) != 0 
            else 0])


def sao_multiplicaveis(mat1, mat2):

    dM1 = dimensoes(mat1)
    dM2 = dimensoes(mat2)

    return True if dM1[1] == dM2[0] else False



