'''
En este ejercicio del tema 3 nos estan pidiendo que hagamos un pequeño juego para adivinar un numero entre el 1 y el 50 en el cual solo tenemos 6 intentos para poder adivinarlo.
'''

import random                               #Aqui utilizamos el comando random el cual sirve para crear una biblioteca para  proporcionar funciones y asi generar números aleatorios para el programa.

numero_secreto = random.randint (1, 50)
assert 1 <= numero_secreto <= 50, "El número tiene que estar entre 1 y 50."

intentos_maximos = 6
intentos = 0 


print("Adivina el numero del 1 al 50")                              #Empezamos a decirle que nos imprima la frase para poder darle paso al inicio del ejercicio.                            

print("Tienes maximo hasta", intentos_maximos,"intentos")           #Aqui le decimos que nos imprima los intentos maximos posibles para adivinar el numero. 

while True:                                               

    assert intentos >= 0, "El contador no tiene que ser negativo."
    
    entrada = input("Introduce un numero:")
    
    try:
        numero = int(entrada)
    
    except ValueError:
        print("Este no es un numero valido, vuelve a probar.")
        continue
        
    if numero < 1 or numero > 50:
        print("El numero tiene que estar entre el 1 y el 50")
        continue
        
    intentos += 1
    
    if numero == numero_secreto:
        print("Has dicho el numero correcto.")
        break
    
    elif numero < numero_secreto:
        print("Demasiado bajo.")
        
    else:
        print("Demasiado alto.")
        
    if intentos == 3:
        if numero_secreto % 2 == 0:
            print( "Pista: el número es par.")
        else:
            print(" Pista: el número es impar.")
            
    if intentos == intentos_maximos and numero != numero_secreto:
        print("Te has quedado sin intentos, el numero secreto era",numero_secreto)
        break
				
'''
CONCLUSION
Finalmente hemos acabado haciendo el juego utilizando condicionales como pueden ser if, else, elif para poder controlar el sentido del juego y ir dando pistas al usuario. Tambien utilizando bucle como while  para poder hacer varios intentos hasta adivinar el numero. Al final en este ejercicios hemos tenido que aplicar extructuras de control, manejo de los errores y la logica de la programacion para hacer el programa funcional.
'''
