acumulador = 0

print("Soma de 5 numeros:\n ")
for i in range(1,6):
      numero = float(input(f"Digite o {i}° para a soma: "))
      acumulador += numero

print(f"Valor total dos 5 numeros: {acumulador}")