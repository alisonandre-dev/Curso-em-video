# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print("\033[34mConversor de médidas\033[m")

metros = float(input("Informe uma distância em metros: "))

mm = metros * 1000
cm = metros * 100
km = metros / 1000


print("\033[34m\nConvenssões\033[m")

print("Centímetros: ", cm, "cm")
print("Milímetros: ", mm, "mm")
print("Quilômetros: ", km, "km")