#Lê uma lista e mostra separa os números pares e impares
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

#Cria uma lista para valores pares e outra para os impares
pares = []
impares = []

#Cria um for que faz a variável número passar por todos os valores que fazem parte da variável números, um de cada vez
for numero in numeros:
  if numero%2 == 0:
    pares.append(numero)
  else:
    impares.append(numero)
    
print("Pares:", pares)
print("Impares:", impares)
