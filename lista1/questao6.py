'''
Q6 - Escreva um programa que mostre todos os múltiplos de 5 entre 0 e 50.

'''

def Mult5():
    x=0
    while x<=50:
        if(x%5==0):
            print(x)
            x+=1
        else:
            x+=1 

Mult5()