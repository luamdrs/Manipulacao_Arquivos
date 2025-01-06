# Com pandas
import pandas as pd

df = pd.read_csv('CSV~/funcionarios.csv')
df_financeiro = df[df['departamento'] == 'TI']
df_financeiro.to_csv('CSV~/TI.csv', index=False)