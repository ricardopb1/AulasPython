"""
Flag(Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""
""" ID



v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))
"""


condicao = True
passou_no_if = None


if condicao :
    passou_no_if = True
    print('Faça algo')
else:
    passou_no_if is None
    print('Não faça algo')

if passou_no_if is not None:
    print('Passou no if')
else:
    print(passou_no_if, passou_no_if is None)

print(passou_no_if, passou_no_if is not None)


