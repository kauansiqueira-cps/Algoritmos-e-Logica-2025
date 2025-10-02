import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = b**2 - 4*a*c

if delta <= 0:
    print(f"Valor de Delta = {delta}, A Equação não possui raízes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"a = {a}\nb = {b}\nc = {c}\nDelta = {delta}\nx1 = {x1}\nx2 = {x2}")