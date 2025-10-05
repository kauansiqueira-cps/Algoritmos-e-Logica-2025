P = float(input("Informe o valor do empréstimo: "))
J_anual = float(input("Informe a taxa de juros anual (em %): "))
N = int(input("Informe o prazo do empréstimo (em meses): "))

J_mensal = (J_anual / 12) / 100

pagamento_mensal = P * (J_mensal * (1 + J_mensal)**N) / ((1 + J_mensal)**N - 1)

if pagamento_mensal < 200:
    print("Pagamento Mensal Baixo")
elif pagamento_mensal >=200 and pagamento_mensal <= 500:
    print("Pagamento Mensal Moderado")
else:
    print("Pagamento Mensal Alto")