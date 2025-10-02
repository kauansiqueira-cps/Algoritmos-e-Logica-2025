custo_fabrica = float(input("Infome o preço de fabrica: "))
porcentagem_distribuidor = float(input("Infome a porcentagem do distribuidor: "))
impostos = float(input("Infome o valor dos impostos de um carro: "))

preco = custo_fabrica + impostos + (custo_fabrica * porcentagem_distribuidor/100)

print(f"Custo do carro novo será: R${preco}")

# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos .

# Escrever um algoritmo que leia o custo de fábrica, a porcentagem do distribuidor e o valor dos impostos de um carro e 
# escreva o custo final ao consumidor.
