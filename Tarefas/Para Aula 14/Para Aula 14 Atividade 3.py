contador_pares = 0
contador_impares = 0
numero_digitado = 1

while numero_digitado != 0:
    numero_digitado = int(input("Digite um número inteiro (0 para encerrar): "))
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            contador_pares += 1
            print("Número par contabilizado.")
        else:
            contador_impares += 1
            print("Número ímpar contabilizado.")

print(f"O total de números pares digitados é: {contador_pares}")
print(f"O total de números ímpares digitados é: {contador_impares}")
