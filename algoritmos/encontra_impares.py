def encontra_impares(list):

    if len(list) <= 1:
        return list if not list[0] % 2 == 0 else []
        
    
    half = len(list) // 2

    first = encontra_impares(list[:half])
    second = encontra_impares(list[half:])
    
    first.extend(second)

    return first

print(encontra_impares([13, 12, 3, 9, 8, 0, 6, 5]))
