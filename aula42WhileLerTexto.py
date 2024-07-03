frase = 'O Python é uma linguagem de programação'\
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum'

i = 0
qtd_apareceuMaisVezes = 0
letraApareceuMaisVezes = ''


while i< len(frase) :
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i+=1
        continue
    
    qtd_vezes_atual = frase.count(letra_atual)
    
    if qtd_apareceuMaisVezes<= qtd_vezes_atual :
        qtd_apareceuMaisVezes = qtd_vezes_atual
        letraApareceuMaisVezes = letra_atual
        
    i+=1
        
print('A letra que apareceu mais vezes foi :\
'f'"{letraApareceuMaisVezes}" que apareceu'\
f'{qtd_apareceuMaisVezes}x')