# 048 Faça um programa que calcule a SOMA de todos os números ímpares que são múltiplos de 3 e que se
# encontram no intervalo de 1 até 500.

soma = 0
for c in range(1, 501, 2): # percorrendo apenas números ímpares
  if c % 3 == 0: # verifica se o numero do contador é multiplo de 3
    soma += c # soma = soma + s (S É O CONTADOR QUE VC DEFINIU PARA O LOOP)
print(soma)
