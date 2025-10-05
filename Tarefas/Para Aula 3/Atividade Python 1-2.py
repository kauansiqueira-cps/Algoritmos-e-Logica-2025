idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (em kg): "))
condicao_saude = input("Digite sua condição de saúde ('boa' ou 'ruim'): ").lower()

if idade >= 18 and peso >= 50:
    if condicao_saude == 'boa':
        print("Você está elegível para doar sangue!")
    else:
        print("Você não pode doar sangue devido à sua condição de saúde.")
else:
    print("Você não está elegível para doar sangue. Verifique os requisitos de idade e peso.")
