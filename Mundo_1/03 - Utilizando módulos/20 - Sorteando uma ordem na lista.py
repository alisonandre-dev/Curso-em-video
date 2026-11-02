# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
print("\033[1;34mSorteando uma ordem da lista\033[m")

aluno_1 = input("Nome do 1° Aluno: ")
aluno_2 = input("Nome do 2° Aluno: ")
aluno_3 = input("Nome do 3° Aluno: ")
aluno_4 = input("Nome do 4° Aluno: ")

lista_de_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_de_alunos)

print(f"\nA Ordem de apresentação será a seguinte:")
print(f"1° {lista_de_alunos[0]}")
print(f"2° {lista_de_alunos[1]}")
print(f"3° {lista_de_alunos[2]}")
print(f"4° {lista_de_alunos[3]}")