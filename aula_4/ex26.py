# informe um aumento de 15% do salário do usuario

print('Este programa ira informar um aumento no seu salário de 15%.')

salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario + salario * 0.15
    val_aumento = 15

else:
    aumento = salario + salario * 0.10
    val_aumento = 10

print(f'Você ganhou um aumento de {val_aumento}%\n'
      f'Seu salário agora é {aumento} RS.')