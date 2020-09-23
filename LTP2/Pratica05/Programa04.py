#Lê uma lista e mostra separa os números pares e ímpares e informa caso não tenha números ímpares ou pares
#Cria uma lista
numeros = []

#Pergunta ao usuário quantos valores ele deseja informar
quantidade = int(input("Quantos valores terá a lista? "))

#Lê os números
while len(numeros)<quantidade:
  numero = int(input("Valor: "))
  numeros.append(numero)

print("\nValores informados:")
print(numeros)

#Cria uma lista para valores pares e outra para os ímpares
pares = []
impares = []

#Cria um for que faz a variável número passar por todos os valores que fazem parte da variável números, um de cada vez
for numero in numeros:
  if numero%2 == 0:
    pares.append(numero)
  else:
    impares.append(numero)

if len(pares)>0:
  print("Pares:", pares)
else:
  print ("Não tem números pares!")

if len(impares)>0:
  print("Ímpares:", impares)
else:
  print("Não tem números ímpares!")
