# 056 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mais_velho = 0
nome_mais_velho = ''
mulheres_20_mais = 0
lista_media = []

for i in range(0,4):
    idade = int(input('Me fale a idade: '))
    sexo = int(input('Me fale se é masculino(1) ou feminino(2). Digite a opção 1 ou 2: '))
    nome = input('Me fale o nome: ')
    lista_media.append(idade) # adicionando idades na lista de idades para saber a média
    if idade > mais_velho and sexo == 1: # descobrindo o homem mais velho e o nome dele
        mais_velho = idade
        nome_mais_velho = nome
    if idade > 20 and sexo == 2: # adicionando mulheres 20+ para a lista
        mulheres_20_mais += 1

print(f'O nome do homem mais velho é {nome_mais_velho} e ele tem {mais_velho} anos')
media = sum(lista_media) / len(lista_media)
print(f'A média de idade do grupo é {media}')
print(f'Quantidade de mulheres com mais de 20 anos: {mulheres_20_mais}')
