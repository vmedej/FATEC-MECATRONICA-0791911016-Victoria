somatoria = 0
contador = 0

continuar = True

while continuar == True:
  numero = int(input("Informe um valor: "))
  somatoria = somatoria + numero
  contador = contador + 1
  resposta = input("Deseja continuar? ")
  if resposta == "sim":
    continuar = True
  else:
    continuar = False

media = somatoria/contador
print("A média dos valores informados é: ", media)
