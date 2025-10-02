velocidade = float(input("Informe a velocidade do veiuculo: "))
distancia = float(input("Informe a distancia a ser percorrida: "))

tempo = distancia / velocidade

if tempo >4:
    print(f"Viagem demorada, duração de {tempo}horas, utilizar veículo sedan")
else:
    print(f"Viagem rápido, duração de {tempo}horas, utilizar veículo hatch")

# Crie um programa que leia do usuário a
# distancia (float)
# velocidade (float)

# Calcule o
# tempo = distancia / velocidade

# E mostre a mensagem:
# se tempo>4
#    viagem demorada, utilizar veículo sedan
# senão
#    viagem rápida, utilizar veículo hatch