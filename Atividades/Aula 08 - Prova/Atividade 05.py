# RA: 0220482523045 | Nome: Kauan Guilherme Siqueira
print("RA: 0220482523045\nNome: Kauan Guilherme Siqueira\nQualquer Coisa: QualQuer Coisa.com.br.fatec\n")

R_investimento = float(input("Informe o valor da taxa do Retorno do Investimento(em decimal, ex: 1.20 para 120%): "))
R_livre = float(input("Informe o valor da taxa de risco (em decimal, ex: 0.20 para 20%): "))
Sigma = float(input("Informe o valor da desvio-padrão da volatilidade: "))

if Sigma == 0:
    Sharp = (R_investimento - R_livre)
else:
    Sharp = (R_investimento - R_livre) / Sigma

Spread = R_investimento - R_livre

if Sharp > 1.5 and Spread > 0.05:
    print("\nInvestimento Excelente: Alta performance ajustada ao risco.")
elif Sharp >= 0.5 and Sharp <= 1.5 or Spread > 0.02:
    print("\nInvestimento Bom: Risco e retorno moderados.")
elif Sharp < 0.5 and R_investimento > 0:
    print("\nInvestimento Aceitável: Retorno positivo, mas risco alto para o ganho.")
else:
    print("\nInvestimento Ruim: Não recomendado.")

print(f"Valor Sharp Ratio: {Sharp:.2f}")