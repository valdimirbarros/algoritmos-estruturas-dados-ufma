'''
Q1 - Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P contendo os números pares de L. 
Observação: utilize criação implícita de listas
'''
def buscarPares(L):
    P = [x for x in L if x%2 == 0]
    return P

L = [1,2,3,4,5,6,7,8,9,10]
print(buscarPares(L))

