# Aventura 

print("¡Bienvenido a la aventura!")
nombre = input("Introduce tu nombre: ")

# Inicio de la aventura
print(f"\nHola {nombre}, despiertas en un bosque misterioso.")
print("Frente a ti hay dos caminos:")
print("1. Tomar el camino a la derecha")
print("2. Tomar el camino a la izquierda")

# Elección de caminos
eleccion = input("¿Qué camino eliges? (1/2): ")

if eleccion == '1':
    print("\nTomas el camino a la derecha y llegas a un río.")
    print("Ves un puente viejo y roto, y un bote pequeño.")
    print("1. Cruzar por el puente.")
    print("2. Usar el bote.")
    
    eleccion_rio = input("¿Qué haces? (1/2): ")
    
    if eleccion_rio == '1':
        print("\nIntentas cruzar el puente, pero se rompe y caes al río.")
        print("Nadas hacia la orilla, pero decides volver al bosque. Fin de la aventura.")
    elif eleccion_rio == '2':
        print("\nUsas el bote para cruzar el río. Llegas a salvo al otro lado.")
        print("Caminas un poco más y encuentras una cueva misteriosa.")
        print("1. Entrar en la cueva.")
        print("2. Rodear la cueva y seguir tu camino.")
        
        eleccion_cueva = input("¿Qué haces? (1/2): ")
        
        if eleccion_cueva == '1':
            print("\nEntras en la cueva y encuentras un tesoro escondido. ¡Has ganado la aventura!")
        elif eleccion_cueva == '2':
            print("\nDecides rodear la cueva y continúas tu camino, pero te pierdes en el bosque. Fin de la aventura.")
        else:
            print("\nOpción no válida. Fin de la aventura.")
    else:
        print("\nOpción no válida. Fin de la aventura.")
        
elif eleccion == '2':
    print("\nTomas el camino a la izquierda y llegas a una montaña.")
    print("Ves dos opciones para escalar la montaña.")
    print("1. Subir por el sendero empinado.")
    print("2. Usar un teleférico viejo.")
    
    eleccion_montana = input("¿Qué haces? (1/2): ")
    
    if eleccion_montana == '1':
        print("\nSubes por el sendero empinado. Es difícil, pero logras llegar a la cima.")
        print("Desde la cima, disfrutas de una hermosa vista. ¡Felicidades, has ganado la aventura!")
    elif eleccion_montana == '2':
        print("\nTe subes al teleférico, pero este se detiene a mitad de camino y quedas atrapado.")
        print("Después de horas de espera, eres rescatado, pero decides no continuar la aventura. Fin de la aventura.")
    else:
        print("\nOpción no válida. Fin de la aventura.")
        
else:
    print("\nOpción no válida. Fin de la aventura.")