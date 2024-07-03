# Operadores lógicos in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# R i c a r d o
#-7-6-5-4-3-2-1
# nome = 'Ricardo'
# # print(nome[-7])
# # print(nome[0])
# print('ard' in nome)
# print('z' in nome)
# print(10*'-')
# print('ard' not in nome)
# print('z' not in nome)
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')