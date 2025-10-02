usuarioCerto = "agua@pscina.com"
senhaCerta = "molhado"

u = input("Informe o Username: ")

if u == usuarioCerto:
    p = input("Informe a Senha: ")
    if p == senhaCerta:
        print("Credencias Validas")
    else:
        print("Senha Invalida")
else:
    print("Usuario Invalido")