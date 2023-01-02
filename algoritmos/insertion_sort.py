def insertion_sort(list):

    for i in range(1, len(list)):

        el = list[i]

        j = i - 1

        while list[j] > el and j >= 0:
            list[j], list[j + 1] = list[j + 1], list[j]
            j -= 1

    return list 

