quantidade_dias = int(input("Informe a quantidade de dias a serem analisados: "))
vendas_totais = 0

for i in range(1, quantidade_dias+1):
    venda_dia = float(input(f"Informe o valor das vendas do {i}° dia: R$ "))
    vendas_totais += venda_dia

media_diaria = vendas_totais / quantidade_dias

if media_diaria > 1500.0:
    imposto_fixo = 200.0
else:
    imposto_fixo = 50.0
if vendas_totais > 10000.0:
    taxa_percentual = 0.08
else:
    taxa_percentual = 0.05

valor_taxa_servico = vendas_totais * taxa_percentual
valor_liquido_final = vendas_totais - valor_taxa_servico - imposto_fixo

print(f"\nValor Total das Vendas: R$ {vendas_totais:.2f}")
print(f"Imposto Fixo Aplicado: R$ {imposto_fixo:.2f}")
print(f"Percentual da Taxa de Serviço: {taxa_percentual * 100:.0f}%")
print(f"Valor Líquido Final: R$ {valor_liquido_final:.2f}")