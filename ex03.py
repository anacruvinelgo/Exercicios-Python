#Escrevendo um programa que leia dois números inteiros e comparando-os, mostrando na tela as mensagens:O primeiro valor é maior, o segundo valor é maior e os valores são iguais.
n1 = int(input('Por favor digite um número: '))
n2 = int(input('Por favor digite outro número: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 == n2:
    print('Os valores são iguais')
else:
    print('O segundo valor é maior')
