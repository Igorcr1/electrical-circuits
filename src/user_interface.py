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
            tensao = input(f"Existe uma fonte de tensão entre {no1} e {no2}? (s/n): ")
            if tensao.lower() == 's':
                valor_tensao = float(input(f"Valor da tensão entre {no1} e {no2} (Volts): "))
                elementos[(no1, no2, 'V')] = valor_tensao
    return nos, elementos
