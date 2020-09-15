#Programa para calcular o valor da parcela
valor_total = float(input("Digite o valor total: "))
numero_parcelas = int(input("Digite o valor de parcelas: "))

#Olha o número de parcelas 
if numero_parcelas == 1:
  parcela = (valor_total * 0.95)/numero_parcelas

elif numero_parcelas == 2:
  parcela = valor_total/numero_parcelas
elif numero_parcelas == 3:
  parcela = (valor_total * 1.05)/numero_parcelas
else:
  parcela = (valor_total * 1.1)/numero_parcelas

print ("Valor da parcela:",  parcela)
