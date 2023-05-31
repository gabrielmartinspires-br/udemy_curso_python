nome = 'Gabriel'
altura = 1.763
peso = 98
imc = peso / (altura ** 2)    # IMC = peso / (altura x altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'

print(linha_1)
print('pesa', peso, 'quilos e seu imc é')
print(imc)