# Com pandas
import pandas as pd

df = pd.read_json('JASON/filmes.json')

filmes_drama = df[df['genero'] == 'Drama']

filmes_drama.to_json('JASON/filmes_drama.json', orient='records', lines=False, force_ascii=False)

if not filmes_drama.empty:
    print('Filmes no gênero "Drama":')
    print(filmes_drama.to_dict(orient='records'))
else:
    print('Nenhum filme encontrado no gênero Drama.')