quantidade_notas = int(input("Digite a quantidade de notas fiscais: "))
soma_das_notas = 0


for i in range(quantidade_notas):
    valor_nota = float(input(f"Digite o valor da {i+1}° nota fiscal: R$ "))
    soma_das_notas += valor_nota

if soma_das_notas <= 100.00:
    aliquota = 0.05
elif soma_das_notas < 5000.00:
    aliquota = 0.09
elif soma_das_notas < 15000.00:
    aliquota = 0.12
else:
    aliquota = 0.16

valor_imposto = soma_das_notas * aliquota

print(f"\nValor total das notas: R$ {soma_das_notas:.2f}")
print(f"Alíquota aplicada: {aliquota*100:.0f}%")
print(f"Valor total do imposto a ser pago: R$ {valor_imposto:.2f}")