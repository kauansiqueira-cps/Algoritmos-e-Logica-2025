import random

numero_secreto = random.randint(1, 6) 
tentativas = 0
acertou = False
palpite_usuario = 0 

print("--- Jogo de Adivinhar o Dado ---")
print("Tente adivinhar o número que o dado sorteou (entre 1 e 6).")

while not acertou:
    palpite_usuario = int(input("Seu palpite: "))

    # Fora do Intervalo
    if palpite_usuario < 1 or palpite_usuario > 6:
        print("Palpite fora do intervalo. Tente um número entre 1 e 6.")
        continue

    tentativas += 1

    # Dentro do intervalo + numero certo
    if palpite_usuario == numero_secreto:
        acertou = True
        print("\n*** Parabéns! Você acertou! ***")
    else:
        print("Errado. Tente novamente.")

print(f"O número sorteado era: {numero_secreto}")
print(f"Você precisou de {tentativas} tentativa(s) para acertar.")