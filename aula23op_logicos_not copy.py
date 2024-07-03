# Operadores lógicos
# Usado para inverter expressões
# not True = False
# not False = True
senha_digitada= input('Digite sua senha: ')
senha_repetida=input('Repita sua senha: ')

if senha_digitada != senha_repetida:
    print('Senha incorreta.')
else:
    print('Senha correta')