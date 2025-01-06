# Sem pandas
import json

with open('JASON/livros.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

livros_ficcao = [livro for livro in data if livro['categoria'] == 'Ficção']

with open('JASON/livros_ficcao.json', 'w', encoding='utf-8') as file:
    json.dump(livros_ficcao, file, ensure_ascii=False, indent=4)

if livros_ficcao:
    print('Livros na categoria "Ficção:"')
    for livro in livros_ficcao:
        print(livro)
else:
    print('Nenhum livro encontrado na categoria "Ficção".')   