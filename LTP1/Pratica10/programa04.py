valor_total = float(input("Informe o valor do produto: "))
quantidade_parcelas = int(input("Informe a quantidade de parcelas: "))

if quantidade_parcelas == 1:
  valor_final = valor_total * 0.9
elif  quantidade_parcelas  == 2:
  valor_final = valor_total
elif quantidade_parcelas == 3:
  valor_final = valor_total * 1.05
else:
  valor_final = valor_total * 1.2

print("O valor final da compra é R$ %.2f, em %i vezes." % (valor_final, quantidade_parcelas))
