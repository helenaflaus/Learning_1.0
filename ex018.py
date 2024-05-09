# 018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan # deste modo podemos importar apenas as operações que queremos usar
angulo = float(input('Me informe o ângulo que conhece: ')) # como já importamos FROM math, aqui podemos remover 'math.xxx' do início da operação

seno = sin(radians(angulo)) # seno, cosseno e tangente estão em radianos no python, por isso precisamos converter os angulos para radianos antes de usa-los
print(f'O angulo {angulo} tem o seno de {seno:.2f}.')

cosseno = cos(radians(angulo))
print(f'O angulo {angulo} tem o cosseno de {cosseno:.2f}.')

tangente = tan(radians(angulo))
print(f'O angulo {angulo} tem a tangente de {tangente:.2f}.')