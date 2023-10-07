import criar_listas

# Nome do arquivo onde as listas estão armazenadas
nome_arquivo = "listas.json"

# Carregue as listas do arquivo
listas_carregadas = criar_listas.carregarLista(nome_arquivo)

# Determine o número de listas no arquivo
numero_de_listas = len(listas_carregadas)

# Acesse as listas individualmente e imprima seu comprimento
for i, lista in enumerate(listas_carregadas):
    print(f"Lista{i+1} tem {len(lista)} elementos.")