salario_fixo = float(input("Informe o salario fixo do vendedor: "))
comissao_produto = float(input("Informe o valor da comissão por produto: "))
quantidade_produtos = float(input("Informe a quantidade de produtos vendidos: "))

salario_total = salario_fixo + (comissao_produto * quantidade_produtos)

print(f"Salario total: {salario_total}\nQuantidade Vendida: {quantidade_produtos}")
if salario_total < 5000:
    imposto = salario_total * 0.16
    print(f"Imposto de 16%, valor do imposto: {imposto}")
else:
    imposto = salario_total * 0.27
    print(f"Imposto de 27%, valor do imposto: {imposto}")


# Faça um programa que leia do usuário
# (float) salario_fixo 
# (float) comissao_produto 
# (float) quantidade_produtos 

# Calcule
# salario_total = salario_fixo + (comissao_produto * quantidade_produtos)

# Depois mostre o valor do imposto, sendo que:
# Se salario_total < 5000
#      imposto = salario_total * 0.16
# Senão
#      imposto = salario_total * 0.27
