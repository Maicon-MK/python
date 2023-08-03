#Classe "Cachorro" que possua o método 
#__int__ para inicializar as propiedades "Nome" e "Idade"
#do cachorro. Em seguida, crie um objeto da classe "Cachorro"
#e imprima o nome ea idade do cachorro.


#Atributos do cachorro 

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Solicitar o nome e a idade do cachorro ao usuário
nome_cachorro = input("Digite o nome do cachorro: ")
idade_cachorro = int(input("Digite a idade do cachorro: "))

# Criar o objeto da classe "Cachorro"
cachorro = Cachorro(nome_cachorro, idade_cachorro)
        
print(f"O nome do seu cachorro é {cachorro.nome} e a idade é {cachorro.idade}.")
