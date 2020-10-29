v_on = float(input("V_on: "))
t = float(input("T: "))

continuar = True

while continuar == True:
  t_on = float(input("T_on "))
  vout = v_on * (t_on/t)
  print("Valor de saída: ", vout)
  continuar = input("Continuar? ") == "sim"
