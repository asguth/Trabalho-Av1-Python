#1. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu 
#peso ideal, utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7

import os

sex = input("\nQual seu sexo? Masculino (M) ou Feminino (F)? ")
h = input("\nDigite sua altura: ")
os.system("clear")

pesom = (72.7 * float(h)) - 58
pesof = (62.1 * float(h)) - 44.7

if sex == "M" or sex == "m" or sex == "masculino" or sex == "Masculino":
    print("\nSeu peso ideal é %.2f: " % pesom)
elif sex == "F" or sex == "f" or sex == "feminino" or sex == "Feminino":
    print("\nSeu peso ideal é %.2f: " % pesof)
else:
    print("\nSexo inválido!")
