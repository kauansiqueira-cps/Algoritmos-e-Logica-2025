anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite o mes que vc nasceu: "))
dias = int(input("Digite o dia que vc nasceu: "))

total_dias = (anos * 365) + (meses * 30) + dias


print(f"A idade expressa apenas em dias é: {total_dias} dias")
