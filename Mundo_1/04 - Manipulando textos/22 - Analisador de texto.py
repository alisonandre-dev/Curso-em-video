# Crie um programa que leia o nome completo de uma pessoa e mostre:

# 1. O nome com todas as letras maiúsculas e minúsculas.

# 2. Quantas letras ao todo (sem considerar espaços).

# 3. Quantas letras tem o primeiro nome.

print("\033[1;34mAnalisando seu nome\033[m")

nome_completo = input("Informe o seu nome completo: ")

total_caracteres = nome_completo.replace(" ", "")
nome_fatiado = nome_completo.split()

print("\n\033[1;34mEsses são os dados analisado 🎲\033[m")
print("Seu nome em maiúsculo:", nome_completo.upper())
print("Seu nome em minúsculo:", nome_completo.lower())
print(f"Ao todo seu nome possui {len(total_caracteres)} letras")
print(f"Seu primeiro nome possui {len(nome_fatiado[0])} letras")