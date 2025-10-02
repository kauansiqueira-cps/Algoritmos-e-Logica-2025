num1 = int(input("Informe um numero inteiro: "))
num2 = int(input("Informe outro numero inteiro: "))

if num1 % num2 == 0 and num2 % num1 == 0:
    print("Os números são divisíveis entre si")
else:
    print("Os números não são divisíveis entre si")
# Crie um programa que solicite dois números inteiros ao usuário. 

# Em seguida, verifique se o primeiro número é divisível pelo segundo número e também se o segundo número é divisível pelo primeiro número. 

# Se ambas as condições forem verdadeiras, exiba a mensagem "Os números são divisíveis entre si". 

# Caso contrário, exiba a mensagem "Os números não são divisíveis entre si".

# DICA:
# if numero1 % numero2 == 0 and numero2 % numero1 == 0:
# ...