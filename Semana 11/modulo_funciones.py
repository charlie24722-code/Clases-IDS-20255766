# En este modulo desarrollamos la logica para el sistema

# Importamos el modulo de datos
import modulo_datos as dat
def registrar_estudiante():
    """Funcion que valida y registra estudiante"""
    while True:
        carnet_i = input("Digite el número de carnet: ")
        existe = "No"
        for e in dat.estudiantes:
            if e ["carnet"] == carnet_i:
                existe = "Si"
        if len(carnet_i) >= 6 and len(carnet_i) <= 10 and existe == "No":
            break
        else: 
            print("El largo debe ser mayor a 5 y menor a 11, y el carnet no debe existir.")
               
    while True:
        nombre_i = input("Digite el nombre del estudiante: ")
        if len(nombre_i) > 1:
            break
        else:
            print("El largo del nombre debe ser al menos 2")
    
    while True: 
        apellido_i = input("Digite el apellido del estudiante: ")
        if len(apellido_i) > 1:
            break
        else:
            print("El largo del apellido debe ser al menos 2")
    
    dat.estudiantes.append({
        "carnet": carnet_i,
        "nombre": nombre_i,
        "apellido": apellido_i  
    })
    # print(dat.estudiantes)

def inscribir_en_cursos():
    """Función para registrar alumnos por curso"""
    try:
        while True:
            carnet = input("Digite su número de carnet(si desea regresar al menu, digite salir): ")
            if carnet.lower() == "salir":
                print("Regresaras al menu principal...")
                return
            elif not carnet:
                print("Debe llenar este campo.")
            estudiante_existe = False
            for estudiante in dat.estudiantes:
                if estudiante["carnet"] == carnet:
                    estudiante_existe = True
                    break
                elif not estudiante_existe:
                    print("El carnet no existe en el sistema.")
            break
        for codigo, descripciones in dat.cursos.items():
            print(f"{codigo}: {descripciones}")
        while True:
            codigo_curso = input("Ingrese el codigo del curso a inscribirse: ")
            if not codigo_curso:
                print("Es necesario completar este campo.")
            elif codigo_curso not in dat.cursos:
                print("No existe ese codigo")
                inscrito = False
            for codigero in dat.Inscripciones:
                if codigero[0] == carnet and dat.Inscripciones == codigo_curso:
                    inscrito = True
                    break
            if inscrito:
                print(f"El estudiante ya esta inscrito en {codigo_curso}")
            break
        nueva_inscripcion = (carnet, codigo_curso)
        dat.Inscripciones.append(nueva_inscripcion)
        print(f"El estudiante con carnet {carnet} ha sido inscrito exitosamente a {codigo_curso}") 
    except Exception as e:
        print(f"Error inesperado en el curso: {e}")
        
def generar_reporte():
    """Esta función genera un reporte de inscripciones"""
    if len(dat.Inscripciones) == 0:
        print("No hay inscripciones realizadas")
        return
    try:
        print("Selecciona el tipo de curso")
        print("1. PY - Python basico")
        print("2. JS - JavaScript para principiantes")
        print("3. BD - Introducción a bases de datos")
        print("4. SE - Seguridad en entornos digitales")
        print("5. Estudiates sin inscripciones")
        opcion = input("Seleccione la opción del menu (1-5): ")
        
        opciones_cursos = {
            "1": "PY",
            "2": "JS",
            "3": "BD",
            "4": "SE"
        }
        if opcion in opciones_cursos:
            codigo_curso = opciones_cursos[opcion]
            print(f"Reporte: {dat.cursos[codigo_curso]} {codigo_curso}")
            carnets_inscritos = []
            for inscr in dat.Inscripciones:
                if inscr[1] == codigo_curso:
                    carnets_inscritos.append(inscr[0])
            if len(carnets_inscritos) == 0:
                print("No hay estudiantes inscritos")
            else:
                print(f"Estudiantes inscritos {len(carnets_inscritos)}:")
                for carns in carnets_inscritos:
                    print(f"\t -{carns}")
        elif opcion == "5":
            print("Reporte: Estudiantes sin inscripciones")
            carnets_con_incscripcion = []
            for inscr in dat.Inscripciones:
                if inscr[0] not in carnets_con_incscripcion:
                    carnets_con_incscripcion.append(inscr[0])
            estudiantes_sin_inscripcion = []
            for est in dat.estudiantes:
                if est["carnet"] not in carnets_con_incscripcion:
                    estudiantes_sin_inscripcion.append(est["carnet"])
            if len(estudiantes_sin_inscripcion) == 0:
                print("Todos los estudiantes tienen inscripciones")
            else:
                print(f"Estudiantes sin inscripciones {len(estudiantes_sin_inscripcion)}:")
                for est_sin in estudiantes_sin_inscripcion:
                    print(f"\t -{est_sin["carnet"], est_sin["nombre"], est_sin["apellido"]}")
        else:
            print("Opción no válida.")
    except Exception as e:
        print(f"Error inesperado en el reporte: {e}")
    
                