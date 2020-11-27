def lerNumerosPositivos():
  continuar = True
  while continuar == True:
    numero = int(input("Informe um valor: "))
    continuar = numero < 0
  return numero

primeiro_valor = lerNumerosPositivos()
segundo_valor = lerNumerosPositivos()
resposta = primeiro_valor + segundo_valor
print("A soma de", primeiro_valor, "com", segundo_valor, "é igual a:", resposta)
