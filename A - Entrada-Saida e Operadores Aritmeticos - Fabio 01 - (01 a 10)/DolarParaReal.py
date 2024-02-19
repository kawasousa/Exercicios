#Contexto: Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

print('>>> Conversor de dolar para real <<<')
#Entrada
CotacaoDolar = int(input("Digite a atual cotação do dolar:"))
QtdDolar = int(input("Digite o número de dolares a ser convertido:"))

#Processamento
ValorReal = CotacaoDolar * QtdDolar

#Saída
print(f"{QtdDolar}, na cotação de {CotacaoDolar}, equivalem a {ValorReal} reais")