import random

print("--- Roleta Russa ---")
print("Dois jogadores se enfrentam. Cada jogador começa com 3 vidas.")
print("O tambor tem 6 balas aleatórias (vazias ou verdadeiras).")
print("Cada jogador escolhe se atira em si mesmo ou no outro jogador.")
print("Itens: cura, visão, dano. Máximo de 3 itens por jogador.\n")

vidas = {1: 3, 2: 3}
itens = {1: [], 2: []}
jogador = 1
posicao = 0
dano_dobrado = {1: False, 2: False}

def carregar_tambor():
    balas = [random.choice([True, False]) for _ in range(6)]
    random.shuffle(balas)
    verdadeiras = balas.count(True)
    falsas = balas.count(False)
    print(f"🔄 Tambor carregado: {verdadeiras} balas verdadeiras, {falsas} balas falsas.\n")
    return balas

def distribuir_itens():
    for j in [1, 2]:
        if len(itens[j]) < 3:
            novos = random.choices(['cura', 'visao', 'dano'], k=3 - len(itens[j]))
            itens[j].extend(novos)
            print(f"🎁 Jogador {j} recebeu itens: {novos}")
        else:
            print(f"🎒 Jogador {j} já tem 3 itens. Nenhum novo item recebido.")

tambor = carregar_tambor()
distribuir_itens()

while True:
    print(f"\nVidas - Jogador 1: {vidas[1]} | Jogador 2: {vidas[2]}")
    print(f"Itens - Jogador 1: {itens[1]} | Jogador 2: {itens[2]}")

    if vidas[1] == 0 or vidas[2] == 0:
        vencedor = 2 if vidas[1] == 0 else 1
        print(f"\n🏆 Jogador {vencedor} venceu! Fim de jogo.")
        break

    if posicao >= len(tambor):
        print("\n🔄 Tambor vazio. Recarregando...")
        tambor = carregar_tambor()
        distribuir_itens()
        posicao = 0

    acao = input(f"\nJogador {jogador}, deseja usar itens? Digite os nomes separados por espaço ou pressione Enter para pular: ").lower().split()

    for item in acao:
        if item in itens[jogador]:
            if item == 'cura':
                if vidas[jogador] < 3:
                    vidas[jogador] += 1
                    print("❤️ Cura usada. +1 vida.")
                else:
                    print("⚠️ Já está com vida cheia.")
            elif item == 'visao':
                print(f"👁️ Próxima bala é {'VERDADEIRA' if tambor[posicao] else 'FALSA'}.")
            elif item == 'dano':
                dano_dobrado[jogador] = True
                print("💥 Dano dobrado ativado para este turno.")
            itens[jogador].remove(item)
        elif item != "":
            print(f"❌ Item '{item}' inválido ou não disponível.")

    alvo = input(f"Jogador {jogador}, digite '1' para atirar em si mesmo ou '2' para atirar no outro jogador: ")

    if alvo not in ['1', '2']:
        print("Escolha inválida. Digite apenas '1' ou '2'.")
        continue

    alvo = jogador if alvo == '1' else (2 if jogador == 1 else 1)
    input(f"Jogador {jogador} puxou o gatilho contra Jogador {alvo}... pressione Enter.")

    dano = 2 if dano_dobrado[jogador] else 1
    if tambor[posicao]:
        vidas[alvo] -= dano
        print(f"\n💥 Jogador {alvo} foi atingido! Perdeu {dano} vida(s).")
    else:
        print("🔫 Clique vazio. Ninguém foi atingido.")

    dano_dobrado[jogador] = False
    posicao += 1
    jogador = 2 if jogador == 1 else 1
