'''
Q1 - Escreva um algoritmo que leia um valor em real e mostre o valor em dólar.
'''
def ConvDolar():
    valor = float(input("Digite o valor em reais: "))
    conv = valor/5.5
    print('o valor em dóslar será: {}'.format(conv))

ConvDolar()    