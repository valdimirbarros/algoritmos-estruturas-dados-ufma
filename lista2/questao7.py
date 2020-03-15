'''
Q7 - Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P com os
valores ordenados de P, agrupados em números pares primeiro e ímpares depois.
'''

def agrupaParImpar(L):
    pares = [x for x in L if x % 2 == 0]
    impares = [x for x in L if x % 2 != 0]
    P = []
    pares.sort()
    impares.sort()
    P.extend(pares)
    P.extend(impares)
    return P

#REFATORAR!!!
# LISTA COM NUMEROS PARES E IMPARES DESORGANIZADOS...
L = [1,3,4,6,8,2,11,25,10,9,15,14,12]
print(agrupaParImpar(L))
