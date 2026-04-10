# -----------------------------------------------------------
# Sistema simples de análise de desempenho de um aluno
# Disciplina: Algoritmos e Programação com Python
# -----------------------------------------------------------

# 1) ENTRADA DE DADOS
# Usamos input() para solicitar as informações ao usuário.

nome = input("Digite o nome do aluno: ")

# As notas precisam ser números com casas decimais, então usamos float()
nota_prova1 = float(input("Digite a nota da Prova 1: "))
nota_prova2 = float(input("Digite a nota da Prova 2: "))
nota_atividades = float(input("Digite a nota das Atividades Práticas: "))

# Faltas e total de aulas normalmente são números inteiros
faltas = int(input("Digite a quantidade de faltas: "))
total_aulas = int(input("Digite o total de aulas ministradas: "))


# -----------------------------------------------------------
# 2) CÁLCULO DA MÉDIA
# Média aritmética das três notas
# -----------------------------------------------------------

media = (nota_prova1 + nota_prova2 + nota_atividades) / 3


# -----------------------------------------------------------
# 3) CÁLCULO DA FREQUÊNCIA
# Frequência = percentual de presença do aluno
# -----------------------------------------------------------

frequencia = ((total_aulas - faltas) / total_aulas) * 100


# -----------------------------------------------------------
# 4) VERIFICAÇÃO DA SITUAÇÃO DO ALUNO
# Aplicando as regras do exercício
# -----------------------------------------------------------

# Primeiro verificamos a frequência
if frequencia < 75:
    situacao = "Reprovado por Falta"
else:
    # Se a frequência for suficiente, analisamos a média
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado por Nota"


# -----------------------------------------------------------
# 5) CLASSIFICAÇÃO DE DESEMPENHO
# Baseada apenas na média do aluno
# -----------------------------------------------------------

if media >= 9:
    classificacao = "Excelente"
elif media >= 7:
    classificacao = "Bom"
elif media >= 5:
    classificacao = "Regular"
else:
    classificacao = "Insuficiente"


# -----------------------------------------------------------
# 6) SAÍDA DE DADOS
# Exibimos os resultados para o usuário
# -----------------------------------------------------------

print("\n----- RESULTADO FINAL -----")

print("Aluno:", nome)

# Usamos round() para mostrar apenas 2 casas decimais
print("Média:", round(media, 2))

print("Frequência:", round(frequencia, 2), "%")

print("Situação:", situacao)

print("Classificação de desempenho:", classificacao)