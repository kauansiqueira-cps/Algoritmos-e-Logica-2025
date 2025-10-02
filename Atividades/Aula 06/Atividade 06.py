temperatura = int(input("Informe a temperatura em Graus Celsius: "))
chovendo = input("Informe se está chovendo (digite 'sim' ou 'não'): "  ).lower()

if temperatura > 20 and chovendo == 'não' or chovendo == 'nao':
    print("O tempo está ideal para atividades ao ar livre!")
else:
    if temperatura >= 15 and temperatura <= 20 or chovendo == 'sim':
        print("O tempo não está ideal para atividades ao ar livre.")
    else: 
        print("O tempo não é propício para atividades ao ar livre!")