def conta_letras(phrase, count="vogais"):
    chars = ""

    for char in phrase:

        isVowel = ( ord(char) == 65 or 
                    ord(char) == 69 or 
                    ord(char) == 73 or 
                    ord(char) == 79 or 
                    ord(char) == 85 or 
                    ord(char) == 97 or 
                    ord(char) == 101 or 
                    ord(char) == 105 or 
                    ord(char) == 111 or 
                    ord(char) == 117)


        if count == "vogais":
            if isVowel:
                chars += char
        else:
            if not isVowel:
                chars += char
 
    return len(chars)
