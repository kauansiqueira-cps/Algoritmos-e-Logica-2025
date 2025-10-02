# RA: 0220482523045 | Nome: Kauan Guilherme Siqueira
print("RA: 0220482523045\nNome: Kauan Guilherme Siqueira\nQualquer Coisa: QualQuer Coisa.com.br.fatec\n")

peso = int(input("Informe o Peso da Encomenda (em kg): "))
distancia = int(input("Informe a Distancia da Entrega (em km): "))

custo_base = (peso * 1.5) + (distancia * 0.25)

if custo_base > 200:
    print("Você recebeu um desconto de 10%")
    custo_final = custo_base - (custo_base * 0.10)
elif custo_base >=50 and custo_base <= 200:
    print("Nenhuma Taxa ou Desconto foi aplicada")
    custo_final = custo_base
else: 
    print("Taxa de R$5.00")
    custo_final = custo_base + 5

print(f"Custo base: R${custo_base:.2f}\nCusto Final: R${custo_final:.2f}")


