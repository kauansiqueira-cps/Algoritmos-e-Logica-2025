idade = int(input("Informe sua idade: "))

if idade >= 60:
    nacionalidade = input("Informe sua nacionalidade('brasileiro' ou outra nacionalidade): ").lower()
    if nacionalidade == 'brasileiro':
        print("Você tem direito a um desconto especial!")
    else:
        print("Você tem direito a um desconto padrão")
else:
    print("Você não tem direito a desconto")