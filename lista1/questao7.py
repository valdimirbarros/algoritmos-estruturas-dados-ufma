'''
Q7 - Escreva um programa que mostre os dias da semana.
'''

import datetime

def DiaSemana():
    x = int(input("Digite o dia: "))
    y = int(input("Digite o mês: "))
    z = int(input("Digite o Ano: "))
    k = 0
    while k<7:
        dt = datetime.datetime(year=z, month=y, day=x+k)
        str_dt = dt.strftime("%a")
        print(str_dt)
        k+=1

DiaSemana()