#Calculadora de 4 operações básicas
import math
from math import sin, cos, tan

operacao = input("Informe a operação desejada: ")

if operacao == "+":
  valor1 = float(input("Digite o primeiro valor: "))
  valor2 = float(input("Digite o segundo valor: "))
  resultado = valor1+valor2
  print("O  resultado é:", resultado)
elif operacao == "-":
  valor1 = float(input("Digite o primeiro valor: "))
  valor2 = float(input("Digite o segundo valor: "))
  resultado = valor1-valor2
  print("O  resultado é:", resultado)
elif operacao == "*":
  valor1 = float(input("Digite o primeiro valor: "))
  valor2 = float(input("Digite o segundo valor: "))
  resultado = valor1*valor2
  print("O  resultado é:", resultado)
elif operacao == "/":
  valor1 = float(input("Digite o primeiro valor: "))
  valor2 = float(input("Digite o segundo valor: "))
  if valor2 == 0:
    print("Valor inválido")
  else:
    resultado = valor1/valor2
    print("O  resultado é:", resultado)
elif operacao == "sen":
  angulo = float(input("Digite o valor do ângulo: "))
  print("O resultado é:", math.sin(math.radians(angulo)))
elif operacao == "cos":
  angulo = float(input("Digite o valor do ângulo: "))
  print("O resultado é:", math.cos(math.radians(angulo)))
elif operacao == "tan":
  angulo = float(input("Digite o valor do ângulo: "))
  print("O resultado é:", math.tan(math.radians(angulo)))
