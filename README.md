# Sistema de Control de Inventario

Este proyecto es una aplicación de consola desarrollada en Python diseñada para la administración eficiente de productos. Permite registrar, listar, buscar, editar y eliminar artículos del inventario, asegurando un control preciso del stock y los precios.

## Integrantes
- Crismar Hernández V-28767682
- Migfrannys Martinez V-28735102
- Luis Rivero V-28731230

## Descripción
El sistema facilita el control de existencias mediante el registro de productos con detalles específicos: ID (Código numérico), Nombre, Categoría, Precio y Stock. Para garantizar que la información no se pierda al cerrar el programa, los datos se almacenan y recuperan automáticamente en archivos de formato JSON.

## Requisitos Técnicos
- Python 3.x
- No requiere la instalación de librerías externas (utiliza módulos nativos como json y os).

## Instrucciones para ejecutar el programa
1. Descargar o clonar los archivos del proyecto manteniendo la estructura de carpetas.
2. Abrir una terminal o consola (o Pydroid 3 en Android) en el directorio raíz del proyecto.
3. Ejecutar el siguiente comando: python main.py

## Estructura general del sistema
```
.
├── main.py              # Punto de entrada y menú principal
├── data/                # Carpeta generada automáticamente para los datos
│   └── inventario.json  # Archivo de persistencia en formato JSON
├── modules/             # Lógica dividida por funcionalidad
│   ├── operaciones.py   # Funciones CRUD (Registrar, Listar, Editar, Eliminar)
│   └── validaciones.py  # Control de errores en la entrada de datos (int, float, texto)
└── utils/               # Herramientas de soporte
    └── archivos.py      # Gestión de lectura y escritura en disco
```
# Estándares del proyecto

Este proyecto cumple con los fundamentos de programación requeridos por la asignatura de Lenguaje de Programación III de la UNEFA:

1. Variables y Tipos de Datos: Uso de cadenas, enteros y flotantes para representar productos.

2. Estructuras de Control: Implementación de ciclos while True para el menú y condicionales if-elif-else para la toma de decisiones.

3. Modularidad: División del código en paquetes (modules, utils) para mejorar la mantenibilidad.

4. Manejo de Colecciones: Uso de listas de diccionarios para manipular los productos en memoria.

5. Persistencia de Datos: Implementación de serialización y deserialización con el módulo json.

6. Validaciones Robustas: Uso de bloques try-except para evitar que el programa se cierre por entradas de usuario incorrectas.

7. Interfaz Limpia: Limpieza automática de pantalla entre operaciones para una mejor experiencia de usuario.
