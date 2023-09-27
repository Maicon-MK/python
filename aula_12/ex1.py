#Seletor de aluno
#1)Escreva um programa que premita selecionar um aluno aleatorio de um arquivo txt
#2)Permita que programa adcionar um aluno a lista 
#3)Permita que o programa remova um aluno da lista

import random

def selecionar_aluno_aleatorio():
    with open('alunos.txt', 'r') as arquivo:
        lista_alunos = arquivo.readlines()
        return random.choice(lista_alunos).strip()  

def adicionar_aluno(nome):
    with open('alunos.txt', 'a') as arquivo:
        arquivo.write(nome + '\n')

def remover_aluno(nome):
    with open('alunos.txt', 'r') as arquivo:
        lista_alunos = arquivo.readlines()
    with open('alunos.txt', 'w') as arquivo:
        arquivo.writelines([aluno for aluno in lista_alunos if aluno.strip() != nome])


while True:
    print("\nEscolha uma opção:")
    print("1 - Selecionar um aluno aleatório")
    print("2 - Adicionar um aluno")
    print("3 - Remover um aluno")
    print("4 - Sair")
    
    opcao = input("Opção: ")

    if opcao == '1':
        aluno_aleatorio = selecionar_aluno_aleatorio()
        print(f"Aluno selecionado aleatoriamente: {aluno_aleatorio}")
    elif opcao == '2':
        novo_aluno = input("Digite o nome do aluno a ser adicionado: ")
        adicionar_aluno(novo_aluno)
        print(f"Aluno '{novo_aluno}' adicionado à lista.")
    elif opcao == '3':
        aluno_a_remover = input("Digite o nome do aluno a ser removido: ")
        remover_aluno(aluno_a_remover)
        print(f"Aluno '{aluno_a_remover}' removido da lista.")
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
