caractere = input("Digite um caractere ou símbolo(ex: *, #, -): ")
repetir = "sim"

while repetir == "sim":
    print(caractere*20)

    repetir = input("Deseja ver outra linha? (Digite SIM para continuar): ").lower()

print("Gerador encerrado. Obrigado!")
