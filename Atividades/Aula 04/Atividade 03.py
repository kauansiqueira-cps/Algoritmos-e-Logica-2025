valor_produto = float(input("Informe o Valor do Produto: "))
porcentagem_imposto = float(input("Informe a Porcentagem de Imposto: "))

valor_imposto = valor_produto * (porcentagem_imposto / 100)
valor_total = valor_produto + valor_imposto

print(f"Valor do produto R${valor_produto} com a soma dos impostos R${valor_imposto}, Totaliza-se R${valor_total}")



# Faça um programa para calcula o valor do imposto e o valor total de uma compra
# Leia as seguintes variáveis float
# valor_produto que significa o  valor do produto
# porcentagem_imposto que significa a porcentagem de imposto
# Depois, calcule
# valor_imposto = valor_produto * (porcentagem_imposto / 100)
# Em seguida, calcule o valor total
# valor_total = valor_produto + valor_imposto
# Mostre os resultado com mensagens apropriadas