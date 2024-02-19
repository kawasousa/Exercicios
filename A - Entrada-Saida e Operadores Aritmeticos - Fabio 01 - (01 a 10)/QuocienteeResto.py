#Contexto: Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1º pelo 2º.

import math
print('>>> Quociente e Resto de uma divisão <<<')
#Entrada
Numero1 = int(input("Digite o primeiro número"))
Numero2 = int(input("Digite o segundo número"))

#Processamento
Quociente = math.floor(Numero1 / Numero2)
Resto = Numero1 % Numero2

#Saída
print(f"O quociente da divisão de {Numero1} por {Numero2} é {Quociente}, o resto é {Resto}")