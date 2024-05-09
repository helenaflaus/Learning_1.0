# 036  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o seu salário? '))
prazo = int(input('Em quantos anos deseja quitar o empréstimo? '))

# vamos criar a variável do empréstimo aqui para facilitar dentro das chaves nas condições
emprestimo = valor / (prazo * 12)

if salario * 0.3 > emprestimo:
  print(f'Para pagar R$ {valor:.2f} em {prazo:.0f} anos a prestação será de R$ {emprestimo:.2f}, que corresponde a {(emprestimo / salario) * 100:.2f}% do salário.\
  Empréstimo aprovado!')
else:
  print(f'Para pagar R$ {valor:.2f} em {prazo:.0f} anos a prestação será de R$ {emprestimo:.2f}, que corresponde a {(emprestimo / salario) * 100:.2f}% do salário.\
  Empréstimo NEGADO!')
