# -- coding: UTF-8 --i#
import re
import math

def calc_1(text):
    words = re.sub(r'[.!?,;:]+', '', text).split()
    # print(words) 
    sum = 0

    for word in words:
        sum += len(word) 
    
    return sum / len(words)

def calc_2(text):
    memo = []
    words = re.sub(r'[.!?,;:]+', '', text).split()


    for word in words:
        if (not word.lower() in memo) and (not word.upper() in memo):
            memo.append(word.lower())

    return len(memo) / len(words)

def calc_3(text):
    memo = []
    words = re.sub(r'[.!?,;:]+', '', text).split() 
    deleted = []

    for idx in range(len(words)):
        if (not words[idx].lower() in memo) and (not words[idx].lower() in deleted):
            memo.append(words[idx].lower())
        else:
            for elIDX in range(len(memo)):
                if (memo[elIDX].lower() == words[idx].lower()):
                    deleted.append(memo[elIDX])
                    del memo[elIDX]
                    break
    

    
    return len(memo) / len(words)

def calc_4(text):
    sentences = re.split(r'[.!?]+', text)
    sum = 0


    if sentences[-1] == "":
        del sentences[-1]

    
    for sentence in sentences:
        chars = re.sub(r'[ ]+', "a", sentence)

        sum += len(chars)
        # for word in words:
        #     sum += len(word)
    
    return sum / len(sentences)

def calc_5(text):
    sentences = re.split(r'[.!?]+', text)

    if sentences[-1] == "":
        del sentences[-1]


    sum = 0

    for sentence in sentences:
        phrases = re.split(r'[,:;]+', sentence)

        sum += len(phrases)
    
    return sum / len(sentences)

def calc_6(text):
        phrases = re.split(r'[.!?,;:]+', text)
        
        if phrases[-1] == "":
            del phrases[-1]

        Nphrases = 0
        Nchars = 0

        for phrase in phrases:
            chars = re.sub(r'[ ]+', "a", phrase)
            Nphrases += 1
            Nchars += len(chars)

        return Nchars / Nphrases

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similarity = 0
    for idx in range(6):
        similarity += abs(as_a[idx] - as_b[idx]) / 6

    return similarity

def calcula_assinatura(text):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    return [
        calc_1(text),
        calc_2(text),
        calc_3(text),
        calc_4(text),
        calc_5(text),
        calc_6(text),
    ]

def avalia_textos(texts, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similarity = -1
    most_similar = 0
    idx = 0

    for text in texts:
        ass = calcula_assinatura(text)

        Sab = compara_assinatura(ass, ass_cp)

        if (similarity == -1) or Sab < similarity:
            similarity = Sab
            most_similar = idx
        
        idx+= 1
    
    return most_similar + 1 
        

        

# print("Bem-vindo ao detector automático de COH-PIAH.")
# print("Informe a assinatura típica de um aluno infectado:\n")

# i_1 = float(input("Entre o tamanho médio de palavra: "))
# i_2 = float(input("Entre a relação Type-Token: "))
# i_3 = float(input("Entre a Razão Hapax Legomana: "))
# i_4 = float(input("Entre o tamanho médio de sentença: "))
# i_5 = float(input("Entre a complexidade média da sentença: "))
# i_6 = float(input("Entre o tamanho médio de frase: "))

# original_traits = [i_1, i_2, i_3, i_4, i_5, i_6]

# texts = []

# texts_traits = []

# txt = "first"

# print()

# while txt != '':
#     txt = input("Digite o texto " + str(len(texts) + 1) + " (aperte enter para sair): ")
#     print()
#     texts.append(txt)

# del texts[-1]

# for text in texts:
#     texts_traits.append([
#         calc_1(text),
#         calc_2(text),
#         calc_3(text),
#         calc_4(text),
#         calc_5(text),
#         calc_6(text),
#     ])

# similarity = 0
# most_similar = 0
# last_similarity = -1
# index = 0

# for text_trait in texts_traits:
    
#     trait_idx = 0

#     for i in text_trait:
#         similarity += abs(i - original_traits[trait_idx]) / 6
#         trait_idx += 1
    
#     if (last_similarity == -1) or similarity < last_similarity:
#         last_similarity = similarity
#         most_similar = index

#     index += 1         

# print("O autor do texto " + str(most_similar + 1) + " está infectado com COH-PIAH")



