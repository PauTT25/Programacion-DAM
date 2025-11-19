'''
En este ejercicio nos piden que utilizemos Python el cual hemos utilizado para trabajar con listas, diccionarios, funciones y bucles para organizar y mostrar información sobre películas y una serie de televisión favorita...
'''


peliculas_favoritas = ["cars","wall_e","shrek"]                          #Lista que contiene los nombres de las películas favoritas.
 
	cars = {                                                             #En este bloque empezamos a implementar los diccionarios.
    "titulo" : "cars",
    "director" : "John Lasseter",
    "año" : 2006
}

	wall_e = {
    "titulo" : "wall_e",
    "director" : "Andrew Stanton",
    "año" : 2008
}

	 shrek = {
    "titulo" : "shrek",
    "director" : "Andrew Adamson",
    "año" : 2001
}

primera_pelicula = peliculas_favoritas[0]                                         

if primera_pelicula == "cars":                                            #Si la primera pelicula coincide empezara a mostrar la informacion.
    print ("Titulo:",cars["titulo"])
    print ("Director:",cars["director"])
    print("Año:",cars["año"])
    
def mostrar_pelicula(pelicula):
    print("Titulo:",pelicula["titulo"])
    print("Director:",pelicula["director"])
    print("Año:",pelicula["año"])
    
for nombre in peliculas_favoritas:                                        #Aqui utilizamos un bucle para que pase por las peliculas que le hemos añadido. 
    
    if nombre == "cars":
        mostrar_pelicula(cars)
    
    if nombre == "wall_e":
        mostrar_pelicula(wall_e)
    
    if nombre == "shrek":
        mostrar_pelicula(shrek)
    
serie_favorita = {                                                        #Este diccionario representa la serie que le hemos añadido con su informacion correspondiente. 
    "titulo": "Breaking Bad",
    "director": "Vince Gilligan",
    "año": 2008,
    "temporadas": 5,
    "personaje_principal": "Walter White"
}
    
print("Serie favorita:")                                                  #Le decimos que nos muestre la informacion de la serie correspondiente. 
mostrar_pelicula(serie_favorita)

print("Temporadas:",serie_favorita["temporadas"])
print("Personaje principal:",serie_favorita["personaje_principal"])

'''
CONCLUSIÓN
Finalmente hemos demostrado como utilizar listas, diccionarios, bucles y funciones en Python para organizar y mostrar información de forma estructurada, llegando a reutilizar codigo para que se pueda comprender facilmente.
'''
