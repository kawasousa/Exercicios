#Contexto: Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6

print('>>> Conversor de km/h para m/s <<<')
#Entrada
VelocidadeInicial = int(input('Digite velocidade em quilometros por hora (km/h: '))

#Processamento
VelocidadeFinal = VelocidadeInicial / 3.6

#Saída
print(f"A velocidade {VelocidadeInicial}km/h, equivale a {VelocidadeFinal}m/s"
)