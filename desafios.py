import time

def converter_data_hora_para_timestamp(data_hora_str):
    # Converter a string de data e hora para um timestamp em segundos

    #A função strptime é usada para analisar uma string de data e hora e transformá-la em um objeto de data e hora.
    #Ela recebe dois argumentos: a string contendo a data e hora a ser analisada e um formato especificando como a data e hora estão estruturadas na string.
    #O formato é definido usando códigos de formatação, como %Y para o ano, %m para o mês, %d para o dia, %H para a hora em formato 24 horas, %M para os minutos e %S para os segundos.""""
    
    timestamp = int(time.mktime(time.strptime(data_hora_str, '%Y-%m-%d %H:%M:%S')))
    return timestamp

# Exemplo de uso
data_hora_str = input("Digite a data e hora no formato 'AAAA-MM-DD HH:MM:SS': ")
timestamp = converter_data_hora_para_timestamp(data_hora_str)
print("Timestamp:", timestamp)
