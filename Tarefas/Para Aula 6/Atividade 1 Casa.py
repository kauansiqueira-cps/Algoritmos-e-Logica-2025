tempo_segundos = int(input("Digite o tempo de duração do evento (em segundos): "))


horas = tempo_segundos // 3600
resto = tempo_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"O evento teve duração de {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")



# 1h = 3600s
# 1h30m = 4200s
# 1h30m50s = 4250s





# Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.
