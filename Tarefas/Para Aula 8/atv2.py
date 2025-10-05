import math

lado_a = float(input("Informe o tamanho do lado A do Triangulo: "))
lado_b = float(input("Informe o tamanho do lado B do Triangulo: "))
lado_c = float(input("Informe o tamanho do lado C do Triangulo: "))

cosseno_gama = (lado_a**2 + lado_b**2 - lado_c**2) / (2 * lado_a * lado_b)
cosseno_gama = math.degrees(math.acos(cosseno_gama))

if lado_a + lado_b > lado_c:
    if cosseno_gama == 90:
        print("O triangulo é retângulo")
    elif cosseno_gama < 90:
        print("O triangulo é acutângulo")
    else:
        print("O triangulo é obtusângulo")
else:
    print("Os lados informados não formam um triangulo")
