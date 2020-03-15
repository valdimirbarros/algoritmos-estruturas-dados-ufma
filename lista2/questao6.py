'''
Q6 - Dada uma lista L de números inteiros, escreva uma função que imprima os índices de todas as
ocorrências de um número especificado.
'''


def buscaIndices(L):
    print('LISTA: ', L)
    inteiroInput = int(input('Informe um inteiro de 1 à 10: '))
    #VASCULHA INDICE E ITEM DA LISTA L E COMPARA CADA ITEM COM O ESPECIFICADO PELO USUARIO, CASO SEJA IGUAL RETORNA SEU INDICE...
    for index, item in enumerate(L):
        if item == inteiroInput:
            print('O inteiro foi encontrado no índice: ', index)
                
# LISTA QUE REPETE OS PARES...
L = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 8, 8, 8, 8, 9, 10, 10, 10, 10, 10, 10]
print(buscaIndices(L))
