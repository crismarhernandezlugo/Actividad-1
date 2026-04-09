# Importamos las funciones desde el módulo de operaciones
from modules.operaciones import (
    registrar_producto, 
    listar_productos, 
    buscar_producto, 
    editar_producto, 
    eliminar_producto
)
from modules.validaciones import validar_entero, limpiar_pantalla, pausar

def mostrar_menu():
    print("\n" + "="*30)
    print("   SISTEMA DE INVENTARIO")
    print("="*30)
    print("1. Registrar Producto")
    print("2. Listar Todo el Inventario")
    print("3. Buscar Producto por ID")
    print("4. Editar Producto")
    print("5. Eliminar Producto")
    print("6. Salir")
    print("="*30)

def ejecutar_sistema():
    while True:
        limpiar_pantalla()  # Limpia antes de mostrar el menú
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            limpiar_pantalla()
            registrar_producto()
            pausar() 
        elif opcion == "2":
            limpiar_pantalla()
            listar_productos()
            pausar()
        elif opcion == "3":
            limpiar_pantalla()
            buscar_producto()
            pausar()
        elif opcion == "4":
            limpiar_pantalla()
            editar_producto()
            pausar()
        elif opcion == "5":
            limpiar_pantalla()
            eliminar_producto()
            pausar()
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("\nOpción no válida.")
            pausar()


# Este bloque asegura que el programa solo corra si ejecutas este archivo
if __name__ == "__main__":
    ejecutar_sistema()
