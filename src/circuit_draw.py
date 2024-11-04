import schemdraw
import schemdraw.elements as elm

def desenhar_circuito(nos, elementos):
    d = schemdraw.Drawing()
    posicoes_nos = {}
    x = 0
    # Posicionar os nós
    for no in nos:
        posicoes_nos[no] = (x, 0)
        d += elm.Dot().at((x, 0)).label(no)
        x += 2

    # Desenhar os elementos entre os nós
    for elem, valor in elementos.items():
        no1, no2, tipo = elem
        pos1 = posicoes_nos[no1]
        pos2 = posicoes_nos[no2]
        if tipo == 'R':
            d += elm.Resistor().at(pos1).to(pos2).label(f"{valor}Ω")
        elif tipo == 'V':
            d += elm.SourceV().at(pos1).to(pos2).label(f"{valor}V")
    d.draw()
