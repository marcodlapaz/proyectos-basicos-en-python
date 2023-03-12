import random


def adivina_el_numero_computadora(x):
    print("======================================")
    print("       ¡Bienvenido(a) al Juego!       ")
    print("======================================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else: 
            prediccion = limite_inferior
            
        respuesta = input(f"Mi predicción es: {prediccion}. \nSi es muy alta, ingresa (A). \nSi es muy baja, ingresa (B). \nSi es correcta, ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1 

    print(f"¡Siii! La computadora adivinó tu número correctamente {prediccion}")
    
adivina_el_numero_computadora(10)