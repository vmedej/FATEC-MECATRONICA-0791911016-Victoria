#Calculadora personalisada
#1 - Soma 
#2 - Subtração 
#3 - Multiplicação 
#4 - Divisão

def exibirMenu():
  print("Menu Calculadora")
  print("1 - somar")
  print("2 - subtrair")
  print("3 - multiplicar")
  print("4 - dividir")
  print ("0 - sair")

def somar(numero1, numero2):
  return numero1 + numero2

def subtrair(numero1, numero2):
  return numero1 - numero2

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
  elif opcao == 0:
    continuar = False
  else:
    print("Opção inválida")
    
  input("\nPressione enter para continuar")
