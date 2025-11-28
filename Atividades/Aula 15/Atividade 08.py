def somar_dois_numeros(numero1, numero2):
  soma = numero1 + numero2
  return soma



num1 = float(input("Digite o primeiro número para a soma: "))
num2 = float(input("Digite o segundo número para a soma: "))

resultado_final = somar_dois_numeros(num1, num2)
print(f"A soma dos números é: {resultado_final}")
