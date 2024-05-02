""" Trabajo Practico N° 5
Nombre y Apellido: MARIA CONSTANZA SCARCELLA
Comisión: Jueves - virtual
"""
"""
1) Hacer un programa que gestiones datos para una escuela.
El programa tiene que ser capaz de:
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, 
Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las 
notas, cantidad de faltas, cantidad de amonestaciones recibidas.
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos
"""

def agregar_alumnos (codigo, nombre, apellido, fecha_nacimiento, dni, tutor):
    alumno = {
        "Nombre": nombre,
        "Apellido":apellido,
        "Fecha de nacimiento": fecha_nacimiento,
        "DNI": dni,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0 ,
        "Amonestaciones": 0
    }
    codigo[dni] = alumno
    
      
def mostrar_datos_alumnos (codigo,dni):
    if dni in codigo:
        print (f"Los datos del alumno con dni", dni, "son :")
        for clave,valor in codigo[dni].items():
            print(clave , " :", valor)
    else:
        print("El alumno no se encontro en la base de datos")

def modificar_datos_alumnos (codigo,dni):
    if dni in codigo:
        print(f"Elija el campo que desea modificar: ")
        print("A - Nombre")
        print("B - Apellido")
        print("C - Fecha de nacimiento")
        print("D - Tutor")
        opcion = input("Escriba la opcion del campo a modificar: ")
        nuevo_dato = input("Ingrese el dato correcto: ")
        
        if opcion == "A":
            codigo[dni]["Nombre"]=nuevo_dato
        elif opcion == "B":
            codigo[dni]["Apellido"]=nuevo_dato
        elif opcion == "C":
            codigo[dni]["Fecha de nacimiento"]=nuevo_dato
        elif opcion == "D":
            codigo[dni]["Tutor"]=nuevo_dato
        else:
            print("No se encontro el alumno")
              

def agregar_notas (codigo,dni,nota):
    if dni in codigo:
        codigo[dni]["Notas"].append(nota)
    else:
        print("El alumno no esta registrado")
        
def agregar_faltas (codigo,dni):
    if dni in codigo:
        codigo[dni]["Faltas"]+=1
    else:
        print("El alumno no esta registrado")

def agregar_amonestaciones (codigo,dni):
    if dni in codigo:
        codigo[dni]["Amonestaciones"] += 1
    else:
        print("El alumno no esta registrado")

def remover_alumnos(codigo,dni): 
    if dni in codigo:
        print(input("Esta seguro que desea remover al alumno ? Si / No : "))
        respuesta = "Si"
        if respuesta == "Si":
             del codigo[dni]
             print("El alumno fue eliminado de la base de datos")
        else:
            print("Ningun alumno fue eliminado")

def menu():
    print("Seleccione una opcion del Menu : ")
    print("1. Consultar datos de un alumno")
    print("2. Modificar datos de un alumno")
    print("3. Agregar un nuevo alumno")
    print("4. Eliminar un alumno")
    print("5. Agregar Notas")
    print("6. Agregar faltas")
    print("7. Agregar amonestaciones")
    print("8. Salir ")
    
base_datos_alumnos ={}
while True:
    menu()
    opcion = input("Ingrese el numero de la opcion deseada: ")
    if opcion =="1":
        dni = input("Ingrese el DNI del alumno: ")
        mostrar_datos_alumnos(base_datos_alumnos,dni)
        
    elif opcion =="2":
        dni = input("Ingrese el DNI del alumno: ")
        modificar_datos_alumnos(base_datos_alumnos,dni)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
        dni = input("Ingrese el DNI: ")
        tutor =input ("Ingrese el nommbre del tutor: ")
        agregar_alumnos(base_datos_alumnos,nombre,apellido,fecha_nacimiento,dni,tutor)
    elif opcion == "4":
         dni = input("Ingrese el DNI del alumno que sea remover: ")
         remover_alumnos(base_datos_alumnos,dni)
    elif opcion =="5":
        dni = input("Ingrese el DNI del alumno: ")
        nota = int(input("Ingrese la nota a agregar: "))
        agregar_notas(base_datos_alumnos,dni,nota)
    elif opcion =="6":
        dni = input("Ingrese el DNI del alumno: ")
        agregar_faltas(base_datos_alumnos,dni)
    elif opcion == "7":
        dni = input("Ingrese el DNI del alumno: ")
        agregar_amonestaciones(base_datos_alumnos,dni)
    else:
        print("Hasta luego")
        break