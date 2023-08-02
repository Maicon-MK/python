import sys #Importando a Blibioteca


if len(sys.argv) > 2:#O usuario adcionar mais de dois argumentos
    sys.exit("Muitos argumentos") #Encerre o programa e "print" a mensagem 
elif len(sys.argv) <2:#Se o usuario adcionar menos de dois comentarios "print" a mensagem
    sys.exit("Poucos argumentos")#Encerre o programa e printe a mensagem 


print("Meu nome e:" ,sys.argv[1])