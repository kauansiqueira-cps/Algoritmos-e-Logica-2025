NUM_LINHAS = 3 # Número Maximo de Linhas da Matriz
NUM_COLUNAS = 3 # Número Maximo de Colunas da Matriz

matriz = [] #Inicialização da Matriz

for i in range(NUM_LINHAS): # Para cada Linha vai ser adicionado o maximo de colunas (Matriz Quadrada 3x3)
    matriz.append([0] * NUM_COLUNAS)

for i in range(NUM_LINHAS): # Loop para as linhas (i)
    for j in range(NUM_COLUNAS): # Loop para as colunas (j)
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: ")) # Usuario Coloca algum valor na posição mencionada
        matriz[i][j] = valor # Adiciona o Valor para a Matriz em sua respectiva posição


for i in range(NUM_LINHAS): # Para Cada linha vai mostra o número os números de suas colunas
    for j in range(NUM_COLUNAS):
        # o parâmetro end na função print() especifica o que deve ser impresso no final da saída, 
        # em vez da quebra de linha padrão (\n)
        # Se você usar end="\t", um espaço de tabulação será adicionado, em vez de quebrar a linha
        print(matriz[i][j], end="\t")
    print() # Pula linha após cada linha da matriz