#Estrutura de repetição

numero_secreto = 13

acertou = False

while acertou == False:
  chute = int(input("Informe seu chute: "))
  if chute > numero_secreto:
    print("O número é menor")
  elif chute < numero_secreto:
    print("O número é maior")
  else:
    acertou = True
    print("Acertou!")

print("Obrigada por jogar!")
