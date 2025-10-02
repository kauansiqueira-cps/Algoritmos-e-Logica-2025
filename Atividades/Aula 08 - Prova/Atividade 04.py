# RA: 0220482523045 | Nome: Kauan Guilherme Siqueira
print("RA: 0220482523045\nNome: Kauan Guilherme Siqueira\nQualquer Coisa: QualQuer Coisa.com.br.fatec\n")

P = float(input("Informe o valor inicial do investimento: "))
T = int(input("Informe o prazo do investimento (em meses): "))

if T < 6:
    J = 0.005
elif T >= 6 and T <= 12:
    J = 0.008   
else:
    J = 0.012

Rendimento_Total = P * J * T

print(f"Taxa de Juros Aplicada: {J*100}%\nRedimento Total: R${Rendimento_Total:.2f}")