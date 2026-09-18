pelicula = ("Nombre", "Genero", "Año", "Calificacion")
catalogo = []

def cargar_pelis():
    cantidad_peliculas=int(input("ingrese la cantidad de películas del catálogo: "))
    for i in range(cantidad_peliculas):
        pelicula = ( (str(input("Nombre: "))),
        (str(input("Genero: "))),
        (int(input("Año: "))),
        (int(input("Calificación (1-10): ")))
        )
        catalogo = pelicula

catalogo= [
        ('Mundial', 'Deporte', 2022, 10),
        ('Rambo','Accion',1999,8),
        ('Moana','Animado', 2019, 7),
        ('Star Wars','Ciencia ficción', 1970, 9)]
catalogo.sort(key=lambda x:x[3], reverse = True)
for i in range(len(catalogo)):
    print(f"{catalogo[i][0]:<10}"," | ",f"{catalogo[i][1]:<20}"," | ",catalogo[i][2]," | ",catalogo[i][3])