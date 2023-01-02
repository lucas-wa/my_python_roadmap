def primeiro_lex(list):
    first = ""

    for string in list:
        if first == "" or string < first:
                first = string
    
    return first
