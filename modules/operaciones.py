from utils.archivos import guardar_json, cargar_json
from modules.validaciones import validar_entero, validar_flotante

def registrar_producto():
    productos = cargar_json()
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    
    id_p = validar_entero("ID (Código numérico): ")
    # Verificar que el ID no exista ya
    for p in productos:
        if p['id'] == id_p:
            print("Error: Este ID ya existe en el inventario.")
            return

    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = validar_flotante("Precio unitario: ")
    stock = validar_entero("Cantidad en existencia: ")
    
    nuevo = {
        "id": id_p,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    
    productos.append(nuevo)
    guardar_json(productos)
    print(f"¡{nombre} registrado con éxito!")

def listar_productos():
    productos = cargar_json()
    if not productos:
        print("\n El inventario está vacío.")
        return
    
    print("\n--- LISTA DE PRODUCTOS ---")
    print(f"{'ID':<10} {'NOMBRE':<20} {'STOCK':<10} {'PRECIO':<10}")
    print("-" * 50)
    for p in productos:
        print(f"{p['id']:<10} {p['nombre']:<20} {p['stock']:<10} ${p['precio']:<10}")

def buscar_producto():
    productos = cargar_json()
    id_buscado = validar_entero("Ingrese el ID a buscar: ")
    
    for p in productos:
        if p['id'] == id_buscado:
            print("\nPRODUCTO ENCONTRADO:")
            print(f"Nombre: {p['nombre']}\nCategoría: {p['categoria']}\nStock: {p['stock']}\nPrecio: ${p['precio']}")
            return
    print(" No se encontró ningún producto con ese ID.")

def editar_producto():
    productos = cargar_json()
    id_buscado = validar_entero("Ingrese el ID del producto a editar: ")
    
    for p in productos:
        if p['id'] == id_buscado:
            print(f"\nEditando: {p['nombre']}")
            p['nombre'] = input(f"Nuevo nombre (presiona Enter para mantener '{p['nombre']}'): ") or p['nombre']
            p['categoria'] = input(f"Nueva categoría (presiona Enter para mantener '{p['categoria']}'): ") or p['categoria']
            p['precio'] = validar_flotante("Nuevo precio: ")
            p['stock'] = validar_entero("Nuevo stock: ")
            
            guardar_json(productos)
            print("Producto actualizado correctamente.")
            return
    print(" ID no encontrado.")

def eliminar_producto():
    productos = cargar_json()
    id_buscado = validar_entero("Ingrese el ID del producto a eliminar: ")
    
    # Filtramos la lista: dejamos todos menos el que tiene el ID buscado
    lista_nueva = [p for p in productos if p['id'] != id_buscado]
    
    if len(lista_nueva) < len(productos):
        guardar_json(lista_nueva)
        print("Producto eliminado satisfactoriamente.")
    else:
        print("No se encontró el ID.")
