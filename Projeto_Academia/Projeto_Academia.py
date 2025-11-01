# ==========================================
# SISTEMA DE CONTROLE DE ALUNOS - ACADEMIA
# ==========================================
# Autor: André Olímpio
# ==========================================
# Funcionalidades:
# - Login de administrador
# - Cadastro e listagem de alunos
# - Cálculo de IMC e classificação
# - Controle de mensalidades com desconto
# - Menu interativo com repetição
# ==========================================

# Lista global para armazenar os alunos
alunos = []

# Função de cálculo do IMC
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    return imc, classificacao

# Função de cálculo da mensalidade
def calcular_mensalidade(meses):
    valor_mensal = 100.0 # valor considerado para cálculo
    total = valor_mensal * meses
    
    # calculando o desconto para pagamento da mensalidade
    if meses >= 6:
        total *= 0.9  # 10% de desconto
    return total

# Função de cadastro de aluno
def cadastrar_aluno():
    print("\n=== Cadastro de Alunos ===") # \n - efetua quebra de linha na impressão na tela
    nome = input("Nome do(a) aluno(a): ").strip() # strip - retira espaço em branco no início e final da cadeia de strings
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura
    }

    alunos.append(aluno) # Inserindo os dados do aluno na lista
    print(f"\n Aluno(a) '{nome}' cadastrado(a) com sucesso!\n") # f - concatenar um texto com valor atribuído na variável

# Função de listagem de alunos
def listar_alunos():
    print("\n=== Lista de Alunos ===")
    
    # verificar se a lista está vazia
    if len(alunos) == 0:
        print("Nenhum aluno(a) cadastrado(a).\n")
        return

    for i, aluno in enumerate(alunos, start=1): # adiciona um índice ao item da lista, iniciando em 1
        print(f"{i}. Nome: {aluno['nome']}, Idade: {aluno['idade']} anos, Peso: {aluno['peso']} kg, Altura: {aluno['altura']} m")
    print()

# Função para cálculo do IMC
def calcular_imc_aluno():
    print("\n=== Cálculo de IMC ===")
    
    # verificar se a lista está vazia
    if len(alunos) == 0:
        print("Nenhum aluno(a) cadastrado(a).\n")
        return

    nome = input("Digite o nome do(a) aluno(a): ").strip()
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower(): # lower - retorna cadeia de strings em minúsculo
            imc, classificacao = calcular_imc(aluno["peso"], aluno["altura"])
            print(f"\nAluno(a): {aluno['nome']}")
            print(f"IMC: {imc:.2f}") # 2f - Formatação de impressão com duas casas decimais
            print(f"Classificação: {classificacao}\n")
            encontrado = True
            break

    if not encontrado:
        print("Aluno(a) não encontrado(a).\n")

# Função para cálculo da mensalidade
def calcular_mensalidade_aluno():
    print("\n=== Cálculo de Mensalidade ===")
    nome = input("Digite o nome do(a) aluno(a): ").strip()
    meses = int(input("Quantidade de meses pagos: "))

    total = calcular_mensalidade(meses)
    print(f"\nAluno: {nome}")
    print(f"Meses pagos: {meses}")
    print(f"Valor total a pagar: R$ {total:.2f}\n")

# Função de login do sistema
def login():
    print("=== LOGIN DO ADMINISTRADOR ===")
    usuario_correto = "admin" # Usuário para validação
    senha_correta = "1234" 

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("\n Login realizado com sucesso!\n")
        return True
    else:
        print("\n Usuário ou senha incorretos. Acesso negado.\n")
        return False

# Função Menu Principal
def menu():
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1 - Cadastrar alunos")
        print("2 - Listar alunos")
        print("3 - Calcular IMC")
        print("4 - Calcular mensalidade")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            calcular_imc_aluno()
        elif opcao == "4":
            calcular_mensalidade_aluno()
        elif opcao == "0":
            print("\nFinalizando a Execução do Sistema!!!\n")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Execução principal
if __name__ == "__main__":
    if login():
        menu()
    else:
        print("Encerrando o Sistema.")
