#Faça um programa que leia o preço de um produto e retorne
#o seu preço com 5%de desconto 

produto = int(input("Quanto custa o produto: "))
q_desconto = int(input("Desconto de:  "))
valor_produto = (produto*q_desconto/100)

print(
    f"Seu produto {produto} \n " 
    f"Desconto {valor_produto}\n"
    f"Ficando no total de: {produto-valor_produto}"
    )

