def soma(num1, num2):
    s = num1 + num2
    return s

def mostrarTitulo():
    m = print('--- Vamos fazer uma soma ---')
    return m

def pegarInfo():
    global num1
    global num2
    num1 = int(input('Num1: '))
    num2 = int(input('Num2: '))

mostrarTitulo()
l = pegarInfo()
s = soma(num1, num2)
print(f'O resultado da soma de {num1} e {num2} é {s}.')
