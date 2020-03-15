'''
Q3 - Dada uma lista L de números inteiros, escreva uma função retorne uma lista P contendo todos os
itens de L acrescidos em 10%.
'''

def acrescentar10PorCento(L):
    P = [x * 1.10 for x in L] # CRIACAO IMPLICITA
    return P    

L = [10,15,100,120,180,250,500,750,900,10000]
print(acrescentar10PorCento(L))



