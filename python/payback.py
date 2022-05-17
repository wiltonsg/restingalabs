#!/usr/bin/env python3

print ('Payback - Retorno financeiro do seu sistema')

preco = float(input('Digite o valor do seu kWh: '))
valor = float(input('Digite o valor do seu sistemas: '))
geracao = float(input('Digite o quanto vai ser gerado pelo sistema: '))

total = (valor / (geracao * preco * 12 ))

print ("Retorno em: " "{:.2f}".format(total))
