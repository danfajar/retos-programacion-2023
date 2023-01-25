'''
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''
p1 = 0
p2 = 0
game1 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

points_rule = {0:'Love',1:'15', 2:'30', 3:'40', 4:'Deuce', 5:'Ventaja' }

for i in game1:
    if i == "P1":
        p1 += 1
        p1p = points_rule[p1]
        p2p = points_rule[p2]
        print(f'{p1p} - {p2p}')
    else:
        p2 += 1
        p1p = points_rule[p1]
        p2p = points_rule[p2]
        print(f'{p1p} - {p2p}')

def marcador(p1,p2):
    
    if p1 == 3 and p2 == 3:
        print('Deuce')
    elif p1 > 3 or p2 > 3:


