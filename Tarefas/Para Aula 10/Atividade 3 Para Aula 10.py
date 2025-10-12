qtd_dias = int(input("Quantos dias houve viagem? "))
total_km_percorridos = 0

for dia in range(1, qtd_dias + 1):
    km = float(input(f"Informe os KM percorridos no {dia}° dia: "))
    total_km_percorridos += km

total_litros = total_km_percorridos / 12
custo_total = total_litros * 4.80

if custo_total > 500:
    print("Alerta de Gastos: O custo total com combustível foi alto (Acima de R$ 500,00).")
else:
    print("Gastos sob controle: O custo total com combustível foi baixo ou moderado.")

print(f"\nTotal de KM percorridos: {total_km_percorridos:.2f} km")
print(f"Custo total com combustível: R$ {custo_total:.2f}")