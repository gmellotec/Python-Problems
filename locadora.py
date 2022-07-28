import os

carros = [("Chevrolet Tracker", 120),
          ("Chevrolet Onix", 90),
          ("Chevrolet Spin", 150),
          ("Hyundai HB20", 85),
          ("Hyundai Tucson", 120),
          ("Fiat Uno", 60),
          ("Fiat Mobi", 70),
          ("Fiat Pulse", 130)]
alugados = []

def mostrar_lista_carros(lista_carros):
    for i, car in enumerate(lista_carros):
        print(f"[{i}] {car[0]} - R$ {car[1]} /dia.")

mostrar_lista_carros(carros)

while True:
    os.system("cls")
    print("===============================")
    print("Bem vindos à Locadora de carros")
    print("===============================")
    print()
    print("O que você deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())

    os.system("cls")
    if op == 0:
        mostrar_lista_carros(carros)

    elif op == 1:
        mostrar_lista_carros(carros)
        print("===========")
        cod_car = int(input("Escolha o código do carro: "))
        dias = int(input("Quantos dias de aluguel? "))
        os.system("cls")

        print(f"Você escolheu {carros[cod_car][0]} por {dias} dias.")
        print(f"O valor do aluguel será de: R$ {carros[cod_car][1] * dias} ")
        print()
        print("Deseja confirmar a sua Reserva? ")
        print("      0 - SIM | 1 - NÃO         ")
        conf = int(input())

        if conf == 0:
            print(f"Reserva realizada com Sucesso! Você alugou {carros[cod_car][0]} por {dias} dias.")
            alugados.append(carros.pop(cod_car))


    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros alugados para devolver!")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_carros(alugados)
            print()
            print("Escolha o código do carro que você deseja devolver:")
            cod_alugados = int(input())
            if conf == 0:
                print(f"Obrigado por devolver o carro {alugados[cod_alugados][0]}")
                carros.append((alugados.pop(cod_alugados)))

    print()
    print("==============================")
    print("0 para CONTINUAR | 1 para SAIR")

    if float(input()) == 1:
        break