# Faça um programa que leia a quantidade de dias e km rodados por um carro alugado, depois calcule o valor do contrato
# sabendo que cada dia custa 60 reais e cada km custa 15 centavos

dias = int(input('Digite quantos dias o carro andou: '))
km = float(input('Digite quantos kilometros foram rodados: '))

custo = dias * 60 + km * 0.15

print(f'O custo do aluguel ficou em {custo}')