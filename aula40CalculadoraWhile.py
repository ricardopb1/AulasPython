""" Calculadora com while"""

# num1 = input('Digite o primeiro número : ')
# num2 = input('Digite o segundo número: ')
# operador = input('Agora insira o operador para calcularmos: ')

while True:
    num1 = input('Digite um número : ')
    operador = input('Digite o operador(+-/*) : ')
    num2 = input('Digite outro número : ')
    numeros_validos = None
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
        
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    if operador == '+':
        print(float(num1)+float(num2))
        continue
    elif operador == '-':
        print(float(num1)-float(num2))
        continue
    elif operador == '/':
        print(float(num1)/float(num2))
        continue
    elif operador == '*':
        print(float(num1)*float(num2))
        continue
    
    sair = input('Quer sair? [s]im ').lower().startswith('s')
    
    if sair is True:
        break