#!/usr/bin/env python3

print('Entre com os valores de consumo mensais')

m1 = int(input('Mẽs 1: '))
m2 = int(input('Mẽs 2: '))
m3 = int(input('Mês 3: '))
m4 = int(input('Mês 4: '))
m5 = int(input('Mês 5: '))
m6 = int(input('Mês 6: '))
m7 = int(input('Mês 7: '))
m8 = int(input('Mês 8: '))
m9 = int(input('Mês 9: '))
m10 = int(input('Mês 10: '))
m11 = int(input('Mês 11: '))
m12 = int(input('Mês 12: '))
m13 = int(input('Mês 13: '))

# Cálculo para a média de consumo
media = (m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12 + m13) / 13

# print (media)
print ("Média: " "{:.2f}".format(media))

# Cálculo para o Potência do sistema
irr = float(input('Digite a Irradiação Inclinada Global do local: '))

pot = (irr * 30 * 0.75) / media

# print (pot)
print ("Potência: " "{:.2f}".format(pot))
