import sympy as sp

def calcular_correntes(nos, elementos):
    no_referencia = nos[-1]  # Define o último nó como referência
    tensoes = {no: sp.symbols(f"V_{no}") for no in nos if no != no_referencia}
    equacoes = []

    for no in nos:
        if no == no_referencia:
            continue
        soma_correntes = 0
        for elem, valor in elementos.items():
            no1, no2, tipo = elem
            if tipo == 'R':
                if no == no1:
                    outro_no = no2
                    V_no = tensoes[no]
                    V_outro_no = tensoes.get(outro_no, 0) if outro_no != no_referencia else 0
                    corrente = (V_no - V_outro_no) / valor
                    soma_correntes += corrente
                elif no == no2:
                    outro_no = no1
                    V_no = tensoes[no]
                    V_outro_no = tensoes.get(outro_no, 0) if outro_no != no_referencia else 0
                    corrente = (V_no - V_outro_no) / valor
                    soma_correntes += corrente
            elif tipo == 'V':
                # Implementar tratamento de fontes de tensão (supernós)
                pass  # Implementação adicional necessária
        equacoes.append(sp.Eq(soma_correntes, 0))

    solucoes = sp.solve(equacoes, list(tensoes.values()))
    tensoes_nos = {no: float(solucoes.get(tensoes[no], 0)) if no != no_referencia else 0 for no in nos}

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
            # Implementar cálculo de corrente em fontes de tensão se necessário
            pass

    return tensoes_nos, correntes_elementos
