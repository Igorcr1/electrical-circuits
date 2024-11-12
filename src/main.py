from user_interface import coletar_dados_usuario
from calculations import calcular_correntes
from circuit_draw import desenhar_circuito

def main():
    # Coleta de dados do usuário
    nos, elementos = coletar_dados_usuario()
    #print(nos,elementos)
    '''
    # Cálculo das correntes e tensões
    try:
        tensoes_nos, correntes_elementos = calcular_correntes(nos, elementos)
    except Exception as e:
        print(f"Erro ao calcular correntes e tensões: {e}")
        return
    '''
    desenhar_circuito(nos,elementos)
    # Desenho do circuito
    #desenhar_circuito(['A', 'B', 'C', 'D'], {('A', 'B', 'R'): 2000.0, ('A', 'C', 'R'): 1000.0, ('A', 'D', 'V'): 10.0, ('B', 'C', 'R'): 2000.0, ('B', 'D', 'R'): 1000.0, ('C', 'D', 'R'): 2000.0})
    #desenhar_circuito(['A', 'B'], {('A', 'B', 'R'): 10.0, ('A', 'B', 'I'): 10.0})
    #desenhar_circuito(['A', 'B', 'C'], {('A', 'B', 'R'): 5.0, ('A', 'C', 'R'): 2.0, ('A', 'C', 'I'): 3.1, ('B', 'C', 'R'): 1.0, ('B', 'C', 'I'): -1.4})

    '''
    # Exibição dos resultados
    print("\nResultados:")
    for no, tensao in tensoes_nos.items():
        print(f"Tensão no nó {no}: {tensao:.2f} V")
    for elem, corrente in correntes_elementos.items():
        no1, no2, tipo = elem
        print(f"Corrente entre {no1} e {no2} ({tipo}): {corrente:.4f} A")
    '''
    
if __name__ == "__main__":
    main()

