#Programa que informe quantos numeros o usuário desejar
#Cada valor informado representa uma temperatura
#A cada valor  informado, perguntar se ele deseja continuar
#Todos os valores informados devem ser armazenados em uma lista
#Quando o usuário não quiser informar mais temperaturas, pedir um valor limiar
#Contar a quantidade de valores que foram informados e estão acima do valor limiar
#Exibir a poncentagem desses valores, dado o tamanho total da lista, que é superior ao limiar
#Dado o valor percentual calculado, exibir uma mensagem

temperaturas = []
continuar = True
while continuar == True:
  temperatura = float(input("Valor da temperatura: "))
  temperaturas.append(temperatura)
  continuar = input ("Continuar? ") == "sim"

limiar = float(input("\nValor limiar: "))
acima_limiar = []

for temperatura in temperaturas:
  if temperatura > limiar:
    acima_limiar.append(temperatura)

porcentagem = len(acima_limiar) / len(temperaturas) * 100

print("\nAcima:", porcentagem, "%")

if porcentagem >= 20 and porcentagem < 45:
  print("\nDentro do esperado!")
elif porcentagem >= 45 and porcentagem < 70:
  print("\nAcima do esperado")
elif porcentagem >= 70 and porcentagem < 100:
  print("\nMuitos valores acima do limiar")
else:
  print("\nSem problemas aqui")
