numero_total_de_pecas = int(input("Digite o número total de peças a serem inspecionadas: "))
tolerancia = 0.5
tamanho_ideal = 15.0
soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0.0

for i in range(numero_total_de_pecas):
    tamanho_medido = float(input(f"Tamanho medido da {i+1}° peça (em cm): "))
    soma_dos_tamanhos += tamanho_medido
    desvio = abs(tamanho_medido - tamanho_ideal)
    if desvio > tolerancia:
        pecas_fora_tolerancia += 1

media_tamanho = soma_dos_tamanhos / numero_total_de_pecas

if pecas_fora_tolerancia == 0:
    print("Lote Aprovado: Qualidade Perfeita (0 peças fora da tolerância).")
elif pecas_fora_tolerancia <= 2:
    print("Lote Aceitável: Pequena correção necessária.")
else:
    print("Lote Reprovado: Alta taxa de defeito.")

print(f"\nMédia de Tamanho das Peças: {media_tamanho:.2f} cm\nQuantidade de Peças Fora da Tolerância: {pecas_fora_tolerancia}")
