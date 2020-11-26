  
#Leitura dos dados
nome = input("Informe um nome: ")
poder = input("Informe um poder: ")
historia_origem = input("Informe a história de origem: ")
universo = input("Informe qual é o universo: ")

#Possibilidade 1
heroi = {"nome": nome, "poder": poder, "historia_origem": historia_origem, "universo": universo}

print("Criado pelo método 1:", heroi)

#Possibilidade 2
heroi2 = {}
heroi2["nome"] = nome
heroi2["poder"] = poder
heroi2["historia_origem"] = historia_origem
heroi2["universo"] = universo

print("Criado pelo método 2:", heroi2)
