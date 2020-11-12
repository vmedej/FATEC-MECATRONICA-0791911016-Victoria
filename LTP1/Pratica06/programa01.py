nome = input("Informe o seu nome: ")
time_de_futebol = input("Informe qual é o seu time de futebol: ")
quantidade = int(input("Informe quantos títulos mundiais o seu time tem: "))

print("Olá", nome)

if time_de_futebol == "Palmeiras":
  print("Seu time não tem títulos mundiais")
else:
  print("O seu time", time_de_futebol, "tem", quantidade, "títulos mundiais!")
