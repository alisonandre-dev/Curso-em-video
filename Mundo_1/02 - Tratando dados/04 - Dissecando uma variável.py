# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

 
print("\033[34mSomando dois números\033[m")

dado = input("Digite algo: ")


print("\nTodos os caracteres são númericos:", dado.isnumeric())
print("Todos os caracteres são alfabéticos:", dado.isalpha())
print("Todos os caracteres são númericos ou alfabéticos:", dado.isalnum())

print("\nTodos os caracteres estão menúsculos:", dado.islower())
print("Todos os caracteres estão maiúsculos:", dado.isupper())
print("Todos os caracteres estão formatados para títulos:", dado.istitle())
