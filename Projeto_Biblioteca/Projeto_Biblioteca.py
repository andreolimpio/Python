# ================================================================
# SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ESCOLAR
# ================================================================
# Autor: André Olímpio
# ================================================================
# Este projeto foi desenvolvido em Python e demonstra os seguintes conceitos:
# - Variáveis simples
# - Estruturas condicionais
# - Estruturas de repetição
# - Estrutura de múltipla escolha (match-case)
# - Variáveis compostas (listas, matrizes e dicionários)
# - Recursividade
# - Manipulação de arquivos externos (CSV)
# ================================================================

import csv   # Módulo para trabalhar com arquivos CSV
import os    # Módulo para comandos do sistema (limpar tela, etc.)

# FUNÇÕES AUXILIARES
def limpar_tela():
    """Limpa a tela do terminal, dependendo do sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Recursividade: percorre a lista recursivamente, somando 1 para cada livro disponível.
# Esta função conta quantos livros estão disponíveis na lista.
def contar_disponiveis(livros, indice=0):
    if indice == len(livros):
        return 0
    disponivel = 1 if livros[indice]["disponivel"] else 0
    return disponivel + contar_disponiveis(livros, indice + 1)

# FUNÇÕES DE ARQUIVOS
def carregar_dados(nome_arquivo):
    """Lê os dados de um arquivo CSV e devolve uma lista de dicionários."""
    dados = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile)
            for linha in leitor:
                # Converte o valor de 'disponivel' para booleano (True/False)
                if "disponivel" in linha:
                    linha["disponivel"] = linha["disponivel"].lower() == "true"
                dados.append(linha)
    return dados

def salvar_dados(nome_arquivo, dados, campos):
    """Grava os dados da lista de dicionários em um arquivo CSV."""
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()  # Cabeçalho
        for d in dados:
            escritor.writerow(d)

# DADOS INICIAIS (carregamento dos arquivos existentes)
livros = carregar_dados("livros.csv")
usuarios = carregar_dados("/usuarios.csv")

# FUNÇÕES DE CADASTRO
def cadastrar_livro():
    limpar_tela()
    print("=== Cadastro de Livro ===")

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    codigo = input("Código do livro: ")

    for livro in livros:
        if livro["codigo"] == codigo:
            print("Livro já cadastrado!")
            input("Pressione ENTER para continuar...")
            return

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "codigo": codigo,
        "disponivel": True
    }
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")
    input("Pressione ENTER para continuar...")

def cadastrar_usuario():
    limpar_tela()
    print("=== Cadastro de Usuário ===")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")

    for u in usuarios:
        if u["matricula"] == matricula:
            print("Usuário já cadastrado!")
            input("Pressione ENTER para continuar...")
            return

    novo_usuario = {
        "nome": nome,
        "matricula": matricula
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")
    input("Pressione ENTER para continuar...")

# FUNÇÕES DE LISTAGEM
def listar_livros():
    limpar_tela()
    print("=== Lista de Livros ===")

    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(livros, start=1):
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"{i}. {livro['titulo']} ({livro['autor']}, {livro['ano']}) - {status}")

    print(f"\nTotal de livros disponíveis: {contar_disponiveis(livros)}")
    input("\nPressione ENTER para continuar...")

def listar_usuarios():
    limpar_tela()
    print("=== Lista de Usuários ===")

    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario['nome']} (Matrícula: {usuario['matricula']})")
    input("\nPressione ENTER para continuar...")

# FUNÇÕES DE EMPRÉSTIMO E DEVOLUÇÃO
def emprestar_livro():
    limpar_tela()
    print("=== Empréstimo de Livro ===")
    matricula = input("Matrícula do usuário: ")
    codigo = input("Código do livro: ")

    usuario = next((u for u in usuarios if u["matricula"] == matricula), None)
    livro = next((l for l in livros if l["codigo"] == codigo), None)

    if not usuario:
        print("Usuário não encontrado!")
    elif not livro:
        print("Livro não encontrado!")
    elif not livro["disponivel"]:
        print("Livro já está emprestado!")
    else:
        livro["disponivel"] = False
        print(f"{usuario['nome']} emprestou o livro '{livro['titulo']}' com sucesso!")

    input("\nPressione ENTER para continuar...")

def devolver_livro():
    limpar_tela()
    print("=== Devolução de Livro ===")
    codigo = input("Código do livro: ")

    livro = next((l for l in livros if l["codigo"] == codigo), None)

    if not livro:
        print("Livro não encontrado!")
    elif livro["disponivel"]:
        print("Este livro já está disponível!")
    else:
        livro["disponivel"] = True
        print(f"Livro '{livro['titulo']}' devolvido com sucesso!")

    input("\nPressione ENTER para continuar...")

# MENU PRINCIPAL (estrutura de múltipla escolha)
def menu():
    while True:
        limpar_tela()
        print("=== Sistema de Biblioteca Escolar ===")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Cadastrar Usuário")
        print("4. Listar Usuários")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1": cadastrar_livro()
            case "2": listar_livros()
            case "3": cadastrar_usuario()
            case "4": listar_usuarios()
            case "5": emprestar_livro()
            case "6": devolver_livro()
            case "7":
                # Salvar os dados antes de encerrar
                salvar_dados("livros.csv", livros, ["titulo", "autor", "ano", "codigo", "disponivel"])
                salvar_dados("usuarios.csv", usuarios, ["nome", "matricula"])
                print("Dados salvos. Finalizando o sistema...")
                break
            case _:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")

# PONTO DE ENTRADA DO PROGRAMA
menu()