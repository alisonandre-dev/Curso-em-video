# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print("\033[34mCálculando a área\033[m")

print("\033[1mAbaixo informe as dimenções\033[m")
largura = float(input("Larguda mt: "))
altura = float(input("Altura mt: "))

area = largura * altura
rendimento = area / 2

print(f"\nA área total a ser pintada é de \033[31m{area}m²\033[m")
print(f"Será necessário \033[31m{rendimento:.2f} Litros\033[m de tinta para pinta toda a área")