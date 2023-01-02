def maiusculas(phrase):
    string = ""

    for char in phrase:
        if ord(char) >= 65 and ord(char) <= 90:
            string += char
    
    return string
