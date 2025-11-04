tabuada = int(input("Deseja saber a tabuada de qual número: "))
contador = 1

while contador <= 10:
    resultado = tabuada * contador
    print(f"{tabuada} x {contador} = {resultado}")
    contador += 1
print(f"\nTabuada do {tabuada} Completa")