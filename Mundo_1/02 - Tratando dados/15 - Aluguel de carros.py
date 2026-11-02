# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print("\033[34mCalculadora de aluguel\033[m")

dias = float(input("Quantos dias você ficou com o veículo: "))
km = float(input("Quantos KM você rodou: "))

preco_total_dias = dias * 60
preco_total_km = km * 0.15

custo_total = preco_total_dias + preco_total_km

print(f"\nValor total a pagar R${custo_total:.2f}")