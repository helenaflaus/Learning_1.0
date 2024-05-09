# 010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere u$$ 1.00 = R$ 3.27

reais = float(input('Quanto possui em reais? '))
dolar = reais / 3.27
print(f'Você possiu {dolar:.2f} dólares.')