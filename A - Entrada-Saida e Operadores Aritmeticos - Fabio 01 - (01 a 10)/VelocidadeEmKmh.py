#Contexto: Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

print('>>> Conversor de m/s para km/h <<<')
#Entrada
VelocidadeInicial = int(input('Digite velocidade em metro por segundo (m/s): '))

#Processamento
VelocidadeFinal = VelocidadeInicial * 3.6

#Saída
print(f"A velocidade {VelocidadeInicial}m/s, equivale a {VelocidadeFinal}km/h"
)