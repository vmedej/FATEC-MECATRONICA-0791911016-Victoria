#Para limpar a tela
from os import system

#Nossa calculadora

#Cria uma função
def mostrar_menu():
  system("clear")
  print("0 - Sair")
  print("+ - Somar")
  print("- - Subtrair")
  print("* - Multiplicar")
  print("/ - Dividir")
  print("sen - Seno")
  print("cos - Cosseno")
  print("elevado - Potência")
  print("raiz - Calcular a Raiz")

def somar():
  numero1 = float(input("Número 1: "))
  numero2 = float(input("Número 2: "))
  resultado = numero1 + numero2
  print("O resultado da soma é:", resultado)

def subtrair():
  numero1 = float(input("Número 1: "))
  numero2 = float(input("Número 2: "))
  resultado = numero1 - numero2
  print("O resultado da subtração é:", resultado)

ligado = True

while ligado == True:
  mostrar_menu()
  opcao = input("Opção: ")
  if opcao == '0':
    ligado = False
  elif opcao == '+':
    somar()
  elif opcao == '-':
    subtrair()
  
  input("Pressione enter para continuar...")

print("Até logo!")
