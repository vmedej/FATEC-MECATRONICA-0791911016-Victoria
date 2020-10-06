#Classificador de nível gamer
#Mouse com RGB 
#Teclado com RGB 
#Monitor com RGB 
#Mouse - Teclado - Monitor - Classificação
# Sim     Sim       Sim       Viciado
# Não     Sim       Não       Nóia
# Sim     Não       Não       Quase Normal
# Não     Não       Não       Normal
# Qualquer outro caso - Não sabe responder

mouse = input("Seu mouse tem RGB? ")
teclado = input("Seu teclado tem RGB? ")
monitor = input("Seu monitor tem RGB? ")

if mouse == "sim" and teclado == "sim" and monitor == "sim":
  print("Viciado")
elif mouse == "não" and teclado == "sim" and monitor == "não":
  print("Nóia")
elif mouse == "sim" and teclado == "não" and monitor == "não":
  print("Quase normal")
elif mouse == "não" and teclado == "não" and monitor == "não":
  print("Normal")
else:
  print("Sem classificação")
