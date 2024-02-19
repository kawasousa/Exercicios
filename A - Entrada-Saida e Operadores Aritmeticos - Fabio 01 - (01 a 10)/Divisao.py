#Contexto: Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

print('>>> Divisão da soma pela diferença de dois números <<<')
#Entrada
Numero1 = int(input("Digite o primeiro número:"))
Numero2 = int(input("Digite o segundo número:"))

#Processamento
Soma = Numero1 + Numero2
Diferenca = Numero1 - Numero2
Divisao = Soma / Diferenca

#Saída
print(f"O valor da divisão da soma pela diferença é {Divisao}")