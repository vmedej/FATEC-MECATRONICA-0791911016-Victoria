#Lista vazia com as temperaturas
#Temperaturas = [23, 5, -6, 34]
temperaturas = []

print(temperaturas)

#Pede para o usuário digitar 5 temperaturas
contador = 0
while contador < 5:
  temperatura = float(input("Informe uma temperatura: "))

  #Adiciona temperatura no final
  temperaturas.append(temperatura)

  #Só para ver o comportamento da lista entre as interações
  print(temperaturas)
  contador += 1 #contador = contador + 1