#Lê uma lista e mostra todos os números pares e positivos dela
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

#Passa toda a lista pra ver quem é par
#Cria um for que faz a variável número passar por todos os valores que fazem parte da variável números, um de cada vez
for numero in numeros:
  if (numero>0) and (numero%2 == 0):
    print(numero)
