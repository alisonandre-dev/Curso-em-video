#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
print("\033[1;34mSeparando digitos\033[m")

numero = int(input("Digite um número inteiro: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"\nO número \033[1;34m{numero}\033[m possui")
print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)