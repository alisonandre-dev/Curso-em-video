#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print("\033[34mCalculadora de descontos %\033[m")

valor_produto = float(input("Informe o valor do produto \033[34mR$\033[m"))

valor_desconto = (5 / 100) * valor_produto
preco_final = valor_produto - ((5 / 100) * valor_produto)

print("\nFoi aplicado 5% off ao produto")
print(f"O preço do produto foi atualizado de R${valor_produto:.2f} para R${preco_final:.2f}")
print(f"Você economizou R${valor_desconto:.2f}")