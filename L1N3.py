#3. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
#no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
#11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos 
#dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

import time
import os

trah = eval(input("\n Quanto você ganha por hora?: "))
os.system("clear")
tram = eval(input("\n Quantas horas você trabalhada no mês?: "))
os.system("clear")

salb = trah * tram

ir = salb * 0.11
inss = salb * 0.08
sind = salb * 0.05

sall = salb - ir - inss - sind

time.sleep(0.5)
print (f"\n Salário Bruto   : R$ {salb:.2f}")
time.sleep(0.5)
print (f" IR (11%)        : R$ {ir:.2f}")
time.sleep(0.5)
print (f" INSS (8%)       : R$ {inss:.2f}")
time.sleep(0.5)
print (f" Sindicato (5%)  : R$ {sind:.2f}")
time.sleep(0.5)
print (f" Salário Liquido : R$ {sall:.2f}")
time.sleep(0.5)
