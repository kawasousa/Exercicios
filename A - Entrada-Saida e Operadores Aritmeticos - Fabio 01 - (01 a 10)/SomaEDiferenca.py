#Contexto: Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

print('>>> Soma e Diferença entre números <<<')
#Entrada
PrimNumero = int(input("Digite o primeiro número inteiro:"))
SegNumero = int(input("Digite o segundo número inteiro:"))
TerNumero = int(input("Digite o terceiro número inteiro:"))

#Processamento
Soma = PrimNumero + SegNumero
Diferenca = SegNumero - TerNumero

#Saída
print(f"A soma dos dois primeiros números equivale a {Soma} e a diferença dos dois ultimos {Diferenca}.")