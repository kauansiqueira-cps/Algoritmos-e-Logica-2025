cateto1 = float(input("Informe a medida do primeiro cateto: "))
cateto2 = float(input("Informe a medida do segundo cateto: "))

hipotenusa = (cateto1**2 + cateto2**2)**0.5

if hipotenusa > 180:
    print(f"triangulo deve ser refeito para ser compatível com proposta")
else:
    print(f"Hipotenusa do triangulo é de : {hipotenusa}")
# Faça um programa que leia os lados de um triangulo retângulo

# (float) cateto1 
# (float) cateto2 

# Calcule
# hipotenusa = (cateto1**2 + cateto2**2)**0.5

# E mostre a mensagem:
# Se hipotenusa > 180
#      triangulo deve ser refeito para ser compatível com proposta
# senão
#     triângulo aceito deve ser incluído na proposta