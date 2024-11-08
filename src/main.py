from user_interface import coletar_dados_usuario
from calculations import calcular_correntes
from circuit_draw import desenhar_circuito

def main():
    # Coleta de dados do usuário
    elementos = coletar_dados_usuario()
    
    # Desenho do circuito
    desenhar_circuito(elementos)
    #desenhar_circuito(elementos = {(0, 0, 'V', 'C'): 10.0, (0, 0, 'R', 'D'): 10.0, (0, 0, 'R', 'B'): 10.0})

'''

    # Cálculo das correntes e tensões
    try:
        tensoes_nos, correntes_elementos = calcular_correntes(nos, elementos)
    except Exception as e:
        print(f"Erro ao calcular correntes e tensões: {e}")
        return
    
    
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
