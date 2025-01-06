# Com pandas
import pandas as pd

df = pd.read_json('JASON/livros.json')

livros_fantasia = df[df['categoria'] == 'Fantasia']

livros_fantasia.to_json('JASON/livros_fantasia.json', orient='records', lines=False, force_ascii=False)

if not livros_fantasia.empty:
    print('Livros na categoria "Fantasia":')
    print(livros_fantasia.to_dict(orient='records'))
else:
    print('Nenhum livro encontrado na categoria Fantasia.')