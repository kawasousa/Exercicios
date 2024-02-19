#Contexto: Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

print('>>> Saiba a quantidade total de minutos <<<')
#Entrada
ValorHoras = (int(input("Digite o número de horas: ")))
ValorMinutos = (int(input("Digite o número de minutos: ")))

#Processamento
EqMinutos = ValorHoras * 60
MinutosTotais = ValorMinutos + EqMinutos

#Saída
print(f"O número de minutos totais é {MinutosTotais}")