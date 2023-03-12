import random

def adivina_el_numero(x):
    print("======================================")
    print("       ¡Bienvenido(a) al Juego!       ")
    print("======================================")
    print("Tu meta es adivinar el número generado por la computadora.")

    numero_aleatorio = random.randint(1, x)
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print(f"Intenta otra vez. {prediccion} es muy pequeño")
        elif prediccion > numero_aleatorio:
            print(f"Intenta otra vez. {prediccion} es muy grande")
    
    print(f"¡Felicidades! Adivinaste el número {numero_aleatorio}")


adivina_el_numero(10)