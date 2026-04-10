# ============================================
# OPERAÇÕES COM MATRIZES EM PYTHON
# ============================================

# -------- MATRIZES INICIAIS --------
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# -------- FUNÇÃO PARA EXIBIR MATRIZ --------
def exibir_matriz(nome, matriz):
    print(f"\n{nome}:")
    for linha in matriz:
        print(linha)

# -------- SOMA DE MATRIZES --------
def soma_matrizes(A, B):
    linhas = len(A)
    colunas = len(A[0])

    resultado = [
        [A[i][j] + B[i][j] for j in range(colunas)]
        for i in range(linhas)
    ]
    return resultado

# -------- MULTIPLICAÇÃO POR ESCALAR --------
def multiplicar_escalar(matriz, escalar):
    return [
        [elemento * escalar for elemento in linha]
        for linha in matriz
    ]

# -------- MULTIPLICAÇÃO DE MATRIZES --------
def multiplicar_matrizes(A, B):
    linhas_A = len(A)
    colunas_A = len(A[0])
    colunas_B = len(B[0])

    resultado = [
        [
            sum(A[i][k] * B[k][j] for k in range(colunas_A))
            for j in range(colunas_B)
        ]
        for i in range(linhas_A)
    ]
    return resultado

# -------- TRANSPOSTA --------
def transposta(matriz):
    return [list(linha) for linha in zip(*matriz)]

# -------- CÁLCULO DE MÉDIA DOS ELEMENTOS --------
def media_matriz(matriz):
    total = sum(sum(linha) for linha in matriz)
    quantidade = sum(len(linha) for linha in matriz)
    return total / quantidade

# -------- EXECUÇÃO --------
exibir_matriz("Matriz A", A)
exibir_matriz("Matriz B", B)

# Soma
soma = soma_matrizes(A, B)
exibir_matriz("Soma A + B", soma)

# Multiplicação por escalar
escalar = 3
mult_escalar = multiplicar_escalar(A, escalar)
exibir_matriz(f"A * {escalar}", mult_escalar)

# Multiplicação de matrizes
mult_matrizes = multiplicar_matrizes(A, B)
exibir_matriz("A x B", mult_matrizes)

# Transposta
transp = transposta(A)
exibir_matriz("Transposta de A", transp)

# Média
media = media_matriz(A)
print(f"\nMédia dos elementos de A: {media:.2f}")

# ============================================
# VERSÃO COM NUMPY (OPCIONAL)
# ============================================

import numpy as np

A_np = np.array(A)
B_np = np.array(B)

print("\n--- Usando NumPy ---")

print("\nSoma:")
print(A_np + B_np)

print("\nMultiplicação por escalar:")
print(A_np * 3)

print("\nMultiplicação de matrizes:")
print(A_np @ B_np)

print("\nTransposta:")
print(A_np.T)

print("\nMédia:")
print(A_np.mean())