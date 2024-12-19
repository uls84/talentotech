import sqlite3
#from colorama import init, Fore, Style, bajo_stock

#init(autoreset=True)



def mostrar_menu ():
    '''
    Función para invocar el menú
    Args:
        Ninguno
    '''
    
    print("--------------------Menu--------------------")
    print(" ")    
    print("""1) Agregar producto al inventario. \n2) Mostrar productos del inventario. \n3) Actualizar stock de un producto. \n4) Eliminar producto. \n5) Buscar producto. \n6) Reporte de bajo stock. \n7) Salir.""")
    print(" ")
    
def validar_opcion ():
    '''
    Función para validar la opción seleccionada en el menú'
    Args:
        Ninguno
    '''
    while True:
        try:
            seleccionar_opcion = int(input("Ingrese una de las opciones del 1 al 7: "))
            if seleccionar_opcion < 1 or  seleccionar_opcion > 7:
              print("Seleccionaste un número no válido, por favor ingrese una opción valida!")      
            else:
                return seleccionar_opcion
        except ValueError:    
            print("Entrada no valida por favor ingrese una nuevamente.")  
            
def validar_cantidad():
    '''
    Función para validar que la cantidad de un producto no sea cero
    Args:
        Ninguno
    '''
    cantidad_producto = -1
    
    while cantidad_producto <= 0:
         cantidad_producto = int(input("Ingrese la cantidad del producto: "))
         if cantidad_producto <= 0:
             print("La cantidad de stock es incorrecta, no puede ingresar una cantidad inferior a uno, vuelva a intentarlo!")
         else:
             return cantidad_producto

def validar_precio():
    '''
    Función para validar que el precio ingresado no sea cero ni negativo
    Args:
        Ninguno
    '''
    precio_producto = -1
    
    while precio_producto <= 0:
         precio_producto = float(input("Ingrese el precio del producto: "))
         if precio_producto <= 0:
             print("El precio del producto no puede ser inferior a uno, vuelva a ingresar un precio valido!")
         else:
             return precio_producto

def registrar_productos():
    '''
    Función para agregar los productos a la base de datos
    Args:
        inventario: base de datos del inventario.
    '''
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = '''
        INSERT INTO inventario (nombre,descripcion,cantidad,precio,categoria)
        VALUES (?,?,?,?,?)
    '''
    
    nombre_producto = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una pequeña descripción del producto: ")
    cantidad = validar_cantidad()
    precio = validar_precio()
    categoria = input("Ingrese la categoría del producto: ")
    params = (nombre_producto, descripcion, cantidad, precio, categoria)
    print("El producto se ha registrado correctamente!")
    cursor.execute(query,params)
    conexion.commit()
    conexion.close()

def mostrar_productos():
    '''
    Función que muestra todos los productos del inventario
    Args:
        Ninguno
    '''
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = '''
        SELECT * FROM inventario
    '''
    cursor.execute(query)
    productos = cursor.fetchall()
    if not productos:
        print("No hay productos en el inventario.")
    else:
        encabezado = f"{'ID':<3} |{'Nombre':<20} |{'Descripcion':<40} |{'Stock':<5} |{'Precio':<10} |{'Categoria':<20}"
        separador = "-" * len(encabezado)
        print("Productos regristrados: ")
        print(encabezado)
        print(separador)
        for producto in productos:
            print(f"{producto[0]:<3} |{producto[1]:<20} |{producto[2]:<40} |{producto[3]:<5} |{producto[4]:<10} |{producto[5]:<20}")
        print("")
        input("Presione enter para continuar...")
        print(f"\n""")    
    conexion.close()

def eliminar_producto():
    '''
    Función que elimina un producto del inventario
    Args:
        Ninguno
    '''
    
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = '''
        DELETE FROM inventario
        WHERE id = ?
    '''
    id_producto = int(input("Ingrese el id del producto a borrar: "))
    producto = buscar_producto(id_producto)
    params = (producto,)
    if producto:
        cursor.execute(query,params)
        conexion.commit()
        conexion.close()
        print(f"El producto con id '{id_producto}' ha sido elimiado el inventario!")
        print("")
        input("Presione enter para continuar...")
        print(f"\n""")  
    else:    
        print(f"El producto con código '{id_producto}' no se encuentra en el inventario.")

def actualizar_stock():
    '''
    Función que actualiza el stock de un producto
    Args:
        Ninguno
    '''
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = '''
        UPDATE inventario
        SET cantidad = ?
        WHERE id = ?
    '''
    id_modificar = int(input("Ingrese el numero de id que desee modificar: "))
    cantidad = validar_cantidad()
    params = (cantidad,id_modificar)
    cursor.execute(query,params)
    conexion.commit()
    conexion.close()
    
def buscar_producto(id_producto):
    '''
    Función que busca un producto dentro del inventario
    Args:
        Id_producto: 
    '''
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = '''
        SELECT * FROM inventario
        WHERE id = ?
    '''
    params = (id_producto,)
    cursor.execute(query,params)
    producto = cursor.fetchone()
    if producto:
        print("")
        print(f"{producto[0]:<3} |{producto[1]:<20} |{producto[2]:<40} |{producto[3]:<5} |{producto[4]:<10} |{producto[5]:<20}")
        conexion.close()
        print("")
        input("Presione enter para continuar...")
    else:
        print("Producto no encontrado.")    
        print("")
        input("Presione enter para continuar...")  

def reporte_bajo_stock():
    '''
    Función que le pide al cliente un número de stock mínimo para buscar coincidencias en el inventario
    Args:
        Ninguno
    '''
    
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = '''
        SELECT nombre, cantidad FROM inventario
        WHERE cantidad <= ?
    '''
    stock_limite = int(input("Ingrese un número mínimo de stock: "))
    params = (stock_limite,)
    cursor.execute(query,params)
    bajo_stock = cursor.fetchall()
    if not bajo_stock:
        print("No hay productos con bajo stock.")
    else:    
        encabezado = f"{'Producto':<30} | {'Stock':<10}"
        separador = "-" * len(encabezado)
        print('\nListado de productos con bajo stock: ')
        print(encabezado)
        print(separador)
        for stock in bajo_stock:
            print(f"{stock[0]:<30} | {stock[1]:<10}")
    conexion.close()
    print("")
    input("Presione enter para continuar...")
    print(f"\n""")  
            
def seleccion (opcion):
    '''
    Función para la selección de opciones del menú.
    Args:
        opcion: recibe la opción a seleccionar del menu.
        inventario: base de datos.
    '''      

    if opcion == 1:
        registrar_productos()     
    elif opcion == 2:
        mostrar_productos()
    elif opcion == 3:
        actualizar_stock()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        id_producto = int(input("Ingrese el id del producto a buscar: "))
        buscar_producto(id_producto)    
    elif opcion == 6:
        reporte_bajo_stock()
        
def crear_tabla():
    '''
    Función que se ejecuta para iniciar la base de datos por primera vez
    '''
    
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS inventario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL CHECK(typeof(cantidad) = 'integer'),
        precio REAL NOT NULL,
        categoria TEXT NOT NULL
    )
    '''
    cursor.execute(query,)
    conexion.commit()
    conexion.close()
    
def programa():
    '''
    Función principal que ejecuta el bucle del menu
    Args:
        inventario: base de datos.
    '''    
    crear_tabla()
    while True:
        mostrar_menu()
        opcion = validar_opcion()
        if opcion == 7:
            print("Gracias por utilizar el sistema!")
            break
        seleccion(opcion)


programa()