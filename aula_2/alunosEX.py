name = []
with open('nomes.txt', 'a') as file:
   lines = file.readline().strip
for line in lines:
   print(line)