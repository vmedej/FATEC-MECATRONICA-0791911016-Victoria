#questão

dados = []

n = 5

while len(dados) < 5:
  if len(dados) != 0:
    dados.append(len(dados) + 2)
  else:
    dados.append(3)
  print(dados)
  
#resposta
[3]
[3, 3]
[3, 3, 4]
[3, 3, 4, 5]
[3, 3, 4, 5, 6]
