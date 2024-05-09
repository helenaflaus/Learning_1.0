# 011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = int(input('Me fala a largura da parede em metros: '))
altura = int(input('Me fale a altura da parede em metros: '))
area = largura * altura
tinta = area/2
print(f'Você vai precisar de {tinta} litros de tinta.')