producto = ("Nombre", "Stock", "Categoria")
lista_productos = []

def cargar_p(): 
    cantidad_de_p = int(input("Ingrese la cantidad de productos: "))
    for i in range (cantidad_de_p):
        producto = (
        (input("Ingrese el nombre del producto: ")),
        (int(input("Ingrese el numero de stock del producto: "))),
        (input("Ingrese la categoria del producto: ") )
        )
        lista_productos.append(producto)

lista_productos = [
    ("Leche", 3, "Lácteos"),
    ("Fideos", 15, "Almacén"),
    ("Galletitas", 2, "Dulces"),
    ("Arroz", 20, "Almacén"),
    ("Manteca", 5, "Lácteos")
]
lista_productos.sort(key=lambda x: x[1])
for i in range(len(lista_productos)):
    print("|",f"{lista_productos[i][0]:<10}"," | ",f"{lista_productos[i][1]:<3}"," | ",f"{lista_productos[i][2]:<10}","|") 

reponer=lista_productos[0][0]
print("Mandando",reponer,"a reponer")
lista_productos.pop(0)
lista_productos.sort(key=lambda x: x[0])
print("Orden alfabetico:")
for i in range(len(lista_productos)):
    print("|",f"{lista_productos[i][0]:<10}"," | ",f"{lista_productos[i][1]:<3}"," | ",f"{lista_productos[i][2]:<10}","|") 