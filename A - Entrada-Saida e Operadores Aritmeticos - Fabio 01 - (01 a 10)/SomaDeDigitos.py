#Contexto: Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U)

import math
print('>>> Somatório de um número de três digitos <<<')
#Entrada
Numero = int(input("Digite um numero inteiro de três digitos:"))

#Processamento
Centena = math.floor(Numero / 100)
Dezena = math.floor((Numero - (Centena * 100)) / 10)
Unidade = Numero - ((Centena*100) + (Dezena*10))
Soma = Centena + Dezena + Unidade

#Saída
print(f"A soma dos algrismos do número {Numero} equivale a {Soma}.")