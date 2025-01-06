# Sem pandas
import csv

filtered_data = []
with open('CSV~/funcionarios.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    filtered_data.append(header)

    for row in reader:
        if row[2] == 'Financeiro':
            filtered_data.append(row)

with open('CSV~/financeiro.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_data)