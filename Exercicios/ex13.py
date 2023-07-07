#Crie um conversor de temperatura (°C °F K )

C = int(input("Quantos C°: "))
para_f =(C*9/5 + 32)
para_k = (C+273,15)

print(
    f"Sua temperatura e de: {C} C° (Graus Celcius)\n "
    f"Convertendo para Fahtenheit: {para_f}\n"
    f"Convertendo para Kelvin: {para_k}"
    )

