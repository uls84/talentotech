
#Menu principal

def menu ():
    print("--------------------Menu--------------------")
    print("--------------------------------------------")    
    print("""1) Agregar producto. \n2) Mostrar productos. \n3) Actualizar cantidad de producto. \n4) Eliminar producto. \n5) Buscar producto. \n6) Reporte de bajo stock. \n7) Salir.""")
    print("--------------------------------------------")

# Funcion para instertar productos en la lista 
def insertar (id_producto, nombre_producto, descripcion, cantidad, precio, categoria, producto):
    producto.append(id_producto)
    producto.append(nombre_producto)
    producto.append(descripcion)
    producto.append(cantidad)
    producto.append(precio)
    producto.append(categoria)    
    print(producto)

# Agregar productos al array para empujarlos a la lista   
def agregar_productos(inventario):
    #producto = []
    id_producto = int(input("Ingrese el id del producto: ")) #Ingresar algo para que no puedan romper el codigo ingresando caracteres
    nombre_producto = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una pequeña descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")
    insertar(id_producto, nombre_producto, descripcion, cantidad, precio, categoria, producto)
    producto = [id_producto, nombre_producto, descripcion, cantidad, precio, categoria, producto]
    
    inventario.append(producto)
    #Borrar éstas dos lineas finales al terminar y buscar todos los print que no sean parte del programa
    print(inventario)
    print("Inserción de artículos exitoso!") 
    
# Validar opcion seleccionada del menu
def validar_opcion (opcion):
    while True:
        try:
            if opcion < 1 or  opcion > 7:
              print("Seleccionaste un número no válido, por favor ingrese una opción valida!")      
            else:
                return 
            opcion = int(input("Ingrese una de las opciones del 1 al 7: "))    
        except ValueError:    
            print("Entrada no valida por favor ingrese una nuevamente.")  
            opcion = int(input("Ingrese una de las opciones del 1 al 7: "))
     
def mostrar_productos(inventario):
    print("********************Productos********************")
    for prod in inventario:
        print(f"ID: \t{prod[0]} \nProducto: {prod[1]} \nDescripción: {prod[2]} \nCantidad: {prod[3]} \nPrecio: {prod[4]} \nCategoría: {prod[5]}")
        print("*************************************************")
    print("_________________________________________________")
    print("")
             
# Selección del menu de opciónes         
def seleccion (opcion, inventario):               
    if opcion == 1:
        agregar_productos(inventario)     
    elif opcion == 2:
        mostrar_productos(inventario)
    elif opcion == 3:
        print()
    elif opcion == 4:
        print()
    elif opcion == 5:
        print()                
    elif opcion == 6:
        print("Llego a la opción 6!")

    
def programa ():
    
    # Lista global
    inventario = []

    menu()
    opcion = int(input("Ingrese una de las opciones del 1 al 7: "))
    validar_opcion(opcion)
    while opcion != 7:
        seleccion(opcion, inventario)
        menu()
        opcion = int(input("Ingrese una de las opciones del 1 al 7: "))
        validar_opcion(opcion) 


programa()