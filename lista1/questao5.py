'''
Q5 - Escreva um programa que some todos os números entre 0 e 99.
'''

def Soma99():
    soma=0
    x=0
    while x<=99:
        soma = soma+x
        x+=1
    print("A soma de todos os numeros de 0 a 99 é: {}".format(soma)) 

Soma99()