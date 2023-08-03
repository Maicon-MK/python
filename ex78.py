#Classe(Retangulo)

#Crie uma classe chamada "retângulo" que possua o método
#__init__ para icializar  as propiedades "Largura" e "Altura"
#do retangulo.  em seguida, crie um objeto da class "Retangulo"
#E calcule e imprima a area do retangulo. 

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura =  altura
n_largura = 5
n_altura = 10
result = n_largura*n_altura
retangulo = Retangulo(n_largura,n_altura)
print(f"{result}")
        