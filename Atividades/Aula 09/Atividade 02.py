numero_tabuada = int(input("Digite um numero que você quer a tabuada: "))

print(f"\n--- Tabuada do {numero_tabuada} ---")
for i in range(1, 11):
      resultado = numero_tabuada * i
      print(f"{numero_tabuada} x {i} = {resultado}")

print("--------------------------")