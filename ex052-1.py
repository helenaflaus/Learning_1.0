## 52 com loop mostrando as divisões possíveis

n = int(input('Descubra se o número é primo: '))
div = 0
for c in range(1, n + 1):
  if n % c == 0:
    div += 1
    print(f'{n} divisível por {c}')
print(f'{n} foi divisível {div} vezes')
if div > 2:
  print('Não é primo.')
else:
  print('É primo.')
