# RESPONDA: Porque a variável senha_digitada começa com vazio ""

# Para o While funcionar a variavel tem que ser inicializada e começando ela com vazio ajuda o programa não finalizar automaticamente caso vc mude a senha
# e acabe 'acertando' na inicialização
SENHA_CORRETA = "python123"
tentativas_erradas = 0
senha_digitada = "" 

print("\n--- Sistema de Login ---")

while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == SENHA_CORRETA:
        print(f"\nSenha válida! Acesso concedido.")       
    else:
        tentativas_erradas += 1
        print("Senha incorreta. Tente novamente.")
print ("Total de entradas erradas", tentativas_erradas)