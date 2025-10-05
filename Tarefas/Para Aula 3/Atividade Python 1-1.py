idade = int(input("Digite sua idade: "))
experiencia = float(input("Digite seus anos de experiência em programação: "))
disponibilidade = input("Digite sua disponibilidade (manhã ou tarde): ").lower()

if idade > 18 and experiencia > 1:
    if disponibilidade == 'manhã' or disponibilidade == 'tarde' or disponibilidade == 'manha':
        print("Parabéns! Você é elegível para a vaga!")
    else:
        print("Não elegível: Disponibilidade não corresponde aos requisitos.")
else:
    print("Não elegível: Idade ou experiência insuficientes.")
