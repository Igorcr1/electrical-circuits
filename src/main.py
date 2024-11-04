from user_interface import coletar_dados_usuario
from calculations import calcular_correntes
from circuit_draw import desenhar_circuito

def main():
    # Coleta de dados do usuário
    nos, elementos = coletar_dados_usuario()
    
    # Cálculo das correntes e tensões
    try:
        tensoes_nos, correntes_elementos = calcular_correntes(nos, elementos)
    except Exception as e:
        print(f"Erro ao calcular correntes e tensões: {e}")
        return
    
    # Desenho do circuito
    desenhar_circuito(nos, elementos)
    
    # Exibição dos resultados
    print("\nResultados:")
    for no, tensao in tensoes_nos.items():
        print(f"Tensão no nó {no}: {tensao:.2f} V")
    for elem, corrente in correntes_elementos.items():
        no1, no2, tipo = elem
        print(f"Corrente entre {no1} e {no2} ({tipo}): {corrente:.4f} A")

if __name__ == "__main__":
    main()
