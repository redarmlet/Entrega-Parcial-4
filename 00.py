compradores[
    {"Nombre":"Ignacio","Edad":"23"}
]
def funcion():
    Encontrado = False
    Nombre=int(input("Ingrese Nombre"))
    for name in compradores:
        if name["Nombre"]==Nombre:
            Encontrado = True
    if not Encontrado:
        return
    
"""
para borrar:
compradores.remove(name)

para agregar un diccionario a la lista:
compradores.append(
{"Nombre": Nombre, "Edad": Edad}
)
hay que definir las variables Nombre
y edad previamente obvio.
"""