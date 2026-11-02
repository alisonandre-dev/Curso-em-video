# Desenvolva um programa que leia as quatro notas de um aluno, calcule e mostre a sua média.

print("\033[34mCalculando a média\033[m")

n1 = float(input("Informe a 1° nota: "))
n2 = float(input("Informe a 2° nota: "))
n3 = float(input("Informe a 3° nota: "))
n4 = float(input("Informe a 4° nota: "))

total = n1 + n2 + n3 + n4
media = total / 4

print(f"\nA sua média aritimétia foi \033[32m{media}\033[m")