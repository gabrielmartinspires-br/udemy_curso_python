nome = 'Gabriel'
altura = 1.76
peso = 98
imc = peso / (altura ** 2)    # IMC = peso / (altura x altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'


print(linha_1)
print(linha_2)
print(imc)