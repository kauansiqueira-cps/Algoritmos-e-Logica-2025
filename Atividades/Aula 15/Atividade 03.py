NUM_PROVAS = 3 # Número de provas
NUM_ALUNOS = 5 # Número de alunos

matriz_notas = [] # Lista que vai armazenar as notas

print(f"--- Entrada de Notas para 3 Provas de 5 Alunos ({NUM_PROVAS}x{NUM_ALUNOS}) ---")

# Loop para cada prova
for i in range(NUM_PROVAS):
    linha_provas = []  # Lista para armazenar notas de uma prova
    print(f"\n[ PROVA {i + 1} ]")
    
    # Loop para cada aluno
    for j in range(NUM_ALUNOS):
        nota = float(input(f"  Digite a nota do Aluno {j + 1} (Posição [{i}][{j}]): ")) # Usuario Coloca Nota do aluno na posição mencionada
        linha_provas.append(nota)  # Adiciona nota na linha
    
    matriz_notas.append(linha_provas)  # Adiciona linha na matriz

# Exibe a matriz formatada
print("\n--- Matriz de Notas Registrada ---")
print("Organização: [Prova] [Aluno]")
print("Alunos: ", end="")
for i in range(5):
    print(f"Aluno {i + 1} ", end="")
print()
for i in range(NUM_PROVAS):  # For para mostrar todas as provas
    print(f"Prova {i + 1}: ", end="") # O end aqui serve pro texto ter uma continuação e não uma quebra de linha
    for j in range(NUM_ALUNOS): # Para cada prova vai mostrar a nota de todos os alunos
        print(f"{matriz_notas[i][j]:.2f}", end="\t")  # Exibe as todas com espaçamentos
    print()
