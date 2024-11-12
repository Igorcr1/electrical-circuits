def coletar_dados_usuario():
    num_nos = int(input("Digite a quantidade de nós no circuito: "))
    nos = [chr(65 + i) for i in range(num_nos)]  # Gera ['A', 'B', 'C', ...]
    elementos = {}
    print("\nInforme as conexões entre os nós:")
    for i in range(num_nos):
        for j in range(i + 1, num_nos):
            no1 = nos[i]
            no2 = nos[j]
            res = input(f"Existe uma resistência entre {no1} e {no2}? (s/n): ")
            if res.lower() == 's':
                valor_res = float(input(f"Valor da resistência entre {no1} e {no2} (Ohms): "))
                elementos[(no1, no2, 'R')] = valor_res
            tensao = input(f"Existe uma fonte de corrente entre {no1} e {no2}? (s/n): ")
            if tensao.lower() == 's':
                valor_corrente = float(input(f"Valor da corrente entre {no1} e {no2} (Amper): "))
                elementos[(no1, no2, 'I')] = valor_corrente
    return nos, elementos
