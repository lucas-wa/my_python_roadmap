def busca(list, element):

    for i in range(len(list)):
        if list[i] == element:
            return i
    
    return False
