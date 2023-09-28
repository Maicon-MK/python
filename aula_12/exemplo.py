import csv
import random
import tkinter as tk
from tkinter import messagebox

def carregar_nomes():
    nomes = []
    try:
        with open("nomes.csv", newline='') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                nomes.append(linha)
    except FileNotFoundError:
        pass
    return nomes

def salvar_nomes(nomes):
    with open("nomes.csv", 'w', newline='') as arquivo:
        nomes_campos = ["nome", "cidade"]
        escritor = csv.DictWriter(arquivo, fieldnames=nomes_campos)
        escritor.writeheader()
        for nome in nomes:
            escritor.writerow(nome)

def adicionar_aluno():
    nome = entry_nome.get()
    cidade = entry_cidade.get()
    
    if nome and cidade:
        nomes = carregar_nomes()
        nomes.append({"nome": nome, "cidade": cidade})
        salvar_nomes(nomes)
        messagebox.showinfo("Sucesso", f"Aluno adicionado: {nome} de {cidade}")
        entry_nome.delete(0, tk.END)
        entry_cidade.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

def selecionar_aleatorio():
    nomes = carregar_nomes()
    if nomes:
        aluno_aleatorio = random.choice(nomes)
        messagebox.showinfo("Aluno Aleatório", f"Aluno selecionado aleatoriamente: {aluno_aleatorio['nome']} de {aluno_aleatorio['cidade']}")
    else:
        messagebox.showerror("Erro", "Nenhum aluno na lista.")

def remover_aluno():
    nomes = carregar_nomes()
    if nomes:
        alunos = [f"{aluno['nome']} de {aluno['cidade']}" for aluno in nomes]
        opcao = tk.simpledialog.askstring("Remover Aluno", "Escolha o aluno a ser removido:\n\n" + "\n".join(alunos))
        if opcao:
            try:
                indice_remover = alunos.index(opcao)
                aluno_removido = nomes.pop(indice_remover)
                salvar_nomes(nomes)
                messagebox.showinfo("Sucesso", f"Aluno removido: {aluno_removido['nome']} de {aluno_removido['cidade']}")
            except ValueError:
                messagebox.showerror("Erro", "Aluno não encontrado.")
    else:
        messagebox.showerror("Erro", "Nenhum aluno na lista.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Gestão de Alunos")


# Rótulos e campos de entrada
label_nome = tk.Label(janela, text="Nome do Aluno:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_cidade = tk.Label(janela, text="Cidade do Aluno:")
label_cidade.pack()
entry_cidade = tk.Entry(janela)
entry_cidade.pack()

# Botões
btn_adicionar = tk.Button(janela, text="Adicionar Aluno", command=adicionar_aluno)
btn_adicionar.pack()

btn_selecionar_aleatorio = tk.Button(janela, text="Selecionar Aleatório", command=selecionar_aleatorio)
btn_selecionar_aleatorio.pack()

btn_remover = tk.Button(janela, text="Remover Aluno", command=remover_aluno)
btn_remover.pack()

# Iniciar a interface gráfica
janela.mainloop()
