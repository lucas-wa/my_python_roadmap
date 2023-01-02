def remove_repetidos(list):
    memo = []

    for l in list:
        if not l in memo:
            memo.append(l)
    
    return sorted(memo)
