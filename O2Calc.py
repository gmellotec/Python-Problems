### O2 CALC - CALCULADORA DE VAZÃO E ENRIQUECIMENTO DE OXIGÊNIO PARA OS ALTO-FORNOS

# VO2 = Vazão de Oxigênio
# EO2 = Percentual de Enriquecimento de O2
# VS = Vazão de Ar Soprado

def vazaoO2(EO2, VS):
    VO2 = (EO2 * VS * 60) / 79
    print("=============================================")
    print(f"A vazão de Oxigênio será de: {VO2:.2f} Nm³/h")

def percentualO2(VO2, VS):
  EO2 = (VO2 * 79) / (VS * 60)
  print("==============================================")
  print(f"O percentual de Oxigênio será de: {EO2:.2f} %")

def vazaoSopro(VO2, EO2):
  VS = (VO2 * 79) / (60 * EO2)
  print("=============================================")
  print(f"A vazão de Ar Soprado é de: {VS:.2f} Nm³/min")


print("===============================")
print("     BEM VINDO AO O2 CALC      ")
print("===============================")
print()
print("1 - Calcular a Vazão de Oxigênio")
print("2 - Calcular o Percentual de Oxigênio")
print("3 - Calcular a Vazão de Ar Soprado")
print("====================================")
opcao = int(input("Escolha uma das opções acima para iniciar o cálculo: "))
print()
while True:
  if opcao == 1:
    EO2 = float(input("Qual o percentual de Oxigênio? "))
    VS = float(input("Qual a vazão de sopro? "))
    vazaoO2(EO2, VS)
  elif opcao == 2:
    VO2 = float(input("Qual a vazão de Oxigênio? "))
    VS = float(input("Qual a vazão de sopro? "))
    percentualO2(VO2, VS)
  elif opcao == 3:
    VO2 = float(input("Qual a vazão de Oxigênio? "))
    EO2 = float(input("Qual o percentual de Oxigênio? "))
    vazaoSopro(VO2, EO2)
  else:
    print("OPÇÃO INVÁLIDA!!!")
  
  print()
  print("1 - SIM  /  2 - NÃO")
  continuar = int(input("Deseja Realizar outro calculo? "))

  if continuar == 1:
    print()
    print("1 - Calcular a Vazão de Oxigênio")
    print("2 - Calcular o Percentual de Oxigênio")
    print("3 - Calcular a Vazão de Ar Soprado")
    print("====================================")
    opcao = int(input("Escolha uma das opções acima para iniciar o cálculo: "))
    print()
  else:
    print()
    print("======================")
    print("FINALIZADO O O2 CALC!!")
    break