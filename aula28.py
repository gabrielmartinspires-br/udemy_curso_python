nome = input('Digite seu nome: ')
nome_invertido = (nome[-1:-20:-1])
quantidade = (len(nome))
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
 
