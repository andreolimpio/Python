# ============================================
# SISTEMA DE ESTOQUE - DESAFIO PYTHON
# ============================================
# Este programa utiliza:
# - listas
# - dicionários
# - funções
# - laços (while e for)
# - métodos como append, remove, sort, reverse, len
# ============================================

# Lista principal que armazenará os produtos
estoque = []


# ============================================
# FUNÇÃO 1 - CADASTRAR PRODUTO
# ============================================
def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")

    # Entrada de dados do usuário
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade em estoque: "))

    # Criando o dicionário do produto
    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    # Adicionando o produto na lista
    estoque.append(produto)

    print("Produto cadastrado com sucesso!")


# ============================================
# FUNÇÃO 2 - LISTAR PRODUTOS
# ============================================
def listar_produtos():
    print("\n--- Lista de Produtos ---")

    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return

    # Percorrendo a lista com for
    for i, produto in enumerate(estoque, start=1):
        print(f"{i} - {produto['nome']} | {produto['categoria']} | "
              f"R${produto['preco']:.2f} | Estoque: {produto['quantidade']}")


# ============================================
# FUNÇÃO 3 - BUSCAR PRODUTO
# ============================================
def buscar_produto():
    print("\n--- Buscar Produto ---")

    nome_busca = input("Digite o nome do produto: ")

    for produto in estoque:
        if produto["nome"].lower() == nome_busca.lower():
            print("\nProduto encontrado:")
            print(produto)
            return

    print("Produto não encontrado.")


# ============================================
# FUNÇÃO 4 - ATUALIZAR QUANTIDADE
# ============================================
def atualizar_quantidade():
    print("\n--- Atualizar Quantidade ---")

    listar_produtos()

    try:
        indice = int(input("Escolha o número do produto: ")) - 1

        if 0 <= indice < len(estoque):
            nova_qtd = int(input("Nova quantidade: "))
            estoque[indice]["quantidade"] = nova_qtd
            print("Quantidade atualizada!")
        else:
            print("Índice inválido.")
    except:
        print("Entrada inválida.")


# ============================================
# FUNÇÃO 5 - REMOVER PRODUTO
# ============================================
def remover_produto():
    print("\n--- Remover Produto ---")

    listar_produtos()

    try:
        indice = int(input("Escolha o número do produto: ")) - 1

        if 0 <= indice < len(estoque):
            # Removendo usando pop()
            removido = estoque.pop(indice)
            print(f"Produto '{removido['nome']}' removido.")
        else:
            print("Índice inválido.")
    except:
        print("Entrada inválida.")


# ============================================
# FUNÇÃO 6 - ORDENAR PRODUTOS
# ============================================
def ordenar_produtos():
    print("\n--- Ordenar Produtos ---")
    print("1 - Ordenar por nome")
    print("2 - Ordenar por preço")

    opcao = input("Escolha: ")

    if opcao == "1":
        estoque.sort(key=lambda x: x["nome"])
        print("Ordenado por nome.")
    elif opcao == "2":
        estoque.sort(key=lambda x: x["preco"])
        print("Ordenado por preço.")
    else:
        print("Opção inválida.")


# ============================================
# FUNÇÃO 7 - MOSTRAR INVERTIDO
# ============================================
def mostrar_invertido():
    print("\n--- Lista Invertida ---")

    # Criando uma cópia para não alterar a original
    lista_invertida = estoque.copy()
    lista_invertida.reverse()

    for produto in lista_invertida:
        print(produto)


# ============================================
# FUNÇÃO 8 - ESTATÍSTICAS DO ESTOQUE
# ============================================
def estatisticas_estoque():
    print("\n--- Estatísticas ---")

    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return

    total_produtos = len(estoque)

    # Valor total do estoque
    valor_total = sum(p["preco"] * p["quantidade"] for p in estoque)

    # Produto mais caro
    mais_caro = max(estoque, key=lambda x: x["preco"])

    # Produto com maior quantidade
    maior_qtd = max(estoque, key=lambda x: x["quantidade"])

    print(f"Total de produtos: {total_produtos}")
    print(f"Valor total do estoque: R${valor_total:.2f}")
    print(f"Produto mais caro: {mais_caro['nome']}")
    print(f"Maior quantidade em estoque: {maior_qtd['nome']}")


# ============================================
# MENU PRINCIPAL (WHILE)
# ============================================
def menu():
    while True:
        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar quantidade")
        print("5 - Remover produto")
        print("6 - Ordenar produtos")
        print("7 - Mostrar produtos invertidos")
        print("8 - Estatísticas do estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            remover_produto()
        elif opcao == "6":
            ordenar_produtos()
        elif opcao == "7":
            mostrar_invertido()
        elif opcao == "8":
            estatisticas_estoque()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# ============================================
# EXECUÇÃO DO PROGRAMA
# ============================================
menu()