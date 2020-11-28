def busca(entrada, nome_procurado):
  encontrei = False
  for nome in entrada.split(';'):
    if nome == nome_procurado:
      encontrei = True
  return encontrei

entrada = input("Informe todos os nomes, separados por ';': ")
nome = input("Informe um nome para buscar: ")

if busca(entrada, nome) == True:
  print("Nome encontrando")
else:
  print("Nome não encontrado")
