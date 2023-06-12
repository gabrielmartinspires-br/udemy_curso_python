nome = input('Digite seu nome: ')
nome_invertido = (nome[-1:-20:-1])
quantidade = (len(nome))
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print('Seu nome contém espaços')

    else:
        print('Seu nome NÃO contém espaços')
    print(f'Seu nome tem {quantidade} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
