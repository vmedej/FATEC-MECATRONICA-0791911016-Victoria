#1 - Criar um log de temperaturas
#2 - Ler N temperaturas
#3 - Calcular a temperatura média
#4 - Encontrar todas as temperaturas acima da média
#5 - Encontrar a maior temperatura
#6 - Encontrar a menor temperatura

#1
temperaturas = []

#2
quantidade = int(input("Digite a quantidade de temperaturas: "))

while len(temperaturas)<quantidade:
  temperatura = float(input("Informe o valor da temperatura:  "))
  temperaturas.append(temperatura)
print("\nValores informados:")
print(temperaturas)

#3
media = sum(temperaturas)/len(temperaturas)
print("\nTemperatura  média:", media)

#Criar uma lista vazia para guardar as temperaturas acima da média
#4
temperaturas_acima = []
for temperatura in temperaturas:
  if temperatura>media:
    temperaturas_acima.append(temperatura)
print("\nTemperaturas acima da média:")
print(temperaturas_acima)

#5
maior_temperatura = max(temperaturas)
print("\nMaior temperatura:")
print(maior_temperatura)

#6
menor_temperatura = min(temperaturas)
print("\nMenor temperatura:")
print(menor_temperatura)
