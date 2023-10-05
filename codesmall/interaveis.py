x = [1,2,3,4,5,6,7,8,9,10]

y = map(lambda i: i**2, x)
#O map() função executa um especificado função para cada item em um iterável. 
# O item é enviado para a função como um parâmetro.
for i in y:
    print(i)
while True:
    try:
        value = next(y)
    except StopIteration:
        print('and')
    break