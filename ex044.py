# 044  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
'''- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

valor1 = float(input('Quanto custa? '))
dinheiro = valor1 * 0.9
cartao = valor1 * 0.95
cartao_2 = valor1
cartao_3_n = valor1 * 1.2

print('''Opções de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')
pagamento = int(input('Digite o número referente a opção de pagamento desejada: '))

if pagamento != 1 and pagamento != 2 and pagamento != 3 and pagamento != 4:
  print('Opção inválida.')
elif pagamento == 1:
  print(f'O produto vai custar R$ {dinheiro:.3f} à vista no dinheiro/cheque.')
elif pagamento == 2:
  print(f'O produto vai custar R$ {cartao:.3f} à vista no cartão.')
elif pagamento == 3:
  print(f'O produto vai custar R$ {cartao_2:.3f} parcelado em 2x no cartão.')
else:
  print(f'O produto vai custar R$ {cartao_3_n:.3f} parcelado no cartão.')
