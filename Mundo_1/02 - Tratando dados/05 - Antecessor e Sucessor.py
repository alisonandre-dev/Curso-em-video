# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

print("\033[34mAntecessor e Sucessor de um número\033[m")

numero = int(input("Digite um número inteiro: "))

sucessor = numero + 1
antecessor = numero - 1

print(f"\nSucessor:", sucessor)
print(f"Antecessor:", antecessor)
