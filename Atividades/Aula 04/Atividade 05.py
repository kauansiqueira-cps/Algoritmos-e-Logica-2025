salario = float(input("Informe o valor do salario: "))

if salario < 5000:
    imposto=salario*0.18
else:
    imposto=salario*0.27

print(f"Valor do Imposto é de {round(imposto, 2)}")
# Se o salário < 5000
#     imposto=salario*0.18
# Senão
#     imposto=salario*0.27

# Mostre o valor do imposto