# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print("\033[34mConversor de temperaturas 🌡️\033[m")

celsius = float(input("Digite uma temperatura em celsius °C: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"\n{celsius}°c celsius equivale á")
print(f"{fahrenheit}F fahrenheit")
print(f"{kelvin}K kelvin")