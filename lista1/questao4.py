'''
Q4 - Escreva um programa que calcule e mostre o seno dos ângulos entre 0 e 360 (de 10 em 10).
Dica: Use a função sin do pacote math
'''

import math

def Senos():
    x=0
    while x<=360:
       print("seno do Angulo {}º é: {}".format(x,math.sin(x)))
       x+=10   

Senos()