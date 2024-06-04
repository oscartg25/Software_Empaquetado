
registro = []


def menu():
    while True:
        print("Bienvenido al menú:")
        print("1. Registro de usuario")
        print("2. Salir")

        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            submenu_registro()
        elif opcion == "2":
            print("¡Gracias por usar nuestro sistema! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
def submenu_registro():
    while True:
        print("\nRegistro de Usuario:")
        print("1. Verificar usuario")
        print("2. Registrar nuevo usuario")
        print("3. Eliminar usuario")
        print("4. Menu empaquetado")
        print("5. Volver al menú principal")

        opcion_registro = input("Por favor, seleccione una opción: ")

        if opcion_registro == "1":
            verificar_usuario()
        elif opcion_registro == "2":
            registrar_usuario()
        elif opcion_registro == "3":
            eliminar_usuario()
        elif opcion_registro == "4":
            menu_empaquetado()
        elif opcion_registro == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def verificar_usuario():
    cedula = input("Ingrese la cédula del usuario a verificar: ")
    usuario = next((user for user in registro if user["cedula"] == cedula),
                   None)
    if usuario:
        print(f"El usuario con cédula {cedula} está registrado como {usuario['nombre']}." )
    else:
        print(f"El usuario con cédula {cedula} no está registrado.")

def registrar_usuario():
    cedula = input("Ingrese la cédula del nuevo usuario: ")
    nombre = input("Ingrese el nombre del nuevo usuario: ")
    usuario = next((user for user in registro if user["cedula"] == cedula),
                   None)
    if usuario:
        print(
            f"El usuario con cédula {cedula} ya está registrado como {usuario['nombre']}."
        )
    else:
        registro.append({"cedula": cedula, "nombre": nombre})
        print(f"Usuario {nombre} con cédula {cedula} registrado exitosamente.")

def eliminar_usuario():
    cedula = input("Ingrese la cédula del usuario a eliminar: ")
    usuario = next((user for user in registro if user["cedula"] == cedula),None)
    if usuario:
        registro.pop(usuario)
        print(f"Usuario con cédula {cedula} eliminado exitosamente.")
    else:
        print(f"El usuario con cédula {cedula} no está registrado.")

def menu_empaquetado():
        print("\nAyudanos por favor ingresando el valor del material que tienes a tu disposición para la elaboración del empaquetado, para brindarte una mayor exactitud, brindanos el valor total por 70X100cm del material, es decir, por el pliego completo")
        vmaterial=float(input("Ingresa el valor del material: $"))
        
        while True:
            opc=int(input("\nCómo te gustaría te ayudemos el día de hoy?: \n 1. Ayuda con tu emapaquetado personalizado? \n 2. Quieres conocer nuestras opciones? \n 3. Volver \n "))
            if opc==1:
                print("Perfecto, ahora necesitaremos tu ayuda, por favor compartenos la siguiente información:\n")
                largo=float(input("En cm por favor ingresa el largo de tu producto: "))
                alto=float(input("En cm por favor ingresa el alto de tu producto: "))
                ancho=float(input("En cm por favor ingresa el ancho de tu producto: "))
                tproducto=largo*alto*ancho
                tempaquetado=tproducto*1.2
                print("Muy bien! vemos que tu producto tiene una dimensión de ",tproducto, " centímeros cuadrados, muy buen tamaño! Es por esto que te recomendamos tu empaquetado sea ",tempaquetado)
                cant=float(7000/tempaquetado)
                valoremp=float(vmaterial/cant)
                print("Wao! te salen alrededor de ",cant," piezas de empaquetado")
                print("Cada pieza para tu empaquetado te sale por $",valoremp)
                vunip=float(input("Ayudanos a darte la mejor recomendación, por favor ingresa tu costo unitario de fabricación para el producto que deseas comercializar \n"))
                if vunip<=(valoremp*0.4):
                     print("El empaquetado es viable para este tipo de producto")
                else: 
                    print("Te recomendamos utilizar otro tipo de empaquetado, pues el costo de empaquetado está algo elevado para tu producto, lo que te podría causar un desequilibrio al momento de plantear tu precio final al consumidor")
                break
            
            elif opc==2:
                print("A continuación queremos que conozcas los tamaños estándares, estos tamaños son los mayormente comercializados: \n")
                print("1. Empaquetado 5X5X5cm")
                print("2. Empaquetado 7X7X7cm")
                print("3. Empaquetado 9X9X9cm")
                print("4. Salir")
                selecopc=int(input("Selecciona por favor la opción que prefieras: "))
                if selecopc==1:
                    print("Has seleccionado el empaquetado 5x5x5cm")
                    cant=float(7000/125)
                    valoremp=float(vmaterial/cant)
                    print("Wao! te salen alrededor de ",cant," piezas de empaquetado")
                    print("Cada pieza para tu empaquetado te sale por $",valoremp)
                elif selecopc==2:
                    print("Has seleccionado el empaquetado 7x7x7cm")
                    cant=float(7000/343)
                    valoremp=float(vmaterial/cant)
                    print("Wao! te salen alrededor de ",cant," piezas de empaquetado")
                    print("Cada pieza para tu empaquetado te sale por $",valoremp)
                elif selecopc==3:
                    print("Has seleccionado el empaquetado 9x9x9cm")
                    cant=float(7000/729)
                    valoremp=float(vmaterial/cant)
                    print("Wao! te salen alrededor de ",cant," piezas de empaquetado")
                    print("Cada pieza para tu empaquetado te sale por $",valoremp)
                elif selecopc==4:
                    break    
                else:
                    print("Elección inexistente, si los empaquetados existentes no son de tu agrado, por favor dirigete a la opción de personalizados")
                vunip=float(input("Ayudanos a darte la mejor recomendación, por favor ingresa tu costo unitario de fabricación para el producto que deseas comercializar \n"))
                if vunip<=(valoremp*0.4):
                     print("El empaquetado es viable para este tipo de producto")
                else: 
                    print("Te recomendamos utilizar otro tipo de empaquetado, pues el costo de empaquetado está algo elevado para tu producto, lo que te podría causar un desequilibrio al momento de plantear tu precio final al consumidor")
            elif opc == 3:
                break
            else:
                print("Ingresa una opción válida") 
            
menu ()

