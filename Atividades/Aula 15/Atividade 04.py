NUM_ITENS = 3 # Número de Maximo de Itens

cardapio = [] # Inicio da Matriz

print("--- Entrada de Dados para Cardápio (3 Itens) ---")

for i in range(NUM_ITENS):
    print(f"\n[ Item {i + 1} ]")
  
    nome = input("  Digite o nome do item: ") # Pedir pro usuario o item
    preco = float(input("  Digite o preço do item: R$ ")) # E seu Preço
   
    item_completo = [nome, preco] # Coloca os Input em uma Matriz
   
    cardapio.append(item_completo) # Adiciona o Valor do item completo como matriz na Matriz[[Matriz 1[0,0]], [Matriz 2[1,1]]


print("\n--- Acessando Elementos Específicos ---")

preco_item2 = cardapio[1][1] # Preço do item da Matriz 1 (Pula a Matriz 0, entra na matriz 1 e vai no segundo campo que é o de dinheiro)
print(f"O preço do Item 2 (posição [1][1]) é: R$ {preco_item2:.2f}")

nome_item3 = cardapio[2][0]
print(f"O nome do Item 3 (posição [2][0]) é: {nome_item3}")

print("\n--- Exibição do Cardápio Completo ---")
for item in cardapio: # Para Cada Matriz do cardapio
    print(f"Nome: {item[0]} | Preço: R$ {item[1]:.2f}") # Vai mostra seu nome e seu preço