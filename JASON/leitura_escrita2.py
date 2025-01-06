# Sem pandas
import json

with open('JASON/filmes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

filmes_ficcao_cientifica = [filme for filme in data if filme['genero'] == 'Ficção Científica']

with open('JASON/filmes_ficcao_cientifica.json', 'w', encoding='utf-8') as file:
    json.dump(filmes_ficcao_cientifica, file, ensure_ascii=False, indent=4)

if filmes_ficcao_cientifica:
    print('Filmes no gênero Ficção Científica:')
    for filme in filmes_ficcao_cientifica:
        print(filme)
else:
    print('Nenhum filme encontrado no gênero Ficção Científica.')