def validar_entrada(valor, tipo=float):
    while True:
        try:
            return tipo(input(valor))
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor válido.")
