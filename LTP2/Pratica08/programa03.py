quantidade_de_personagens = int(input("Informe a quantidade de personagens: "))
personagens = {"Dps": [], "Healer": [], "Support": [], "Tank": []}

contador = 0
while contador < quantidade_de_personagens:
  nome = input("\nInforme o nome do personagem: ")
  categoria = input("\nInforme a classe do personagem: ")
  if categoria in personagens.keys():
    personagens[categoria].append(nome)
    contador += 1
  else:
    print("\nClasse inválida")
  print(personagens)

print("\nPorcentagens relativas:")
for categoria in personagens.keys():
  porcentagem = len(personagens[categoria])/quantidade_de_personagens
  print("Categoria:", categoria, "-", porcentagem*100)

print("\nPersonagens:\n")
for categoria in personagens.keys():
  print("Classe de personagem:", categoria.capitalize())
  for nome_de_personagem in personagens[categoria]:
    print(nome_de_personagem)
  print("------------")
