# =============================================================================
# PROGRAMA: Procesamiento de datos con estructuras de datos en Python
# MÓDULO:   Python optativo — UD04
# AUTOR:    Esteban Ospina
# FECHA:    Marzo 2026
# =============================================================================
# DESCRIPCIÓN:
#   Demuestra el uso de las cuatro estructuras de datos principales de Python:
#     1. Cadenas (str)       → operaciones con nombre del usuario
#     2. Listas (list)       → gestión de catálogo de productos
#     3. Tuplas (tuple)      → códigos de productos (datos inmutables)
#     4. Diccionarios (dict) → productos con sus precios
# =============================================================================


def separador(titulo):
    """Imprime un separador visual con un título para mejorar la legibilidad."""
    print("\n" + "=" * 55)
    print(f"  {titulo}")
    print("=" * 55)


# =============================================================================
# BLOQUE 1 — CADENAS DE CARACTERES (str)
# Las cadenas son secuencias inmutables de caracteres.
# Python ofrece numerosos métodos integrados para manipularlas.
# =============================================================================


def ejercicio_cadenas():
    """
    Solicita el nombre completo del usuario y realiza tres operaciones:
      - Formateo en título
      - Conteo de vocales
      - Inversión del nombre
    """
    separador("BLOQUE 1 — CADENAS DE CARACTERES")

    # --- Entrada de datos ------------------------------------------------
    nombre_completo = input("\n  Introduce tu nombre completo: ").strip()

    # --- Operación 1: Formato título ------------------------------------
    # .title() convierte la primera letra de cada palabra a mayúscula
    # y el resto a minúscula. Ideal para nombres propios.
    nombre_titulo = nombre_completo.title()
    print(f"\n  Nombre en formato título: {nombre_titulo}")

    # --- Operación 2: Contar vocales ------------------------------------
    # Definimos las vocales (con y sin tilde) como una cadena de referencia
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

    # Usamos una comprensión de lista para filtrar solo las vocales del nombre
    # y len() para contar cuántas hay
    lista_vocales_encontradas = [letra for letra in nombre_completo if letra in vocales]
    cantidad_vocales = len(lista_vocales_encontradas)

    print(f"  Vocales encontradas: {lista_vocales_encontradas}")
    print(f"  Número total de vocales: {cantidad_vocales}")

    # --- Operación 3: Invertir el nombre --------------------------------
    # El slicing [::-1] recorre la cadena de derecha a izquierda
    nombre_invertido = nombre_completo[::-1]
    print(f"  Nombre invertido: {nombre_invertido}")

    return nombre_titulo


# =============================================================================
# BLOQUE 2 — LISTAS (list)
# Las listas son colecciones ordenadas y mutables. Permiten duplicados.
# Se pueden modificar después de su creación: añadir, eliminar, ordenar...
# =============================================================================


def ejercicio_listas():
    """
    Trabaja con una lista de productos:
      - Muestra la lista ordenada
      - Añade y elimina elementos
      - Filtra por letra inicial
    """
    separador("BLOQUE 2 — LISTAS")

    # --- Definición de la lista inicial --------------------------------
    # Lista mutable con 5 nombres de productos tecnológicos
    productos = [
        "Monitor 4K",
        "Auriculares Bluetooth",
        "Teclado Mecánico",
        "Alfombrilla XXL",
        "Cable HDMI",
    ]

    print(f"\n  Lista original:  {productos}")

    # --- Operación 1: Ordenar alfabéticamente --------------------------
    # .sort() ordena la lista en su lugar (modifica el original)
    # sorted() devolvería una copia ordenada sin modificar la original
    productos.sort()
    print(f"  Lista ordenada:  {productos}")

    # --- Operación 2a: Agregar un nuevo producto -----------------------
    # .append() añade el elemento al final de la lista
    nuevo_producto = "Webcam HD"
    productos.append(nuevo_producto)
    print(f"\n  Tras añadir '{nuevo_producto}': {productos}")

    # --- Operación 2b: Eliminar el tercer elemento (índice 2) ----------
    # .pop(índice) elimina el elemento en la posición indicada y lo retorna
    # Los índices en Python empiezan en 0: índice 2 = tercer elemento
    producto_eliminado = productos.pop(2)
    print(f"  Eliminado (índice 2): '{producto_eliminado}'")
    print(f"  Lista resultante: {productos}")

    # --- Operación 3: Filtrar productos que empiezan por "A" -----------
    # Comprensión de lista con .startswith() para filtrar por letra inicial
    # .startswith() es sensible a mayúsculas, por eso verificamos con "A"
    productos_con_a = [p for p in productos if p.startswith("A")]
    print(f"\n  Productos que empiezan por 'A': {productos_con_a}")

    return productos


# =============================================================================
# BLOQUE 3 — TUPLAS (tuple)
# Las tuplas son colecciones ordenadas e INMUTABLES.
# Se usan para datos que no deben cambiar: coordenadas, códigos, constantes...
# =============================================================================


def ejercicio_tuplas():
    """
    Trabaja con una tupla de códigos de productos:
      - Verifica si un código existe
      - Muestra un rango de elementos con slicing
    """
    separador("BLOQUE 3 — TUPLAS")

    # --- Definición de la tupla de códigos ----------------------------
    # Usamos paréntesis (aunque son opcionales, mejoran la legibilidad)
    # Al ser inmutable, los códigos no pueden modificarse accidentalmente
    codigos_productos = ("P001", "P002", "P003", "P004", "P005")

    print(f"\n  Códigos disponibles: {codigos_productos}")
    print(f"  Tipo de dato: {type(codigos_productos)}")  # <class 'tuple'>

    # --- Operación 1: Verificar si un código existe -------------------
    # El operador 'in' comprueba la pertenencia en cualquier secuencia
    codigo_buscado = (
        input("\n  Introduce un código a buscar (ej. P003): ").strip().upper()
    )

    if codigo_buscado in codigos_productos:
        # .index() devuelve la posición del primer elemento que coincide
        posicion = codigos_productos.index(codigo_buscado)
        print(f"  ✅ Código '{codigo_buscado}' encontrado en la posición {posicion}.")
    else:
        print(f"  ❌ Código '{codigo_buscado}' NO existe en el catálogo.")

    # --- Operación 2: Slicing del segundo al cuarto elemento ----------
    # codigos[1:4] → índice 1 (inclusive) hasta índice 4 (exclusivo)
    # Resultado: elementos en posiciones 1, 2 y 3 (P002, P003, P004)
    codigos_segundo_a_cuarto = codigos_productos[1:4]
    print(f"\n  Códigos del 2.º al 4.º: {codigos_segundo_a_cuarto}")

    return codigos_productos


# =============================================================================
# BLOQUE 4 — DICCIONARIOS (dict)
# Los diccionarios almacenan pares clave:valor.
# Las claves son únicas; los valores pueden ser de cualquier tipo.
# Son ideales para representar objetos con propiedades (producto → precio).
# =============================================================================


def ejercicio_diccionarios():
    """
    Trabaja con un diccionario de productos y precios:
      - Consulta el precio de un producto
      - Añade un nuevo producto
      - Elimina un producto existente
    """
    separador("BLOQUE 4 — DICCIONARIOS")

    # --- Definición del diccionario inicial ---------------------------
    # Clave: nombre del producto (str) | Valor: precio en euros (float)
    catalogo_precios = {
        "Monitor 4K": 349.99,
        "Auriculares Bluetooth": 89.95,
        "Teclado Mecánico": 129.00,
        "Alfombrilla XXL": 24.50,
        "Cable HDMI": 9.99,
    }

    print("\n  Catálogo de productos y precios:")
    # Iteramos sobre los pares clave-valor con .items()
    for nombre, precio in catalogo_precios.items():
        print(f"    · {nombre:<25} {precio:>8.2f} €")

    # --- Operación 1: Consultar precio de un producto ----------------
    # .get(clave, valor_por_defecto) es más seguro que acceso directo []
    # porque no lanza KeyError si la clave no existe
    producto_buscado = (
        input("\n  ¿De qué producto quieres saber el precio? ").strip().title()
    )

    precio_encontrado = catalogo_precios.get(producto_buscado)
    if precio_encontrado is not None:
        print(f"  Precio de '{producto_buscado}': {precio_encontrado:.2f} €")
    else:
        print(f"  Producto '{producto_buscado}' no encontrado en el catálogo.")

    # --- Operación 2: Agregar un nuevo producto -----------------------
    # Asignar a una clave nueva crea el par automáticamente
    nuevo_nombre = "Webcam HD"
    nuevo_precio = 79.99
    catalogo_precios[nuevo_nombre] = nuevo_precio
    print(f"\n  Añadido: '{nuevo_nombre}' → {nuevo_precio:.2f} €")

    # --- Operación 3: Eliminar un producto existente -----------------
    # del elimina la clave (y su valor) del diccionario
    # También puede usarse .pop(clave) si queremos guardar el valor eliminado
    producto_a_eliminar = "Cable HDMI"
    del catalogo_precios[producto_a_eliminar]
    print(f"  Eliminado: '{producto_a_eliminar}'")

    # --- Mostrar el catálogo actualizado -----------------------------
    print("\n  Catálogo actualizado:")
    for nombre, precio in catalogo_precios.items():
        print(f"    · {nombre:<25} {precio:>8.2f} €")

    return catalogo_precios


# =============================================================================
# BLOQUE PRINCIPAL
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("   GESTIÓN DE CLIENTES Y PRODUCTOS — UD04")
    print("=" * 55)
    print("  Estructuras de datos: str · list · tuple · dict")

    # Ejecutar los cuatro bloques en orden
    nombre_usuario = ejercicio_cadenas()
    lista = ejercicio_listas()
    tupla = ejercicio_tuplas()
    catalogo = ejercicio_diccionarios()

    # Resumen final
    separador("RESUMEN")
    print(f"\n  Usuario:        {nombre_usuario}")
    print(f"  Productos:      {len(lista)} en lista")
    print(f"  Códigos:        {len(tupla)} en tupla")
    print(f"  Catálogo:       {len(catalogo)} productos con precio")
    print("\n  ¡Programa completado con éxito!")
    print("=" * 55)
