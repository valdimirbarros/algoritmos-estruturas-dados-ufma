'''
Q3 - Escreva um programa que escolha aleatoriamente um número entre 0 e 10, ao qual o usuário deve
tentar adivinhar. O jogo acaba quando o usuário acerta ou quando ele desiste (digitando 0).
'''

from random import randint


def RamdomGame():
    x=-1
    while x!=randint(0,10):
        x = int(input("Digite um valor: "));
        print("Tente Novamente! :(")
    print("Você ganhou!!!!!")   

RamdomGame()