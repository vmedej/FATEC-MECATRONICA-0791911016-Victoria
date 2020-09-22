#Calculadora de 4 operações básicas

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
