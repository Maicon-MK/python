"Crie um programa onde 4 Jogadores jogam um dado guarde esses resusltados em um dicionario no final, coloque em orge"

import random

jogadores = {
    "Jogador1": random.randint(1, 10),
    "Jogador2": random.randint(1, 10),
    "Jogador3": random.randint(1, 10),
    "Jogador4": random.randint(1, 10)
}

pairs = []
for k, v in jogadores.items():
    pairs.append((k, v))


pairs.sort(key=lambda item: item[1], reverse=False)

result = []
for k, v in reversed(pairs):
    result.append((k, v))  
print(result)
