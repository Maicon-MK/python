# Forma simples, não incorreta, mas inconsistente
# Solicita o nome e a casa do estudante e imprime na tela.
name = input("Nome: ")
home = input("Casa: ")
print(f"{name} de {home}")


# Usando uma função principal (main)
# Função principal que chama outras funções para obter e imprimir as informações do estudante.
def main_1():
    name = get_name()
    home = get_home()
    print(f"{name} de {home}")


def get_name():
    return input("Nome: ")  # Obtém o nome do estudante a partir da entrada do usuário.


def get_home():
    return input("Casa: ")  # Obtém a casa do estudante a partir da entrada do usuário.


# Trabalhando de forma mais inteligente com tuplas
# Função principal que chama outras funções para obter e imprimir as informações do estudante usando tuplas.
def main_2():
    student = get_student_2()  # Chama a função para obter os dados do estudante usando tupla.
    print(f"{student[0]} de {student[1]}")


def get_student_2():
    name = input("Nome: ")  # Obtém o nome do estudante a partir da entrada do usuário.
    home = input("Casa: ")  # Obtém a casa do estudante a partir da entrada do usuário.
    return (name, home)  # Retorna um valor com 2 valores (tupla) contendo o nome e a casa do estudante.


# Como sobrescrever um erro usando listas
# Função principal que chama outras funções para obter e imprimir as informações do estudante usando listas.
def main_3():
    student = get_student_3()  # Chama a função para obter os dados do estudante usando lista.
    if student[0] == "Rodrigo":  # Verifica se o nome do estudante é "Rodrigo".
        student[1] = "Vila Isabel"  # Se o nome for "Rodrigo", sobrescreve o valor da casa para "Vila Isabel".
    print(f"{student[0]} de {student[1]}")


def get_student_3():
    name = input("Nome: ")  # Obtém o nome do estudante a partir da entrada do usuário.
    home = input("Casa: ")  # Obtém a casa do estudante a partir da entrada do usuário.
    return [name, home]  # Retorna uma lista com o nome e a casa do estudante.


# Usando dicionários para ser mais limpo
# Função principal que chama outras funções para obter e imprimir as informações do estudante usando dicionários.
def main_4():
    student = get_student_4()  # Chama a função para obter os dados do estudante usando dicionário.
    if student["name"] == "Rodrigo":  # Verifica se o nome do estudante é "Rodrigo".
        student["home"] = "Vila Isabel"  # Se o nome for "Rodrigo", sobrescreve o valor da casa para "Vila Isabel".
    # Certifique-se de usar aspas simples
    print(f"{student['name']} de {student['home']}")


def get_student_4():
    student = {}  # Cria um dicionário vazio para armazenar os dados do estudante.
    student["name"] = input("Nome: ")  # Obtém o nome do estudante a partir da entrada do usuário.
    student["home"] = input("Casa: ")  # Obtém a casa do estudante a partir da entrada do usuário.
    return student  # Retorna um dicionário contendo o nome e a casa do estudante.

# Por que usar variáveis desnecessárias?
# Essa função foi omitida porque não é usada em nenhum lugar do código.


# Criando uma classe
# Classe para representar um estudante com atributos nome e casa.
class Estudante:
    pass  # A palavra-chave 'pass' indica que a classe ainda não possui implementações


def main():
    student = get_student()
    print(f"{student.name} de {student.home}")


def get_student():
    student = Estudante()  # Cria um objeto da classe Estudante.
    # Obtém o nome do estudante a partir da entrada do usuário e armazena no atributo 'name'.
    student.name = input("Nome: ")
    # Obtém a casa do estudante a partir da entrada do usuário e armazena no atributo 'home'.
    student.home = input("Casa: ")
    return student  # Retorna o objeto Estudante contendo o nome e a casa do estudante.


if __name__ == "__main__":
    main()  # Chama a função principal para começar a execução do programa.
