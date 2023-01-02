def ordena(list):

    for i in range(len(list) - 1):

        smaller_idx = i

        for j in range(i + 1, len(list)):
            if list[j] < list[smaller_idx]:
                smaller_idx = j
        
        list[i], list[smaller_idx] = list[smaller_idx], list[i]
    
    return list

