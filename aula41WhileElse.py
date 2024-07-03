"""while/else (Pouco usado)"""
string = 'Valor qualquer'
i=0

while i<len(string):
    letra=string[i]
    
    print(letra)
    i += 1
    if i>6:
        break
else:
    print('Saiu')
print('Fora do while')