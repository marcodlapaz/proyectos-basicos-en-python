import random


def jugar():
    usuario = input("Escoge una opción: 'pi' para pieda, 'pa' para papel, 'ti' para tijeras.\n").lower()
    computadora = random.choice(["pi", "pa", "ti"])
    
    if usuario == computadora:
        return f"{usuario} | {computadora} - ¡Empate!"

    if gano_el_jugador(usuario, computadora):
        return f"{usuario} | {computadora} - ¡Ganaste!"
    
    return f"{usuario} | {computadora} - ¡Perdiste!"


def gano_el_jugador(jugador, oponente):
    if (jugador == "pi" and oponente == "ti") or (jugador == "pa" and oponente == "pi") or (jugador == "ti" and oponente == "pa"):
        return True
    else:
        return False
    
    
print(jugar())