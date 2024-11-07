import schemdraw
import schemdraw.elements as elm

def desenhar_circuito(elementos):
    d = schemdraw.Drawing()
    novo_elementos = {}
    numero_de_elementos = len(elementos) #Esse é o ultimo
    i = 0 #Contador para fechar o circuito, falta QI pra fazer algo normal
    for elem, valor in elementos.items():
        x, y, tipo, orientacao = elem
        if(i==0): #O primeiro elemento precisa ter uma variavel diferente pra fechar o circuito.
            a = tipagem_do_elemento(tipo,valor,orientacao)
            d += a
            novo_elementos[(d.here[0],d.here[1], tipo, orientacao)] = valor
        else:
            c = tipagem_do_elemento(tipo,valor,orientacao)
            d += c
            novo_elementos[(d.here[0],d.here[1], tipo, orientacao)] = valor
        i += 1
        if (numero_de_elementos == i):
            fech = fechando_circuito(elementos,a)
            d += fech
            novo_elementos[(d.here[0],d.here[1], tipo, orientacao)] = valor
    elementos = novo_elementos #Aqui a coisa fica legal, o dict antigo deixa de existir e o novo tem x,y
    d += nos(elementos)
    d.draw()


def tipagem_do_elemento(tipo,valor,orientacao):
    if orientacao == 'C':
        orit = 'up'
    elif orientacao == 'B':
        orit = 'down'
    elif orientacao == 'E':
        orit = 'left'
    elif orientacao == 'D':
        orit = 'right'

    if tipo == 'R':
        c = elm.Resistor(d=f'{orit}').label(f"{valor} Ohms")
    elif tipo == 'V':
        c = elm.SourceV(d=f'{orit}').label(f"{valor} V")
    elif tipo =='A':
        c = elm.SourceI(d=f'{orit}').label(f"{valor} A")
    elif tipo == 'G':
        c = elm.Ground(d=f'{orit}')
    elif tipo == 'L':
        c = elm.Line(d=f'{orit}')
    return c

def fechando_circuito(elementos,a):
    fech = elm.Line().tox(a.start)
    return fech


def nos(elementos):
    n = int(input('Onde você quer colocar o nó? Os elementos do circuito aparecerão em ordem. Será possível começar a colocar')) - 1
    element = list(elementos.keys())
    return elm.Dot().at((element[n][0], element[n][1]))
