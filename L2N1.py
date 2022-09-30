#1. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do 
#saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão 
#as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa 
#não deve se preocupar com a quantidade de notas existentes na máquina.
#a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
#uma nota de 50, uma nota de 5 e uma nota de 1;
#b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
#uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

import time
import os

print("\nBem vindo ao seu caixa eletrônico")
time.sleep(2)
os.system("clear")

num = int(input("\nValor para sacar Mínimo: R$10 | Máximo R$600: "))

n100 = int(num/100)
num -= (n100*100)
    
n50 = int(num/50)
num -= (n50*50)

n10 = int(num/10)
num -= (n10*10)

n5 = int(num/5)
num -= (n5*5)

n1 = num

os.system("clear")
print(f"\nNotas R$100,00 = " ,n100)
print(f"Notas R$ 50,00 = " ,n50)
print(f"Notas R$ 10,00 = " ,n10)
print(f"Notas R$  5,00 = " ,n5)
print(f"Notas R$  1,00 = " ,n1)
time.sleep(60)
