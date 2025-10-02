# RA: 0220482523045 | Nome: Kauan Guilherme Siqueira
print("RA: 0220482523045\nNome: Kauan Guilherme Siqueira\nQualquer Coisa: QualQuer Coisa.com.br.fatec\n")

pureza = float(input("Informe a puzera do lote (em decimal, ex: 0.92 para 92%): "))
massa_total = int(input("Informe a massa total do lote (em kg): "))
taxa_contaminacao = float(input("Informe a taxa de contaminação (em decimal,  ex: 0.02 para 2%): "))
FD = (pureza * 100) - (taxa_contaminacao * 50)

if massa_total > 1000:
    P_base = 10
else:
    P_base = 12.5
    
if FD > 90 and pureza > 0.98:
    print("Classificação: PREMIUM (Venda Imediata)")
    P_final_kg = P_base * 1.50

elif FD >= 70 and FD <= 0.90 and taxa_contaminacao < 0.05:
    print("Classificação: PADRÃO (Venda Normal)")
    P_final_kg = P_base * 1.10
elif FD < 70 or pureza < 0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento)")
    P_final_kg = P_base * 0.25
else:
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    P_final_kg = P_base * 0.90

Preco_Total_Final = P_final_kg * massa_total
print(f"Preço Base por kg: R${P_base:.2f}\nPreço Total Final: R${Preco_Total_Final:.2f}")