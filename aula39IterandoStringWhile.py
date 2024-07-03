"""
Iterando strings com while
"""
#       0123456789101112
nome =  'Ricardo Pires'  #Iteráveis
#       13121110987654321
indice = 0
novo_nome = ''

while indice<len(nome):
    letra = nome[indice]
    novo_nome +=f'*{letra}'
    indice +=1
    
novo_nome+='*'
print(novo_nome)