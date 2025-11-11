# 1. Criação do Vetor (Lista)
# Uma Lista consegue Guardar Mais de um Valor
lista_frutas = ["Maçã", "Banana", "Uva", "Pêra", "Manga"] 

print("--- Análise da Lista ---")
# 2. Exibição Total
# Uma lista tem indices, mas se vc não indicar um, o valor a ser apresentados vai ser todos os valores que estão na lista
print("Lista completa:", lista_frutas)

# 3. Acesso ao Primeiro Elemento (Índice 0)
primeiro = lista_frutas[0] # Primeiro Valor da Lista começa em 0
print("1. Primeiro elemento (índice 0):", primeiro)

# 4. Acesso ao Terceiro Elemento (Índice 2)
terceiro = lista_frutas[2]
print("2. Terceiro elemento (índice 2):", terceiro)

# 5. Acesso a Lista ao contrario
#Inserir um indice negativo numa lista ele irá começar com os ultimos valores da lista
ultimo = lista_frutas[-1] # Ultimo Elemento
print("3. Último elemento (índice -1):", ultimo)
Penultimo = lista_frutas[-2] # Penúltimo Elemento
print("4. Penúltimo elemento (índice -2):", Penultimo)