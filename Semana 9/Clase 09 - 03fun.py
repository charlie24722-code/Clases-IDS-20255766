#Este modulo tendra funciones

# Una función tiene 2 tiempos

# Vamos a definir una función

def mi_funcion():
    """Esta función imprime un saludo"""
    print("Hola Mundo")
    print("amigo usuario")
    print("Gracias por usar nuestro sistema")
    
# Vamos a recibir información desde fuera de la función

def capturar_nombre():
    """Esta función recibe valores por medio de input"""
    nombre_input = input("Escriba su nombre: ")
    apellido_input = input("Digite su apellido:")
    nombre_completo = f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)
    
def capturar_usuario(nombre, edad):
    """Esta función recibe valores por medios de argumentos"""
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años de edad."
    print(texto)
    
# funcion que devuelve un valor

def calculo_de_impuesto(ventas):
    """Esta función calcula el valor de un impuesto"""
    if ventas < 500: 
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.25
    return tasa_impuesto

ventas = 1000
tasa_calculada = calculo_de_impuesto(ventas)
monto_impuesto = calculo_de_impuesto(ventas)*ventas
print(f"""el valor de la venta fue de {ventas:,.2f},
      la tasa de impuesto es {tasa_calculada:,.2f} 
      y el monto por tanto es {monto_impuesto:,.2f}""")