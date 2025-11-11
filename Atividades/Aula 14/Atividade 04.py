NUMERO_CIDADES = 5
cidades = []

for i in range(NUMERO_CIDADES):
    cidade = input(f"Digite o nome da cidade {i + 1}: ")
    cidades.append(cidade)

for i in range(len(cidades)):
    print(f"Cidade {i+1}: {cidades[i].upper()}")
