NUMERO_NOTAS = 5
lista_notas = []

for i in range(NUMERO_NOTAS):
    Nota = float(input(f"Digite a {i + 1}º Nota : "))
    lista_notas.append(Nota)

for i in range(len(lista_notas)):
    print(f"A nota na posição {i} é: {lista_notas[i]}")
