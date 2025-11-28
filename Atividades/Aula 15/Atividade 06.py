def exibir_cabecalho(titulo, simbolo):
    linha_separacao = simbolo * 20
   
    print(linha_separacao)
    print(" {0} ".format(titulo.upper()))
    print(linha_separacao)


# 1ª Chamada: Título e Símbolo '#'
exibir_cabecalho("Relatório Mensal", "#")

# Adiciona uma linha em branco para separar visualmente
print("\n")

for i in range(6):
    print(f"Relatorio{i+1}")

# Adiciona uma linha em branco para separar visualmente
print("\n")

# 2ª Chamada: Título e Símbolo '*'
exibir_cabecalho("Resultado", "*")