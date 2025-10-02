renda_mensal = float(input("Informe a Renda Mensal: "))
score_Credito = int(input("Informe a o Score Crédito (entre 0 e 1000): "))
tempo_trabalho = int(input("Informe tempo de trabalho na empresa atual em número de anos: "))

if score_Credito >=0 and score_Credito <= 1000:
    if renda_mensal > 3000 and tempo_trabalho >= 2:
        if score_Credito >= 700 and score_Credito <= 1000:
            print("Empréstimo aprovado com taxa de juros baixa!")
        else:
            print("Score de crédito insuficiente.")
    else:
        print("Não elegível: Renda ou tempo de trabalho insuficientes.")
else:
    print("O Score Crédito tem que estar entre 0 e 1000")