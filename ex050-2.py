## 050 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

# agora usando apenas uma variável e loop
soma = 0 # essa variável será usada para armazenar a soma dos números pares fornecidos pelo usuário
for i in range(6): # em cada iteração do loop (6 vezes), a variável i vai assumir um valor de 0 a 5
  n = int(input(f'Digite um número inteiro: '))
  if n % 2 == 0:
    soma += + n # se o número fornecido pelo usuário for par, adicionamos esse número à variável soma, isso é feito somando o valor atual de soma com o valor de n e armazenando o resultado de volta em soma
print(soma)
