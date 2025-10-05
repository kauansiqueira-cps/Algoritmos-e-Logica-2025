# O for é um laço de repetição
# É uma ferramenta usada para iterar sobre sequências como listas, tuplas, strings, dicionários ou intervalos
# Ele permite executar um bloco de código para cada item da sequência
# A sintaxe básica do for em Python é:
# for item in sequencia:

# Exemplo 1: Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"] #- [] listas são usadas para armazenar múltiplos itens em uma única variável
for fruta in frutas:
    print(fruta)

# Exemplo 2: Iterando sobre uma string
for letra in "Abc":
    print(letra)

# Exemplo 3: Usando range() para gerar uma sequência de números
for numero in range(5): #- range() em Python é usada para gerar uma sequência de números inteiros
    print(numero)