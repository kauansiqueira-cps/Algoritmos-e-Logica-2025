# Pede pro Usuario informar a quantidade de itens que vai comprar
quantidade = int(input("Qual a quantidade? "))

# Pede pro Usuario informar o preço do item que que ele está comprando
preco = float(input("Qual o Preço? "))

# Se a quantidade de itens for maior que 10, então o usuario vai ter um desconto de 15%
if quantidade > 10:
    desconto = 0.15
else:
    # Caso Seja Menor que 10, o desconto vai ser  só de 8%
    desconto = 0.08


# Calculo do Preço * Quantidade de Item
total = quantidade * preco

# Calculo do valor a se pagar com o desconto
pagar = total - (total * desconto)

# Mostra pro usuario as informações
print(f"Por comprar {quantidade} itens, vc ganhou um desconto de {desconto*100}% o preço total a se pagar é de R${pagar}")
