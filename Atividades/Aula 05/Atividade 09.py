salario = float(input("Informe o Valor do Salario: "))
horas = int(input("Informe a quantidade de horas: "))

if salario > 5000 and horas < 40:
    adicional = 0.15
else:    
    adicional = 0.18

print(f"Salario Total com o adicional de {adicional*100}%: R${salario + (salario * adicional)}")
# Faça um programa que leia:
# salario (float)
# horas (int)

# E verifique
# Se salario > 5000 E horas < 40
#     adicional=0.15
# senão
#    adicional=0.18

# Mostrar o valor do salário acrescido do adicional