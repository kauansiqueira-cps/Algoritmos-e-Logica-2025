qtde_alunos = int(input("Informe a quantidade de alunos na sala: "))

soma_das_notas = 0

for i in range(1, qtde_alunos+1):
      nota = float(input(f"Informe a nota do {i}° Aluno: "))
      soma_das_notas += nota

media_turma = soma_das_notas / qtde_alunos
print(f"Média da Turma: {media_turma}")
