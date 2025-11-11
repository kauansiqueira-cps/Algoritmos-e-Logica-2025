# Definimos uma constante que representa o tamanho do vetor (lista).
TAMANHO_VETOR = 5

# Criamos uma lista chamada 'vetor_nomes' com 5 posições.
# Cada posição é inicializada com uma string vazia ("").
# Isso reserva espaço na memória para 5 nomes.
vetor_nomes = [""] * TAMANHO_VETOR  # vetor de palavras

print("--- Entrada de Nomes (5 Posições Fixas) ---")

# Primeiro laço FOR: usado para coletar os nomes dos alunos.
# Ele percorre os índices de 0 a 4 (total de 5 posições).
for i in range(TAMANHO_VETOR):
    # Solicita ao usuário que digite o nome do aluno.
    nome = input(f"Digite o nome do Aluno {i + 1} (Posição [{i}]): ")
    
    # Armazena o nome digitado na posição correspondente do vetor.
    vetor_nomes[i] = nome

print("\n--- Processamento dos Dados ---")
print("Os nomes registrados, acessados por índice:")

# Segundo laço FOR: usado para exibir os nomes armazenados.
# Novamente percorre os índices de 0 a 4.
for i in range(TAMANHO_VETOR):
    # Acessa o nome atual usando o índice 'i'.
    nome_atual = vetor_nomes[i]
    # Exibe o nome na tela.
    print(vetor_nomes[i])
