estudiantes=[]

def agregar_estudiante(nombre):
    estudiantes.append(nombre)

def mostrar_estudiantes():
    print("\nLista de estudiantes")
    if len(estudiantes)==0:
        print("No hay estudiantes registrados")
    else:
        for estudiante in estudiantes:
            print("-",estudiante)

agregar_estudiante("Ana")
agregar_estudiante("Carlos")
agregar_estudiante("Laura")

mostrar_estudiantes()