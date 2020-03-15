'''
Q4 - .Dada uma lista L de números inteiros, escreva uma função que imprima os itens de L de trás para
frente, sem utilizar reverse().
'''


def reveterItensLista(L):   
    for x in range(1, len(L) + 1):
        #eu tenho que fazer algo como ... L[-1] depois L[-2] até a quantidade de indices...
        print(L[-x])
        
    
L = [10, 30, 20, 50, 40 , 70, 60 , 90, 80, 100]
reveterItensLista(L)
