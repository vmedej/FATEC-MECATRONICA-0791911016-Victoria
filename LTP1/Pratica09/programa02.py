entrada = input("Informe os nomes, separando eles por ';': ")

#Estrutura for
for nome  in entrada.split(";"):
  print(nome.upper())
