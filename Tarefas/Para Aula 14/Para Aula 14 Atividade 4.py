soma_pares = 0
soma_impares = 0
numero_digitado = 1

while numero_digitado != 0:
    numero_digitado = int(input("Digite um número inteiro (0 para encerrar): "))
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            soma_pares += numero_digitado
            print("Número par adicionado à soma.")
        else:
            soma_impares += numero_digitado
            print("Número ímpar adicionado à soma.")

print(f"A soma total dos números pares é: {soma_pares}")
print(f"A soma total dos números ímpares é: {soma_impares}")
