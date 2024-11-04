import sympy as sp

def calcular_correntes(nos, elementos):
    # Definir o nó de referência
    no_referencia = nos[-1]
    
    # Criar variáveis simbólicas para as tensões em cada nó, exceto o nó de referência
    tensoes = {no: sp.symbols(f"V_{no}") for no in nos if no != no_referencia}
    
    equacoes = []

    # Montar as equações para cada nó
    for no in nos:
        # Não montar equação para o nó de referência
        if no == no_referencia:
            continue

        # Inicializar a soma das correntes entrando e saindo do nó
        soma_correntes = 0
        for elem, valor in elementos.items():
            no1, no2, tipo = elem

            if tipo == 'R':
                # Resistor: calcular a corrente aplicando a Lei de Ohm
                if no == no1 or no == no2:
                    outro_no = no2 if no == no1 else no1
                    V_no = tensoes.get(no, 0)
                    V_outro_no = tensoes.get(outro_no, 0) if outro_no != no_referencia else 0
                    corrente = (V_no - V_outro_no) / valor
                    soma_correntes += corrente

            elif tipo == 'V':
                # Fonte de tensão: adicionar equação específica para a diferença de potencial
                if no == no1:
                    equacoes.append(sp.Eq(tensoes.get(no, 0) - (tensoes.get(no2, 0) if no2 != no_referencia else 0), valor))
                elif no == no2:
                    equacoes.append(sp.Eq(tensoes.get(no, 0) - (tensoes.get(no1, 0) if no1 != no_referencia else 0), -valor))

        # Adicionar a equação da soma de correntes se não houver uma fonte de tensão impondo potencial fixo
        if soma_correntes != 0:
            equacoes.append(sp.Eq(soma_correntes, 0))

    # Printar o sistema de equações montado para depuração
    print("\nSistema de Equações Montado:")
    for eq in equacoes:
        print(eq)

    # Resolver o sistema de equações para encontrar as tensões nos nós
    try:
        solucoes = sp.solve(equacoes, list(tensoes.values()))
    except Exception as e:
        raise ValueError(f"Erro ao resolver o sistema de equações: {e}")

    # Se solucoes for uma lista, selecionar o primeiro resultado
    if isinstance(solucoes, list):
        if len(solucoes) > 0:
            solucoes = solucoes[0]
        else:
            raise ValueError("Nenhuma solução encontrada para o sistema de equações.")

    # Converter soluções simbólicas em valores numéricos para cada nó
    if isinstance(solucoes, dict):
        tensoes_nos = {no: float(solucoes.get(tensoes[no], 0)) if no != no_referencia else 0 for no in nos}
    else:
        raise ValueError("Erro inesperado: formato de soluções não reconhecido.")

    # Calcular correntes nos elementos
    correntes_elementos = {}
    for elem, valor in elementos.items():
        no1, no2, tipo = elem
        V_no1 = tensoes_nos[no1]
        V_no2 = tensoes_nos[no2]
        if tipo == 'R':
            corrente = (V_no1 - V_no2) / valor
            correntes_elementos[elem] = corrente
        elif tipo == 'V':
            # Correntes em fontes de tensão precisam de uma abordagem diferente (usando equações de malha, por exemplo)
            correntes_elementos[elem] = (V_no1 - V_no2) / valor if valor != 0 else 0

    return tensoes_nos, correntes_elementos
