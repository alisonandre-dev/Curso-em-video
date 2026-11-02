# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt, hypot
print("\033[1;34mCálculando a hipotenusa\033[m")

oposto = float(input("Informe o comprimendo do cateto oposto: "))
adjacente = float(input("Informe o comprimendo do cateto adjacente: "))

hipotenusa = hypot(oposto, adjacente)

# hipotenusa = √(a² + b²)
# hipotenusa = sqrt(oposto ** 2 + adjacente ** 2)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")