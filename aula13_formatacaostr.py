nome = 'Ricardo Pires'
altura = 1.79
peso = 73
imc = peso / altura**2
#fstrings
linha_1 = f'{nome} tem  {altura:.2f} de altura'
linha_2 = f'{peso} quilos e seu imc é:{imc:.2f}'
linha_3 = f'{imc:.2f}'



print(linha_1)
print(linha_2)
print(linha_3)
#print(nome,'tem :', altura,'de altura')
# print('Pesa : ', peso  )
# print('O imc é : ', imc)