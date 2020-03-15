'''
Q8 - Faça um programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20
elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras
listas.
'''

def intercalarElementos(L1,L2):
    L3 = []
    for x in range(0,10):
        L3.append(L1[x])
        L3.append(L2[x])
    return L3

#REFATORAR!!!
# LISTA COM NUMEROS PARES E IMPARES DESORGANIZADOS...
L1 = [1,2,3,4,5,6,7,8,9,10]
L2 = [10,20,30,40,50,60,70,80,90,100]

print(intercalarElementos(L1,L2))
