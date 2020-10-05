#Estruturas de decisão

temperatura_limite = input("Informe uma temperatura limite: ")
temperatura_atual = input("Informe a temperatura atual: ")

if temperatura_atual > temperatura_limite:
  print("A temperatura está acima do limite!")
elif temperatura_atual < temperatura_limite:
  print("A temperatura está abaixo do limite!")
else:
  print("A temperatura está no limite!")

print("Obrigada por utilizar o sistema!")
