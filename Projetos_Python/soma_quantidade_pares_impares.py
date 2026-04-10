soma_par = 0
soma_impar = 0
quant_impar = 0
quant_par = 0

for i in range(0,10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if (numero % 2 == 0):
        soma_par = soma_par + numero
        quant_par = quant_par + 1
    else:
        soma_impar = soma_impar + numero
        quant_impar = quant_impar + 1
print("Soma dos números pares:",soma_par)
print("Quantidade de números pares:",quant_par)
print("Soma dos números ímpares:",soma_impar)
print("Quantidade de números ímpares:",quant_impar)