orcamento = float(input("Digite o orçamento total do projeto (em reais): "))
num_membros = int(input("Digite o número de membros na equipe: "))
area_pesquisa = input("Digite a área de pesquisa ('inovação' ou 'sustentabilidade'): ").lower()

if orcamento > 50000 and num_membros > 3:
    if area_pesquisa == 'inovação' or area_pesquisa == 'sustentabilidade'  :
        print("Projeto qualificado para o financiamento!")
    else:
        print("Projeto não qualificado: A área de pesquisa não é prioritária.")
else:
    print("Projeto não qualificado: Orçamento ou tamanho da equipe insuficientes.")
