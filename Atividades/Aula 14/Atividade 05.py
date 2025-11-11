# Definimos uma constante que representa o número de elementos do vetor.
TAMANHO_VETOR = 5
#Lista com 5 elementos, todos inicializados com 0.0.
vetor_notas = [0.0] * TAMANHO_VETOR
# Inicializamos a variável 'soma_notas' com 0.0 para acumular as notas digitadas.
soma_notas = 0.0
# Inicializamos a variável 'media' com 0.0, que será usada para armazenar o resultado final.
media = 0.0
print("--- Entrada de 5 Notas ---")
# Início do primeiro laço FOR, responsável por coletar as notas do usuário.
# O laço vai de 0 até 4 (total de 5 Notas)
for i in range(TAMANHO_VETOR):
    # Usuário vai digitar uma nota.
    nota = float(input(f"Digite a Nota {i + 1} (Posição [{i}]): "))
    
    # Armazenamos a nota digitada na posição correspondente do vetor.
    # Isso substitui o valor 0.0 previamente alocado.
    vetor_notas[i] = nota
print("\n--- Processamento dos Dados ---")
# Segundo laço FOR: percorremos o vetor para somar todas as notas.
# Usamos o mesmo índice 'i' para acessar cada elemento da lista.
for i in range(TAMANHO_VETOR):
    # Somamos o valor da nota atual ao acumulador 'soma_notas'.
    soma_notas = soma_notas + vetor_notas[i]
# Após somar todas as notas, verificamos se o tamanho do vetor é maior que zero.
# Essa verificação evita divisão por zero em casos genéricos.
if TAMANHO_VETOR > 0:
    # Calculamos a média dividindo a soma total pelo número de elementos.
    media = soma_notas / TAMANHO_VETOR
# Exibimos os resultados finais:
print(f"Vetor de Notas Registrado: {vetor_notas}")
print(f"Soma Total das Notas: {soma_notas:.2f}")
print(f"Média Final da Turma: {media:.2f}")