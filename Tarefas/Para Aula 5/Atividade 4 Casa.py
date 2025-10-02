valor_futuro = float(input("Informe o valor que deseja chegar ao investir: "))
taxa_juros = float(input("Informe o valor da Taxa de Juros: "))
anos = float(input("Informe a quantidade de anos: "))

valor_presente = valor_futuro / (1 + taxa_juros)**anos

if valor_presente < 30000:
    print(f"valor deve ser investido em bens não duráveis, Valor Presente: {round(valor_presente,2)}")
else:
    print(f"valor deve ser investido em renda fixa superior a 24 meses, {round(valor_presente,2)}")
# Faça um programa de investimentos que leia

# float - valor_futuro
# float - taxa_juros 
# int - anos 

# calcule
# valor_presente = valor_futuro / (1 + taxa_juros)**anos

# Mostre mensagem:
# se valor_presente < 30000
#      valor deve ser investido em bens não duráveis
# senão
#     #  valor deve ser investido em renda fixa superior a 24 meses