# Sem pandas
import csv 

try:
    with open('CSV~/funcionarios.csv', mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        print('Cabeçalho:', header)

        for row in reader:
            print(row)
except FileNotFoundError:
    print('Erro: O arquivo "funcionarios.csv" não foi encontrado.')
except Exception as e:
    print(f'Erro ao ler o arquivo: {e}')