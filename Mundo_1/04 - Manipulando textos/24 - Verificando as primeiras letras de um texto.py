# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
print("\033[1;34mBuscando a palavra SANTO\033[m")

cidade = input("Digite a cidade em que você nasceu: ")

cidade = cidade.strip().upper()

palavra = cidade.split()

print("\nA cidade digitada inicia com SANTO?",palavra[0] == "SANTO")