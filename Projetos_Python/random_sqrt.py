import random
import math

numero_aleatorio = random.randint(1, 100)
print("Número aleatório gerado:", numero_aleatorio)

numero = float(input("Digite um número positivo: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print("Raiz quadrada:", raiz)
else:
    print("Não existe raiz quadrada real para número negativo.")