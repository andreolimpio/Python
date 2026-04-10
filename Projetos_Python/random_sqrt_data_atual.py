import random
import datetime
import math

numero = random.randint(1, 100)
data = datetime.datetime.now()

print("=== SISTEMA ===")
print("Número sorteado:", numero)
print("Data:", data.strftime("%d/%m/%Y %H:%M:%S"))

raiz = math.sqrt(numero)

print("Raiz quadrada:", round(raiz, 2))