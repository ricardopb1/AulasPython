# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy(Que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input(' [E]ntrar [S]air: ')
senha_digitada = input('Senha : ')
senha_permitida = ('123456' and '1234' and '123')
senha = senha_digitada

if (entrada == 'E'or entrada =='e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

if senha_digitada == ('123' or '1234'):
    print ('OK')
else:
    print('nada')

# Avaliação de curto circuito:
# print('abc' or False or 0 or True)