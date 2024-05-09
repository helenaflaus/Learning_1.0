for c in range(0, 7):
  print(c)
#
for c in range(0, 7):
  print(c)
  print('fim')
#
for c in range(0, 7):
  print(c)
print('fim')
#
for c in range(0, 7, 1):
  print(c)
#
for c in range(7, 0, -1):
  print(c)
#
for c in range(0, 7, 2):
  print(c)
#
n = int(input('Digite um número: '))
for i in range(0, n+1):
  input()
  print(i)
print('fim')
#
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for N in range(i, f+1, p):
  print(N)
print('fim')
#
s = 0
for c in range(0, 4):
  n = int(input('digite valor: '))
  s += n # s = s + n
print(s)

# ISSO SIGNIFICA QUE ESTAMOS CRIANDO UM LOOP COM OPERAÇÕES ARITMETICAS EM FUNÇÃO DE ALGO QUE QUEREMOS DESCOBRIR
# neste caso quero inserir 4 valores inteiros e descobrir a soma deles