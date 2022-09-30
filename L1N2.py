#2. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o 
#estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma 
#multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a 
#variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade 
#de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima 
#os dados do programa com as mensagens adequadas.

import time
import os

print ("\nRendimento Diário Peixe")
time.sleep(2)
os.system("clear")

print ("\nBem Vindo João")
time.sleep(2)
os.system("clear")

pesop = eval(input("\nQuantos kilos de peixe pescou hoje?: "))
os.system("clear")

if pesop  > 50:
    exc = pesop - 50
    multa = 4 * exc

print(f"\nHoje você pescou: {pesop}Kg de peixes")
time.sleep(2)
print(f"\n Excesso da quantidade de quilos além do limite: {exc}Kg")
time.sleep(2)
print(f"\n Multa à pagar: R${multa:.2f}")
time.sleep(2)
