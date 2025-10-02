#-------------------------
# EXPLIQUE O QUE FAZ ESSE PROGRAMA
# Pergunta para o usuario o peso do pacote e se o destino for local ou nacional, com essas informações o programa vai 
# calcular o custo total de envio

# EXPLIQUE OS IF/ELSE ANINHADOS
# Vai verificar se o destino está escrito corretamente e vai atribuir diferentes valores com base no destino escrito como local o custo base sendo
# 5 reais e se peso ter a condição como verdadeiro 2 reais por kg em excesso
# Se o destino for nacional, vai fazer a mesma coisa só que com valores aumentados o custo base sendo 15 reais e o kg em excesso sendo 5 reais
# Caso não for um nem o outro, vai finalizar o programa explicando para o usuario que ele digitou o destino errado

#-------------------------



peso = float(input("Digite o peso do pacote em kg: ")) # Variavel Decimal para valor de peso
destino = input("Digite o destino ('local' ou 'nacional'): ").lower()  
# .lower() serve para colocar todos os caracteres em minusculo para fazer verificação de If mais precisa sem varias variações de verificações

custo_total = 0.0 # Criação de Variavel do sistema, sem pergunta ao usuario para ser usada depois 

if destino == 'local': # Verifica se o destino for igual a 'local', se for verdadeiro
    custo_base = 5.00 # Atribui valor ao custo_base

    if peso > 10: # se o peso for maior que 10kg

        excesso_peso = peso - 10 # Peso em excesso vai ser o peso acima de 10 menos 10(Ex: 12 - 10 | Peso em Excesso = 2kg)
        custo_extra = excesso_peso * 2.00 # Para cada kg em excesso vai ter um custo extra de 2 reais
        custo_total = custo_base + custo_extra # Junta o custo base + o custo extra

    else: # se o peso for menor ou igual a 10kg

        custo_total = custo_base # o custo total vai ser apenas o custo_base
    
    print(f"O custo total do envio para o destino local é: R$ {custo_total:.2f}") # Mostra pro Usuario o custo total do envio até o destino local
    # '.2f' Do custo total serve para exibir apenas 2 casas decimais

else:  # Se o destino não for 'local', entra neste bloco

    if destino == 'nacional': # se o destino for 'nacional', se for verdadeiro
        custo_base = 15.00 # Atribui valor ao custo_base

        if peso > 10: # se o peso for maior que 10kg

            excesso_peso = peso - 10 # Peso em excesso vai ser o peso acima de 10 menos 10(Ex: 12 - 10 | Peso em Excesso = 2kg)
            custo_extra = excesso_peso * 5.00 # Para cada kg em excesso vai ter um custo extra de 5 reais
            custo_total = custo_base + custo_extra # Junta o custo base + o custo extra

        else: # se o peso for menor ou igual a 10kg

            custo_total = custo_base # o custo total vai ser apenas o custo_base
        print(f"O custo total do envio para o destino nacional é: R$ {custo_total:.2f}")# Mostra pro Usuario o custo total do envio até o destino nacional
    # '.2f' Do custo total serve para exibir apenas 2 casas decimais

    else:
        # Caso o usuario não digitar 'local' ou nem 'nacional' - O Programa vai finalizar sem nenhum calculo ou informação do custo total de envio
        print("Erro: Destino inválido. Por favor, digite 'local' ou 'nacional'.") 