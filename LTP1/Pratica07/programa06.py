#Calculadora personalisada
#1 - Soma 
#2 - Subtração 
#3 - Multiplicação 
#4 - Divisão
#5 - R = (V, I)
#6 - V = (R, I)
#7 - I = (V, R)
#8 - Req  = série
#9 - Req = paralelo
#10 - P = (R, I)

def exibirMenu():
  print("Menu Calculadora")
  print("1 - somar")
  print("2 - subtrair")
  print("3 - multiplicar")
  print("4 - dividir")
  print("5 - resistência")
  print("6 - tensão ")
  print("7 - corrente")
  print("8 - req circuito série")
  print("9 - req circuito paralelo")
  print("10 - potência")
  print("0 - sair")

def somar(numero1, numero2):
  return numero1 + numero2

def subtrair(numero1, numero2):
  return numero1 - numero2

def multiplicar(numero1, numero2):
  return numero1 *  numero2

def dividir(numero1, numero2):
  if numero2 != 0:
    return numero1 / numero2
  else:
    print("Divisão por  0!")

def resistencia(numero1, numero2):
  return dividir(numero1, numero2)

def tensao(numero1, numero2):
  return multiplicar(numero1, numero2)

def corrente(numero1, numero2):
  return dividir(numero1, numero2)

def serie(resistencia1, resistencia2):
  return somar(resistencia1, resistencia2)

def paralelo(resistencia1, resistencia2):
  return multiplicar(resistencia1, resistencia2)/somar(resistencia1, resistencia2)

def potencia(resistencia1, corrente1):
  return resistencia1 * (corrente1**2)

#Programa principal
import os

continuar = True
while continuar == True:
  os.system("clear")
  exibirMenu()
  opcao = int(input("Digite a opção escolhida: "))
  if opcao == 1:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print("Resultado:", somar(n1,n2))
  elif opcao == 2:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print("Resultado:", subtrair(n1,n2))
  elif opcao == 3:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print("Resultado:", multiplicar(n1,n2))
  elif opcao == 4:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print("Resultado:", dividir(n1,n2))
  elif opcao == 5:
    n1 = float(input("Tensão: "))
    n2 = float(input("Corrente: "))
    print(resistencia(n1,n2), "Ohms")
  elif opcao == 6:
    n1 = float(input("Corrente: "))
    n2 = float(input("Resistência: "))
    print(tensao(n1,n2), "Volts")
  elif opcao == 7:
    n1 = float(input("Tensão: "))
    n2 = float(input("Resistência: "))
    print(corrente(n1,n2), "Amperes")
  elif opcao == 8:
    n1 = float(input("Resistência 1: "))
    n2 = float(input("Resistência 2: "))
    print("Em série", serie(n1,n2))
  elif opcao == 9:
    n1 = float(input("Resistência 1:  "))
    n2  = float(input("Resistência 2: "))
    print("Paralelo:", paralelo(n1,n2))
  elif opcao == 10:
    n1 = float(input("Resistência: "))
    n2 = float(input("Corrente: "))
    print(potencia(n1,n2), "Watts")
  elif opcao == 0:
    continuar = False
  else:
    print("Opção inválida")

  input("\nPressione enter para continuar")
