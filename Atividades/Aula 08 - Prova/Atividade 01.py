# RA: 0220482523045 | Nome: Kauan Guilherme Siqueira
print("RA: 0220482523045\nNome: Kauan Guilherme Siqueira\nQualquer Coisa: QualQuer Coisa.com.br.fatec\n")

preco_custo = float(input("Informe o preço de custo: "))
preco_venda = float(input("Informe o preço de venda: "))

lucro = preco_venda - preco_custo
margem = (lucro / preco_custo) * 100

if margem > 30:
    print("Margem Excelente!")
elif margem >= 10 and margem <=10:
    print("Margem Satisfatória.")
else:
    print("Margem Baixa: Avaliar preço de venda.")

