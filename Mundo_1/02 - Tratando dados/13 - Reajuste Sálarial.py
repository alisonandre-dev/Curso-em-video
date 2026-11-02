# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print("\033[34mReajuste Salárial\033[m")

salario_atual = float(input("Informe seu salário atual \033[34mR$\033[m"))

valor_do_aumento = (15 / 100) * salario_atual
salario_final = salario_atual + ((15 / 100) * salario_atual)

print("\nSeu salário foi reajustado em 15%")
print(f"Parabéns, você recebeu um aumento de R${valor_do_aumento:.2f}")
print(f"Seu novo salário agora será de R${salario_final:.2f}")