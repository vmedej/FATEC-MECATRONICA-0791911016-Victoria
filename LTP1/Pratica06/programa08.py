preco = input("Informe um valor: ")

posicao = 0
posicao_da_virgula = "Sem vírgula"
while posicao < len(preco):
  if preco[posicao] == ",":
    posicao_da_virgula = posicao
  posicao = posicao + 1

if posicao_da_virgula == "Sem vírgula":
  print("O valor informado foi de:", preco, "reais")
else:
  print("O valor informado foi de:", preco[:posicao_da_virgula], "reais")
  print("E", preco[posicao_da_virgula+1:], "centavos")
