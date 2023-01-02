def ordenada(list):

    if len(list) == 1:
        return True

    if (list[0] > list[1] or list[-2] > list[-1]):
        return False

    for i in range(1 , len(list) - 1):
        if not (list[i] < list[i + 1] and list[i] > list[i - 1]):
            return False
    
    return True