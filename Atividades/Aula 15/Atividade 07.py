def ler_notas(quantidade): 
  notas = [] # Função cria o Vetor de notas
  print(f"\n--- Leitura de {quantidade} Notas ---")
  for i in range(quantidade): # Com base na quantidade de alunos informado na função, mais notas serão inseridas
      nota = float(input(f"Digite a Nota {i + 1}: ")) # Pede o Usuarios as notas
      notas.append(nota) # Adiciona as Notas
  return notas # Retorna o Vetor de Notas

def analisar_notas(lista_notas): # Média e Maior Nota
  soma = 0.0
  maior_nota = 0.0
  for nota in lista_notas:
    soma += nota # Soma todas as Notas do Vetor
    if nota > maior_nota:
      maior_nota = nota # Pega a maior Nota do Vetor
     
  media = soma / len(lista_notas) # Faz a média de notas com base na soma de todas as notas dividido pela quantidade de notas
 
  return media, maior_nota # Retorna média e maior nota

# --- Programa Principal ---

quantidade_alunos = 4 # Quantidade de Alunos 

vetor_de_notas = ler_notas(quantidade_alunos) # Vai chamar a Função fazendo o usuario inserir as notas de cada aluno

media_final, nota_maxima = analisar_notas(vetor_de_notas) # Vai chamar a função trazendo a média e a maior nota dos alunos

print("\n--- Resultados da Análise ---") 
print(f"Lista de Notas Lida: {vetor_de_notas}")
print(f"Média Calculada: {media_final:.2f}")
print(f"Maior Nota Alcançada: {nota_maxima:.2f}")