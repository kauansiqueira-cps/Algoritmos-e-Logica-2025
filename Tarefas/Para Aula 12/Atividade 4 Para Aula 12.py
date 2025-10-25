numero_lancamentos = int(input("Digite o número total de lançamentos: "))
saldo_final = 0.0
total_receitas = 0.0
total_despesas = 0.0

for i in range(numero_lancamentos):
    valor = float(input(f"Valor da {i+1}° transação (positivo para receita, negativo para despesa): "))
    if valor > 0:
        total_receitas += valor
    else:
        total_despesas += abs(valor)
    saldo_final += valor

if saldo_final > 0 and total_receitas > total_despesas * 2:
    print("Situação Excelente: Bônus de 5% sobre o saldo aplicado.")
    saldo_ajustado = saldo_final * 1.05
elif saldo_final > 0:
    print("Situação Boa: Sem bônus ou taxa.")
    saldo_ajustado = saldo_final
else:
    print("Situação Ruim: Taxa de serviço de 2% aplicada.")
    saldo_ajustado = saldo_final * 0.98

print(f"\nTotal de Receitas: R$ {total_receitas:.2f}\nTotal de Despesas: R$ {total_despesas:.2f}\nSaldo Final Ajustado: R$ {saldo_ajustado:.2f}")