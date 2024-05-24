import json
import os

ruta_archivo = "TP5.json"

def cargar_datos(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo,"r") as archivo:
            try:
                datos = json.load(archivo)
                return datos
            except json.JSONDecodeError:
                return{}
    else:
        return{}
    
def guardar_datos(ruta_archivo,datos):
    with open(ruta_archivo,"w") as archivo:
        json.dump(datos,archivo,indent=4)

datos = cargar_datos(ruta_archivo)
print("Listado de alumnos: ", datos)
datos["nuevo_dato"] = "valor"
guardar_datos(ruta_archivo,datos)
print("Listado de alumnos", datos)