# 017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

catetoOposto = int(input('Informe o comprimento do cateto oposto: '))
catetoAdjacente = int(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = ((catetoOposto ** 2) + (catetoAdjacente ** 2)) ** 0.5
print(f'O comprimento da hipotenusa é igual a {hipotenusa:.0f}.')
