# Com pandas
import pandas as pd

try:
    df = pd.read_csv('CSV~/funcionarios.csv')
    print(df.head())
except FileNotFoundError:
    print('Erro: O arquivo "funcionarios.csv" não foi encontrado.')
except pd.errors.EmptyDataError:
    print('Erro: O arquivo está vazio.')
except pd.errors.ParserError:
    print('Erro: O arquivo tem um formato inválido.')
except Exception as e:
    print(f'Erro ao ler o arquivo: {e}')