'''
Q5 - Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P contendo os
itens de L sem repetição.
'''

def removeRepetidos(L):
    P = [] 
    for x in L:
        if x not in P: #SE O ELEMENTO X NAO EXISTIR NA LISTA P ELE ADICIONA. DESSA FORMA A LISTA P NAO RECEBERA ELEMENTOS REPETIDOS
            P.append(x)
    return P    
    
L = [1,2,2,3,4,4,4,5,6,6,6,6,7,8,8,8,8,8,9,10,10,10,10,10,10] # LISTA QUE REPETE OS PARES...
print(removeRepetidos(L))
