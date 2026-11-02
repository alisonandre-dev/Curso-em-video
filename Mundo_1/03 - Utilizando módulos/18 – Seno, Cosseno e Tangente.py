# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

print("\033[1;34mSeno, Cosseno e Tangente de um ângulo\033[m")

angulo = float(input("Escreva um ângulo que deseja consultar: "))

# Precisamos converter para radianos
tangente = math.radians(angulo)

print(f"\nO ângulo de {angulo} possui:")
print(f"Seno de {math.sin(tangente):.2f}")
print(f"Cosseno de {math.cos(tangente):.2f}")
print(f"Tangente de {math.tan(tangente):.2f}")

