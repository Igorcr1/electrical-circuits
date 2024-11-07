def coletar_dados_usuario():
    n=0
    elementos = {}
    num_nos = limit()
    while (n != 4):
        n = menu(elementos)
    return elementos


def menu(elementos): 
    '''É preciso dar a orientação de cada objeto, para  desenha-lo. Vamos definir uma forma de fazer isso
        por exemplo elm.Resistor().down() vamos falar pro usuario colocar B-baixo, C-cima, E-Esquerda ou D- Direita'''
    escolha = input(f'Bem-vindo(a), o que deseja fazer? \n1- Verificar o que já foi adicionado;\n2- Adicionar elemento;\n3- Excluir elemento \n4- Passar pro próximo no\n')
    if escolha == '1':
        print(elementos)
    elif escolha == '2':
        print('A adição de elementos requer cuidados, você deve usar o valor+letra de refêrencia ao elemento(V para fonte de tensao)+a letra referência(C-cima,D-Direita,E-Esquerda,B-baixo), ex:10+V+D - tensão 10V a direita')
        elem = input('Elementos:\nV - Fonte de tensão\nA-Fonte de corrente\nR-Resistor\nG-Terra. Lembrando: Valor+Elemento+Orientação\n')
        part = elem.split(sep='+')
        elementos[(0, 0, part[1], part[2])] = float(part[0])
        #É O SEGUINTE, TIREI OS NÓS E COLOQUEI COORDENADA CARTESIANA. (0,0) isso será alterado quando o objeto for plotado, teremos um mapa bidimensional.
    elif escolha == '3':
        print(elementos.values())
        escolha = input('Copie a chave que deseja remover')
        elementos.pop(escolha, None)
    elif escolha == '4':
        return 4
    
def limit():
    num_nos = int(input("Digite a quantidade de nós no circuito:\n "))
    while(num_nos <= 0 or num_nos > 5):
        print('você deve especificar até 5 nós.')
        num_nos = int(input("Digite a quantidade de nós no circuito:\n "))
