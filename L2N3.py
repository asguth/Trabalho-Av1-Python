#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 

num = float(input("\nDigite um número: "))

if (num%1) == 0:
    print("\nSeu número é INTEIRO")
else:
    print("\nSeu número é DECIMAL")
