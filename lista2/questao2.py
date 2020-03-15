'''
Q2 - Dada uma lista L de números inteiros, escreva uma função que imprima todos os números de
índices múltiplos de 3.
'''

def buscarNumerosIndiceMult3(L):
    for indice in range(len(L)):
        if  indice % 3  == 0:
            print(indice)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
buscarNumerosIndiceMult3(L)
