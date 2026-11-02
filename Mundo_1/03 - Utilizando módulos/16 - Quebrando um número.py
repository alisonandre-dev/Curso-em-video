# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
print("\033[1;34mPorção inteira de um número\033[m")

numero = float(input("Informe um valor: "))

print(f"\nA porção inteida de \033[34m{numero}\033[m é \033[1;34m{trunc(numero)}\033[m")