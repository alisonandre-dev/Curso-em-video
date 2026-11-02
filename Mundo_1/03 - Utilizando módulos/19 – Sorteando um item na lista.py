# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
print("\033[1;34mSorteando um aluno\033[m")

aluno_1 = input("Nome do 1° Aluno: ")
aluno_2 = input("Nome do 2° Aluno: ")
aluno_3 = input("Nome do 3° Aluno: ")
aluno_4 = input("Nome do 4° Aluno: ")

lista_de_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

aluno_sorteado = choice(lista_de_alunos)

print(f"\nO Aluno escolhido foi \033[34m{aluno_sorteado}\033[m")