def menor_nome(names):
    smaller = ''

    for name in names:
        if smaller == "" or len(name.strip()) < len(smaller):
            smaller = name.strip().capitalize()
    
    return smaller
