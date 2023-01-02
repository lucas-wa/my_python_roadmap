def incomodam(n):
    
    if n <= 0:
        return ""

    if n == 1:
        return "incomodam "
    
    return "incomodam " + incomodam(n-1)

def elefantes(n, firstCall = True):

    if n < 1:
        return ""
    
    if n == 1:
        return "Um elefante incomoda muita gente"
    
    return elefantes(n -1, False) + "\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n" + ((str(n) + " incomodam muita gente") if not firstCall else "")

