"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x e X - Hexadecimal
(Caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.:0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.123125414414123:,.2f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')