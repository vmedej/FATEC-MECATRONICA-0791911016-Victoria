#Programa
valor = 0
contador = 0
while contador < 7:
  valor = valor + (valor / 2) + 4
  if valor % 2 == 0:
    print (valor)
  else:
    print (valor//2)
  contador = contador + 1

#Resposta
4
10
9
16
26
41
64
