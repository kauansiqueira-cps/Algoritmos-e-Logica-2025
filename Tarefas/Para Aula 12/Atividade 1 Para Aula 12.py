V_base = float(input("\nDigite o Valor Base do Bônus: "))
P_ind = int(input("Digite a Pontuação de Performance Individual (0 a 100): "))
P_equipe = int(input("Digite a Pontuação de Meta da Equipe (0 a 100): "))

if P_ind > 90:
    FAP = 1.25
elif P_ind > 70:
    FAP = 1.10
elif P_ind > 50:
    FAP = 1.00
else:
    FAP = 0.80

B_ajustado = V_base * FAP

if P_equipe > 85:
    if P_ind > 95 or B_ajustado > 5000:
        print("Bônus Máximo (30% Extra)")
        B_final = B_ajustado * 1.30
    else:
        print("Bônus Padrão (10% Extra)")
        B_final = B_ajustado * 1.10
elif P_equipe >= 60 and P_equipe <= 85:
    if P_ind < 60:
        print("Penalidade por Desempenho Individual (15% de Redução)")
        B_final = B_ajustado * 0.85
    else:
        print("Sem Alteração Adicional")
        B_final = B_ajustado
else:
    print("Penalidade Severa (25% de Redução)")
    B_final = B_ajustado * 0.75

print(f"Valor Base do Bônus: {V_base}\nFator de Ajuste Aplicado (FAP): {FAP}\nBônus Final: {B_final}")

