gastos = {}

continuar = True
while continuar == True:
  valor_do_gasto = float(input("Informe o valor: "))
  categoria = input("Informe a categoria: ").lower()
  #Verificando se a categoria já existe no dicionário
  if categoria in gastos.keys():
    gastos[categoria] += valor_do_gasto
  else:
  #Uma nova categoria será criada
   gastos[categoria] = valor_do_gasto
  print(gastos)
  continuar = input("Deseja continuar? ").lower()  == "sim"

#Passa por todas as categorias e exibe todos os gastos
for categoria in gastos.keys():
  print("Categoria:", categoria, "Valor:", gastos[categoria])
