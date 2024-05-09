n_lista = int(input('Quantos numeros desejar inserir na lista? '))
lista_par = []
lista_impar = []
for cont in range(n_lista):
  item_lista = int(input('Digite o 1o item: '))
  if item_lista % 2 == 0:
   lista_par.append(item_lista)
  else:
    lista_impar.append(item_lista)

print(f'a soma dos numeros pares é {sum(lista_par)}')
print(f'o maior item da lista é {max(lista_par)}')
print(f'o menor item da lista é {min(lista_par)}')
print(f'a quantidade numeros pares inseridos é {len(lista_par)}')
