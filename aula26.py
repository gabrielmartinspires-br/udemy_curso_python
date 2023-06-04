"""
Formatação básica de strings
s - strong
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal

(Caractere) (<>^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal  + ou -
Ex.: 0>-100,.1f

Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:0^10}')
print(f'{1000.4873648123746:,.1f}')
print(f'{-1000.4873648123746:-,.1f}')
print(f'{1000.4873648123746:+,.1f}')
print(f'{1000.4873648123746:0>+10,.1f}')
