def semiperimetro(a, b, c):
  return (a+b+c)/2

def area(a, b, c):
  s = semiperimetro (a, b, c)
  return (s*(s-a)*(s-b)*(s-c))**0.5
  
a = int(input("Primeiro lado: "))
b = int(input("Segundo lado: "))
c = int(input("Terceiro lado: "))

area_triangulo = area(a, b, c)
print("A área do triângulo é:", area_triangulo)
