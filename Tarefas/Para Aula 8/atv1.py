condicao_tempo = input("Informe a condição do tempo ('limpo', 'nublado' ou 'tempestade'): ").lower()
visibilidade = int(input("Informe a visibilidade da pista (em metros): "))
status_motor = input("Informe o status do motor ('ok' ou 'avaria'): ").lower()

if condicao_tempo == 'limpo' and visibilidade > 1000:
    print("Condições de decolagem ideais. Autorizado.")
elif condicao_tempo == 'nublado' and visibilidade >= 500 and status_motor == 'ok':
    print("Condições de decolagem aceitáveis. Aguardando autorização final.")
elif status_motor == 'avaria':
    print("Decolagem negada. Avaria no motor detectada.")
else:
    print("Condições de segurança não atendidas. Voo atrasado.")