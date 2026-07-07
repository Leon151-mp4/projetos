#imports
import math

#entrada primaria
# print('')
a = float(input("Digite o primeiro número: "))
print( )
b = float(input("Digite o segundo número: "))

print(f'os numeros são: {a, b}')
print( )

#entrada segundaria
c = input('insira um operador dentre x,+,-,/ ')
#cerebro da calculadora
if c == '+':
    print(a + b)
elif c == 'x':
    print(a * b)
elif c == '-':
    print(a - b)
elif c == '/':
    print(a / b)
