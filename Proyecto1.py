"""
Proyecto
"""

"""
***************************************************************************
*COMPROBAR SI LA OPCIÓN DIGITADA ES VÁLIDA*
***************************************************************************
•Nombre: validar
•Entradas: opcion
•Salidas: True si la entráda es un String. False si la entrada no es un String. 
•Restricciones: La entrada debe ser un String.
"""
def validar(opcion):
    if (isinstance(opcion, str) and opcion != ""):
        return True
    else:
        return False
#-------------------------------------------------------------

print("Bienvenida/o a al sistema de reservacion de boletos. \n")

"""
****************************
*MENÚ PRINCIPAL*
****************************
•Nombre: sistemaDeReservación
•Entradas: no posee.
•Salidas: menú principal de la agenda de contactos.
•Restricciones: no posee.
"""


def sistemaDeReservacion():
    print("І-------------------------MENÚ PRINCIPAL-------------------------І\n")
    print("Debes elegir una de las siguientes opciones, mediante el numero: ")
    print("1. Opciones Administrativas.")
    print("2. Opcion para Usuario normal.")
    print("3. Salir.")

    eleccion = input("\nDigite una opción del menú principal: ")
    if (validar(eleccion)):
        if(eleccion == "1"):
            print("\n**********Bienvenid@ a la Administracion**********")
            return comprobarAcceso()
        elif(eleccion == "2"):
            print("Usuario")
            return usuarioNormal()
        elif(eleccion == "3"):
            print("***********************")
            print("*Saliendo del programa*")
            print("***********************")
            print("***UN GUSTO SERVIRLE***")
            print("***********************")
            
        else:
            print("La opcion digitada no es correcta, favor ingresar el numero de la opcion a elegir.")
            return sistemaDeReservación()
    else:
        print("La opción que digitaste no es válida. Por favor inteta otra vez.")
        return sistemaDeReservación()
#-------------------------------------------------------------------------
"""
Nombre: comprobarAcceso
Entrada: Usuario y Contraseña
Salida: Si el usuario y contraseña esta en el sistema, permite el acceso, de lo contrario lo denegará y permitirá registrarse
"""
def comprobarClave():
    Clave = open("Clave.txt")
    Clave1 = Clave.readlines()
    Clave.close()
    return Clave1
    
#-------------------------------------------------------------------
"""
Nombre: ComprobarEmpresa
Entrada; No posee
Salida: Retorna una funcion
Restricciones: No posee
"""
def comprabarEmpresas():
    Empresas = open("Empresas")
    Empresas1 = Empresas.readlines()
    Empresas.close()
    return Empresas1

#----------------------------------------------------------------------
"""
Nombre: permitirAcceso
Entrada: La calve de acceso
Salida: El retorno a la administracion
Restricciones: Que sea la calve registrada en el sistema
"""
def comprobarAcceso():
    print("\nPara acceder a la administracion, se requiere una clave de acceso")
    clave = input("Digite la clave de acceso: ")
    return comprobarAcceso_aux(clave)

def comprobarAcceso_aux(clave):
    Clave1 = comprobarClave()
    validarClave = validarC(clave, Clave1)
    if (validarClave):
        return administracion()
    else:
        return False

def validarC(clave, Clave1):
    if (("clave:"+clave) in Clave1):
        return administracion()
    else:
        print("CLAVE INCORRECTA, por favor intentar de nuevo")
        return comprobarAcceso()    


#-----------------------------------------------------------------------
def administracion():
    print("\n*******************************************")
    print("*BIENVENID@ A LAS OPCIONES ADMINISTRATIVAS*")
    print("*******************************************\n")
    print("----ELIJA UNA DE LAS SIGUIENTES OPCIONES----\n")
    print("11. Gestion de empresa")
    print("12. Gestion de transporte por empresa")
    print("13. Gestion de viaje")
    print("14. Consultar historial de reservaciones")
    print("15. Estadistica de viaje")
    print("16. Volver al menú principal")
    eleccion = input("\nDigite una nueva opcion del menú administrativo: ")
    if(validar(eleccion)):
        if(eleccion == "11"):
            return gestionEmpresas()
        elif(eleccion == "12"):
            return gestionTransporteEmpresa()
        elif(eleccion == "13"):
            return gestionViaje()
        elif(eleccion == "14"):
            return consultarHistorialReservaciones()
        elif(eleccion == "15"):
            return estadisticaViaje()
        elif(eleccion == "16"):
            print("--*Volviendo al menú principal*--")
            return sistemaDeReservacion()
        else:
            print("La opcion digitada no se encuentra. Por favor intenta otra vez")
            return administracion()
    else:
        print("La opcion digitada no se encuentra. Por favor intenta otra vez")
        return sistemaDeReserva()
        
#-------------------------------------------------------------------------------------
"""
Nombre: gestionEmpresa
Entrada:
Salida:
Restricciones:
"""
def gestionEmpresas():
    print("\n----------GESTIÓN DE EMPRESAS----------\n")
    print("----ELIJA UNA DE LAS SIGUIENTES OPCIONES----\n")
    print("111. Añadir una empresa")
    print("112. Eliminar una empresa")
    print("113. Modificar una empresa")
    print("114. Volver al menú de opciones administrativas")
    eleccion = input("\nDigite una nueva opcion del menú Gestión de Empresas: ")
    if(validar(eleccion)):
        if(eleccion == "111"):
            return añadirEmpresa()
        elif(eleccion == "112"):
            return eliminarEmpresa()
        elif(eleccion == "113"):
            return modificarEmpresa()
        elif(eleccion == "114"):
            print("-----Volviendo al menú administrativo-----")
            return administracion()
        else:
            print("La opcion digitada no se encuentra. Por favor intenta otra vez")
            return gestionEmpresas()
    else:
        print("La opcion digitada no se encuentra. Por favor intenta otra vez")
        return gestionEmpresas()
            
#-----------------------------------------------------------------------------------
def añadirEmpresa():
    print("\n-----AÑADIR EMPRESA-----\n")
    cedula = input("Digite su cedula juridica: ")
    nombre = input("Digite su nombre: ")
    ubicacion = input("Digite la direcccion del negocio: ")
    

    












sistemaDeReservacion()








