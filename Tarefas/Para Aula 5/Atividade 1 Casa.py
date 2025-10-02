frente = float(input("Informe a medida da frente do terreno: "))
fundo = float(input("Informe a medida da fundo do terreno: "))

perimetro = 2 * (frente + fundo)

if perimetro > 16:
    print(f"Ta aprovado na alteração no cadastro, perimetro de {perimetro}")
else:
    print(f"Ta reprovado na alteração no cadastro, perimetro de {perimetro}")

# Faça um programa que leia do usuário os valores de um terreno
# (float) frente 
# (float) fundo 

# Calcule
# perimetro = 2 * (frente + fundo)

# Mostrar mensagem:
# se perimetro > 16
#      aprovar alteração do cadastro
# senão
#      reprovar alteração do cadastro