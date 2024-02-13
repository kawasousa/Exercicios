// Contexto: Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
import {question} from 'readline-sync'

console.log(`
____________________________________
 >>> Conversor de m/s para km/h <<< 
____________________________________
`)

//Entrada
const VelocidadeInicial = Number(question('Digite a velocidade em metro por segundo (m/s): '))

//Processamento
const VelocidadeFinal = VelocidadeInicial * 3.6

//Saída
console.log(`
____________________________________
A velocidade ${VelocidadeInicial}m/s, em km/h equivale a ${VelocidadeFinal}km/h
____________________________________
`)