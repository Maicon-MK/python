# Faça um conversor de celcius para fahrenheit e kelvin.

celcius = int(input('Diga a temperatura em graus Celcius: '))

fahrenheit = (9 * celcius + 160) / 5
kelvin = celcius + 273.15

print(f'A temperatura em Fahrenheit é {fahrenheit} e a temperatura em Kelvins é {kelvin}.')