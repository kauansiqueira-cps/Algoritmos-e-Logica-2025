qtde_produtos = int(input("Informe a quantidade de produtos diferentes: "))
total_da_compra = 0

for i in range(qtde_produtos):
     preco = float(input(f"Informe o Preço do {i+1}° Produto: ")) 
     total_da_compra += preco
print(f"O total a pagar é: R${total_da_compra:.2f}")