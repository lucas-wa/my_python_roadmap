def soma_lista(list):
    
    if len(list) == 1:
        return list[0]
    
    half = len(list) // 2

    return soma_lista(list[half:]) + soma_lista(list[:half]) 
