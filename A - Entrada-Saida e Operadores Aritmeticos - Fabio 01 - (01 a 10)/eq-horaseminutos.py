#Contexto: Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

import math
print('>>> Saiba a quantidade de horas e minutos <<<')
#Entrada
ValorMinutosTotais = (int(input("Digite o número de minutos: ")))

#Processamento
ValorHoras = math.floor(ValorMinutosTotais / 60)
ValorMinutosFinais = (ValorMinutosTotais % 60)
#Saída
print(f"{ValorMinutosTotais} equivalem a {ValorHoras}horas e {ValorMinutosFinais}minutos")