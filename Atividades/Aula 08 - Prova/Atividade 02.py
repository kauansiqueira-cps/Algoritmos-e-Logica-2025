# RA: 0220482523045 | Nome: Kauan Guilherme Siqueira
print("RA: 0220482523045\nNome: Kauan Guilherme Siqueira\nQualquer Coisa: QualQuer Coisa.com.br.fatec\n")


valor_glicose = float(input("Informe o Valor da Glicose em Jejum: "))

if valor_glicose < 100:
    print("Glicemia Normal.")
elif valor_glicose >= 100 and valor_glicose <= 125:
    print("Pré-diabetes: Risco Moderado.")
else:
    print("Diabetes: Nível Alto.")