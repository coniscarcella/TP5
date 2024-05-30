import json

def guardar_datos(codigo, archivo):
    with open(archivo, 'w') as f:
        json.dump(codigo, f, indent=4)
    print("Datos guardados en el archivo.")


def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}


def agregar_alumnos(codigo, nombre, apellido, fecha_nacimiento, dni, tutor):
    try:
        dni = int(dni)  # Intentar convertir el DNI a entero
    except ValueError:
        raise ValueError("El DNI debe ser un número entero.")

    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha de nacimiento": fecha_nacimiento,
        "DNI": dni,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    codigo[dni] = alumno
    print("El alumno fue agregado a la base de datos")
    guardar_datos(codigo, "alumnos.json")


def mostrar_datos_alumnos(codigo, dni):
    try:
        dni = int(dni)
    except ValueError:
        print("El DNI debe ser un número entero.")
        return

    if dni in codigo:
        print(f"Los datos del alumno con DNI {dni} son:")
        for clave, valor in codigo[dni].items():
            print(f"{clave} : {valor}")
    else:
        print("El alumno no se encontró en la base de datos")


def modificar_datos_alumnos(codigo, dni):
    try:
        dni = int(dni)
    except ValueError:
        print("El DNI debe ser un número entero.")
        return

    if dni in codigo:
        print("Elija el campo que desea modificar:")
        print("A - Nombre")
        print("B - Apellido")
        print("C - Fecha de nacimiento")
        print("D - Tutor")
        opcion = input("Escriba la opción del campo a modificar: ")
        nuevo_dato = input("Ingrese el dato correcto: ")

        if opcion == "A":
            codigo[dni]["Nombre"] = nuevo_dato
        elif opcion == "B":
            codigo[dni]["Apellido"] = nuevo_dato
        elif opcion == "C":
            codigo[dni]["Fecha de nacimiento"] = nuevo_dato
        elif opcion == "D":
            codigo[dni]["Tutor"] = nuevo_dato
        else:
            print("Opción no válida")
        
        print("Los datos del alumno han sido actualizados.")
        guardar_datos(codigo, "alumnos.json")
    else:
        print("El alumno no se encontró en la base de datos")


def agregar_notas(codigo, dni, nota):
    try:
        dni = int(dni)
    except ValueError:
        print("El DNI debe ser un número entero.")
        return

    if dni in codigo:
        codigo[dni]["Notas"].append(nota)
        guardar_datos(codigo, "alumnos.json")
    else:
        print("El alumno no está registrado")


def agregar_faltas(codigo, dni):
    try:
        dni = int(dni)
    except ValueError:
        print("El DNI debe ser un número entero.")
        return

    if dni in codigo:
        codigo[dni]["Faltas"] += 1
        guardar_datos(codigo, "alumnos.json")
    else:
        print("El alumno no está registrado")


def agregar_amonestaciones(codigo, dni):
    try:
        dni = int(dni)
    except ValueError:
        print("El DNI debe ser un número entero.")
        return

    if dni in codigo:
        codigo[dni]["Amonestaciones"] += 1
        guardar_datos(codigo, "alumnos.json")
    else:
        print("El alumno no está registrado")


def remover_alumnos(codigo, dni):
    try:
        dni = int(dni)
    except ValueError:
        print("El DNI debe ser un número entero.")
        return

    if dni in codigo:
        respuesta = input("¿Está seguro que desea remover al alumno? Si / No: ")
        if respuesta.lower() == "si":
            del codigo[dni]
            print("El alumno fue eliminado de la base de datos")
            guardar_datos(codigo, "alumnos.json")
        else:
            print("Ningún alumno fue eliminado")
    else:
        print("El alumno no se encontró en la base de datos")


def menu():
    print("Seleccione una opción del menú:")
    print("1. Consultar datos de un alumno")
    print("2. Modificar datos de un alumno")
    print("3. Agregar un nuevo alumno")
    print("4. Eliminar un alumno")
    print("5. Agregar notas")
    print("6. Agregar faltas")
    print("7. Agregar amonestaciones")
    print("8. Salir")


base_datos_alumnos = cargar_datos("alumnos.json")

while True:
    menu()
    opcion = input("Ingrese el número de la opción deseada: ")

    try:
        if opcion == "1":
            dni = input("Ingrese el DNI del alumno: ")
            mostrar_datos_alumnos(base_datos_alumnos, dni)

        elif opcion == "2":
            dni = input("Ingrese el DNI del alumno: ")
            modificar_datos_alumnos(base_datos_alumnos, dni)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
            dni = input("Ingrese el DNI del alumno: ")
            tutor = input("Ingrese el nombre del tutor: ")
            agregar_alumnos(base_datos_alumnos, nombre, apellido, fecha_nacimiento, dni, tutor)

        elif opcion == "4":
            dni = input("Ingrese el DNI del alumno que desea remover: ")
            remover_alumnos(base_datos_alumnos, dni)

        elif opcion == "5":
            dni = input("Ingrese el DNI del alumno: ")
            nota = int(input("Ingrese la nota a agregar: "))
            agregar_notas(base_datos_alumnos, dni, nota)

        elif opcion == "6":
            dni = input("Ingrese el DNI del alumno: ")
            agregar_faltas(base_datos_alumnos, dni)

        elif opcion == "7":
            dni = input("Ingrese el DNI del alumno: ")
            agregar_amonestaciones(base_datos_alumnos, dni)

        elif opcion == "8":
            print("Hasta luego")
            break

        else:
            print("Opción no válida")
    except ValueError:
        print("El DNI debe ser un número entero")
