import math

x1 = float(input("Informe o valor do ponto x1: "))
x2 = float(input("Informe o valor do ponto x2: "))
y1 = float(input("Informe o valor do ponto y1: "))
y2 = float(input("Informe o valor do ponto y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distância entre os pontos é: {round(distancia,2)}")