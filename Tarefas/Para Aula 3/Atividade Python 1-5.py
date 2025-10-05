nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
presenca = float(input("Digite a porcentagem de presença do aluno (%): "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nMédia: {media:.2f}")
print(f"Presença: {presenca:.1f}%\n")

if presenca >= 75:
    if media >= 7: # Se a media for maior igual que 7 (7-10) 
        print("Aluno Aprovado") # se o If for verdadeiro, executar essa parte do codigo
    
    elif media >= 5: # Se a media for maior igual que 5 (5-6)
        print("Aluno em Recuperação") # se of If anterior for falso, e esse if for verdeiro, vai executar essa parte
    else:
        print("Aluno Reprovado por nota") # Caso nenhum dos if anteriores forem verdadeiros, vai vir pro else
else:
    print("Aluno Reprovado por falta")

# if (Se): Verifica uma condição, se for verdadeira vai executar uma parte do codigo
# elif (else if - Senão Se): Verifica outra condição se o if anterior for falso, e se for verdadeiro vai executar outra parte do codigo
# else (Senão): Executa uma parte do código se todas as condições anteriores forem falsas