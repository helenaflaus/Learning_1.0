# 053 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Me diga uma frase: ').upper
frase_sem_espaco = ''

for caractere in frase:
    if caractere != ' ':
        frase_sem_espaco += caractere

reversa = frase_sem_espaco[::-1]
if reversa == frase_sem_espaco[::-1]:
    print(f'"{frase}" é um palíndromo')
if reversa != frase_sem_espaco[::-1]:
    print((f'"{frase}": não é um palíndromo'))
