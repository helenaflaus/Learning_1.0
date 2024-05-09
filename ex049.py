# 049 Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# "Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada (tentar formatar corretamente!)."

n = int(input('Vamos descobrir a tabuada do: '))

for t in range(1,11):
    print(f'{t} x {n} = {t*n}')