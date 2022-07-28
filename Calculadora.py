import os

print("=======================")
print("  Calculadora Python   ")
print("=======================")

print("1. + Adição")
print("2. - Subtração")
print("3. x Multiplicação")
print("4. / Divisão")
print("5. ^ Exponênciação")
print()


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


def exponenciacao(x, y):
    return x ** y


while True:

    escolha = int(input('Digite sua opção: '))

    if escolha == 1:
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} + {num2} = {adicao(num1, num2)}')
        break
    elif escolha == 2:
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print(f'{num1} - {num2} = {subtracao(num1, num2)}')
        break
    elif escolha == 3:
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')
        break
    elif escolha == 4:
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} / {num2} = {divisao(num1, num2)}')
        break
    elif escolha == 5:
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} ** {num2} = {exponenciacao(num1, num2)}')
        break
    else:
        print()
        print('Opção Invalida')
        print()

while True:

    print()
    print('DESEJA REALIZAR OUTRA OPERAÇÃO?')
    print('1 - SIM   /   0 - NÃO')
    repetir = int(input())

    if (repetir == 0):
        print('CALCULADORA FINALIZADA!!')
        break

    os.system("cls")

    print("1. + Adição")
    print("2. - Subtração")
    print("3. x Multiplicação")
    print("4. / Divisão")
    print("5. ^ Exponênciação")
    print()

    escolha = int(input('Digite sua opção: '))

    if (escolha == 1):
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} + {num2} = {adicao(num1, num2)}')
    elif (escolha == 2):
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print(f'{num1} - {num2} = {subtracao(num1, num2)}')
    elif (escolha == 3):
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')
    elif (escolha == 4):
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} / {num2} = {divisao(num1, num2)}')
    elif (escolha == 5):
        print()
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
        print()
        print(f'{num1} ** {num2} = {exponenciacao(num1, num2)}')
    else:
        print()
        print('Opção Invalida')
        print()