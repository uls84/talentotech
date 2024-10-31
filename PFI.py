#Menu principal
def menu ():
    print("--------------------Menu--------------------")
    print("--------------------------------------------")    
    print("""1) Agregar producto al inventario. \n2) Mostrar productos del inventario. \n3) Actualizar cantidad de producto. \n4) Eliminar producto. \n5) Buscar producto. \n6) Reporte de bajo stock. \n7) Salir.""")
    print("--------------------------------------------")


# Validar opcion seleccionada del menu
def validar_opcion ():
    while True:
        try:
            seleccionar_opcion = int(input("Ingrese una de las opciones del 1 al 7: "))
            if seleccionar_opcion < 1 or  seleccionar_opcion > 7:
              print("Seleccionaste un número no válido, por favor ingrese una opción valida!")      
            else:
                return seleccionar_opcion
        except ValueError:    
            print("Entrada no valida por favor ingrese una nuevamente.")  


# Validar que la cantidad de un producto no sea cero
def validar_cantidad():
    cantidad_producto = -1
    
    while cantidad_producto <= 0:
         cantidad_producto = int(input("Ingrese la cantidad del producto: "))
         if cantidad_producto <= 0:
             print("La cantidad de stock es incorrecta, no puede ingresar una cantidad inferior a uno, vuelva a intentarlo!")
         else:
             return cantidad_producto


# Agregar productos a la lista para empujarlos a la lista   
def agregar_productos(inventario):
  id_producto = input("Ingrese el id del producto: ")
  nombre_producto = input("Ingrese el nombre del producto: ")
  descripcion = input("Ingrese una pequeña descripción del producto: ")
  cantidad = validar_cantidad()
  precio = float(input("Ingrese el precio del producto: "))
  categoria = input("Ingrese la categoría del producto: ")
  producto = [id_producto, nombre_producto, descripcion, cantidad, precio, categoria]
  inventario.append(producto)


# Mostrar productos
def mostrar_productos(inventario):
    print("")
    print("--------------------Productos--------------------")
    print("-------------------------------------------------")
    for producto in inventario:
        print(f"ID: \t{producto[0]} \nProducto: {producto[1]} \nDescripción: {producto[2]} \nCantidad: {producto[3]} \nPrecio: {producto[4]} \nCategoría: {producto[5]}")
        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
    print("-------------------------------------------------")
    print("")
    input("Presione enter para continuar...")
    print("")
    
# Selección del menu de opciónes         
def seleccion (opcion, inventario):               
    if opcion == 1:
        agregar_productos(inventario)     
    elif opcion == 2:
        mostrar_productos(inventario)
    elif opcion == 3:
        print()        
    elif opcion == 6:
        print("Llego a la opción 6!")


# Programa principal    
def programa ():
    inventario = []
    menu()
    opcion = validar_opcion()
    while opcion != 7:
        seleccion(opcion, inventario)
        menu()
        opcion = validar_opcion() 


programa()