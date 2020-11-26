gastos = {"pessoal": 0, "trabalho": 0, "lazer": 0, "outros": 0}

continuar = True
while continuar == True:
  categoria = input("Qual o tipo de categoria? ").lower()
  valor_do_gasto = float(input("Informe o valor: "))
  if categoria in gastos.keys():
    gastos[categoria] += valor_do_gasto
  else:
    gastos["outros"] += valor_do_gasto

  continuar = input("Deseja continuar? ").lower()  == "sim"


for categoria in gastos.keys():
  print("Categoria:", categoria, "Valor:", gastos[categoria])
