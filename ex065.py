"""Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou não continuar a
digitar os valores
"""
from time import sleep

resp = 'S'
soma = quanti = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('\033[33mDigite um numero\033[33;0m: '))
    soma += num
    quanti += 1
    if quanti == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [\033[032mS\033[0m/\033[032mN\033[0m] ')).upper().strip()[0]
media = soma / quanti
print('Você digitou {} números e a média foi {}'.format(quanti, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
sleep(2)
