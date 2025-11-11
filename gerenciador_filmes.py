'''
Nome: Carlos Silva
Cursc SENAC RJ Programação Python
Gerenciador de filmes simples com versionamento.
'''

# Peça ao usuário que digite os títulos dos filmes separados por vírgula.
nomes_filmes = input('Digite o nome dos filmes separados por vírgula: ')
lista_filmes = [nome.strip() for nome in nomes_filmes.split(',')]
print()

# Mostre quantos filmes foram cadastrados, o nome do primeiro filme e o nome do último filme.
print(f'Foram cadastrados {len(lista_filmes)} filmes.')
print(f'O nome do primeiro filme da lista é: {lista_filmes[0]}')
print(f'O nome do último filme da lista é: {lista_filmes[-1]}')
print()

# Peça ao usuário para adicionar mais um filme no final da lista.
filme_final_da_lista = input('Digite o nome do filme que será inserido no final da lista: ')
lista_filmes.append(filme_final_da_lista)
print()

# Peça ao usuário para adicionar um filme no início da lista.
filme_inicio_da_lista = input('Digite o nome do filme que será inserido no início da lista: ')
lista_filmes.insert(0, filme_inicio_da_lista)
print()

# Peça ao usuário para remover um filme pelo nome.
while True:
    nome_filme_removido = input('Digite o nome do filme que será removido: ').strip()
    nome_filme_removido_lower = nome_filme_removido.lower()
    lista_filmes_lower = [filme.lower() for filme in lista_filmes]
    if nome_filme_removido_lower in lista_filmes_lower:
        indice_filme_removido = lista_filmes_lower.index(nome_filme_removido_lower)
        nome_filme_removido_na_lista = lista_filmes[indice_filme_removido]
        lista_filmes.remove(nome_filme_removido_na_lista)
        print(f'O filme "{nome_filme_removido_na_lista}" foi removido da lista.\n')
        break
    else:
        print(f'O filme "{nome_filme_removido}" não está na lista.')
    print()

# Mostre a lista de filmes em ordem alfabética.
lista_filmes.sort()
print(f'Lista dos filmes em ordem alfabética: {lista_filmes}')
for filme in lista_filmes:
    print(filme)
print()

# Inverta a ordem da lista e mostre o resultado.
lista_filmes.reverse()
print(f'Lista dos filmes na ordem inversa: {lista_filmes}')
for filme in lista_filmes:
    print(filme)
print()

# Faça uma cópia da lista original para a variável copia_filmes e limpe a original com clear.
copia_filmes = lista_filmes.copy()
lista_filmes.clear()

# Mostre ambas as listas para o usuário.
print(f'Cópia da Lista de filmes: {copia_filmes}')
print(f'Lista original após o "clear": {lista_filmes}')

