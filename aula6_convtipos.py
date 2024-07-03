#conversão de tipos, coerção
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro
#tipos imutáveis e primitivos:
#str, int, float, bool
print(type('1'))
#print('1'+1) (Não funciona por que o '1' é um str)
#não é possível concatenar um tipo com outro tipo diferente
#sem declarar
print(int('1'), type(int('1')))
print(int('1') + 1)
print(bool(''))
print(bool(' '))
print(str(11)+'b')