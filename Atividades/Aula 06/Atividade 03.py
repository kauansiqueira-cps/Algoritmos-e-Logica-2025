valor_total = float(input("Informe o valor total da compra: "))

desconto = 0

if valor_total > 100:

    desconto = 0.05
    novo_valor = valor_total - (valor_total * desconto)

    if novo_valor > 150:

        desconto = 0.02
        novo_valor = novo_valor - (novo_valor * desconto)
        print(f"Valor Total com Desconto de 5% e um desconto adicional de 2%: R${novo_valor:.2f}")
    else:
        print(f"Valor Total com Desconto de 5%: R${novo_valor:.2f}")
else:
    print("Nenhum Desconto")