quantidade_dias = int(input("Informe a quantidade de dias a serem analisados: "))
soma_das_temperaturas = 0

for i in range(1, quantidade_dias + 1):
    temp = float(input(f"Informe a temperatura do {i}° dia em °C: "))
    soma_das_temperaturas += temp

media = soma_das_temperaturas / quantidade_dias

if media > 28:
    print("Média de temperatura: Clima Quente.")
elif 18 <= media <= 28:
    print("Média de temperatura: Clima Agradável.")
else:
    print("Média de temperatura: Clima Frio.")

print(f"Média final da temperatura do período: {media:.2f}°C")