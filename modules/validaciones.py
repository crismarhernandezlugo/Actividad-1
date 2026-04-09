import os
def validar_entero(mensaje):
    """Asegura que el usuario ingrese un número sin decimales"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print(" Error: Debes ingresar un número entero (ej: 1, 10, 500).")

def validar_flotante(mensaje):
    """Asegura que el usuario ingrese un número que puede tener decimales"""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print(" Error: Debes ingresar un valor numérico (ej: 10.50 o 5).")

def validar_texto(mensaje):
    """Asegura que el texto no esté vacío"""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print(" Error: Este campo no puede quedar vacío.")
        
def limpiar_pantalla():
    # En Pydroid 3 el comando 'clear' limpia la consola
    os.system('clear')

def pausar():
    input("\n Presiona Enter para continuar...")

