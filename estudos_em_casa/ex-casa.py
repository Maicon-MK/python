#Estrutura With

#Sem with       arquivo     wirte para ler
arquivo = open("nomes.txt","w" )
arquivo.write("Michael")

arquivo.close()

#com whit
with open("nomes.txt") as arquivo:
    arquivo.write("Para escrever")
with open("nomes.txt", 'r') as arquivo:
    print(arquivo.read())