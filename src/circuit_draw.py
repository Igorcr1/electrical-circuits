import schemdraw
import schemdraw.elements as elm

def desenhar_circuito(nos, elementos):
    #Vamos definir para somente 5 nós.
    match len(nos):
        case 2:
            d, posicoes = basico(nos,elementos,index=2)
            d.draw()
        case 3:
            d, posicoes = basico(nos,elementos,index=3)
            d,posicoes = sec_basico(nos,elementos,d,posicoes)
            d.draw()
        case 4:
            d, posicoes = basico(nos,elementos,index=4)
            d.draw()
        case 5:
            d, posicoes = basico(nos,elementos,index=5)
            pass


def basico(nos,elementos,index=2):
    # fonte de tensao/corrente, resistor, o ground e fecha

    terra = nos[-1]
    posicoes = {}
    
    d = schemdraw.Drawing()
    for elem,valor in elementos.items():
        x,y,tipo = elem
        if(tipo == 'R' and x=='A' and y=='B'):
            posicoes['B'] = (d.here)
            d += elm.Resistor().left().label(f'{valor}')
            posicoes['A'] = (d.here)
        elif(tipo == 'I' and x=='A' and y=='B'):
            posicoes['A'] = (d.here)
            d += elm.Line().up()
            if (index == 2):
                d += elm.Ground().left()
            d += elm.SourceI().right().label(f'{valor}')
            d += elm.Line().down()
            d += elm.Dot().label('A')
            posicoes['B'] = (d.here)
        elif(tipo == 'V' and x=='A' and y=='B'):
            posicoes['A'] = (d.here)            
            d += elm.Line().up()
            d += elm.Ground().left()
            d += elm.SourceV().right().label(f'{valor}')
            d += elm.Line().down()
            d += elm.Dot().label('A')
            posicoes['B'] = (d.here)
        # Se não houver,A,B vc precisa meter uma linha pra indicar A E B
    return d,posicoes


def sec_basico(nos,elementos,d,posicoes):
    for elem,valor in elementos.items():
        x,y,tipo = elem
        #Bloco 1
        if(tipo == 'R' and x == 'A' and y == 'C'):
            d += elm.Resistor().at(posicoes[f'{x}']).down().label(f'{valor}')
            posicoes['C'] = (d.here)
        elif(tipo == 'I' and x == 'A' and y == 'C'):
            d += elm.Line().at(posicoes[f'{x}']).left()
            d += elm.SourceI(reverse=orit_reverse(valor)).down().label(f'{(valor)}')
            d += elm.Line().right()
            posicoes['C'] = (d.here)
        #Aqui tambem precisa de um elif 

        #bloco 2
        elif(tipo == 'R' and x == 'B' and y == 'C'):
            d += elm.Resistor().at(posicoes[f'{x}']).down().label(f'{valor}')
        elif(tipo == 'I' and x == 'B' and y == 'C'):
            d += elm.Line().at(posicoes[f'{x}']).right()
            d += elm.SourceI().down().label(f'{(valor)}')
            d += elm.Line().left()
            d += elm.Line().left()
            d += elm.Ground()
            posicoes['C'] = (d.here)
    return d,posicoes
    
def terc_basico(nos,elementos,d,posicoes):
    pass


def orit_reverse(valor): # A construção de algumas imagens necessita inverter o valor, sim, é uma gambiarra
    if valor > 0:
        return True
    else:
        return False

