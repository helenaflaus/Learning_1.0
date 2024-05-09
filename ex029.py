# 029 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Velocidade: '))

if vel > 80:
  multa = (vel - 80) * 7
  print(f'Você está acima do limite de velocidade e vai pagar R$ {multa:.2f} de multa.')
