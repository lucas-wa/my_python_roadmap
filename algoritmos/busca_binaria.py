def busca(list, element):
    first = 0
    last = len(list) - 1

    while first <= last:
        idx = (first + last)//2

        print(idx)

        if list[idx] == element:
            return idx
        else:
            if list[idx] < element:
                first = idx + 1
            else:
                last = idx - 1
    
    return False
