def kelvin(celsius):
  return celsius + 273

def  farenheit(celsius):
  return ((9/5)*celsius) + 32

celsius = float(input("Informe a temperatura em °C: "))
print(kelvin(celsius), "K")
print(farenheit(celsius), "F")
