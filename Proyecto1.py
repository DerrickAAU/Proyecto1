"""
Proyecto
"""

"""
Nombre: Convertir la lista en string
"""
def convertirstr(lista):
    if isinstance(lista, list):
        string = ""
        for indice in lista:
            string += indice
        return string
    else:
        print("Error: no se puede convertir a String, porque, el tipo de dato de entrada, no es una lista")
        
#----------------------------------------------------------
        
"""
Nombre: Cantidad de indices
"""
def cantidadDeindices(convertirstr):
    if convertirstr == "" or convertirstr==[]:
        return 0
    else:
        return 1+ cantidadDeindices(convertirstr[1:])

#----------------------------------------------------------
    
"""
Nombre: Verificar si el indice se encuentra
"""

def seEncuentra(buscar,convertirstr):
    indicesBuscar= cantidadDeindices(buscar)
    if isinstance(convertirstr,list):
        return seEncuentraA(buscar,indicesBuscar,convertirstr,0)
    else:
        return seEncuentraEnstring(buscar,convertirstr,indicesBuscar)

def seEncuentraA(buscar,indicesBuscar,lista,cont):
    if lista == []:
        return False
    else:
        if seEncuentraEnstring(buscar,lista[0],indicesBuscar):
            return True
        else:
            return seEncuentraA(buscar,indicesBuscar,lista[1:],cont +1)

def seEncuentraEnstring(buscar,cadena,indicesBuscar):
    if cadena =="":
        return False
    else:
        if buscar== cadena [0: indicesBuscar]:
            return True
        else:
            return seEncuentraEnstring(buscar,cadena[1:], indicesBuscar)

"""
Nombre: Es númerico
Entrada: cadena
salida: True si todos los caracteres de la entrada corresponde a númerico
"""
def esNumerico(cadena):
    if (cadena ==""):
        return True
    else:
        primerCaracter=cadena[0]
        if(primerCaracter =="0" or primerCaracter =="1" or primerCaracter=="2" or primerCaracter =="3" or primerCaracter =="4"):
            return True and esNumerico(cadena=cadena[1:])
        elif(primerCaracter == "5" or primerCaracter == "6" or primerCaracter == "7" or primerCaracter == "8" or primerCaracter == "9" or primerCaracter =="10"):
            return True and esNumerico(cadena=cadena[1:])
        else:
            return False
        
#------------------------------------------------------------------------------
def eliminarInformacion(listaEmpresas, indice, cont):
    if cont==4:
        return convertirstr(listaEmpresas)
    else:
        print(listaEmpresas[indice].strip())
        listaEmpresas.pop(indice)
        return eliminarInformacion(listaEmpresas, indice, cont + 1)

#--------------------------------------------------------------------------------
def mostrarEmpresas(listaEmpresas, indice, cont):
    if cont > 2:
        print("-------------------------------------")
    else:
        if(cont == 0):
            print("Cédula juridica: " + listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        elif(cont == 1):
            print("Nombre de la empresa: ", listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        else:
            print("Ubicación de la empresa: ", listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)


#---------------------------------------------------------------------------------
def convertir_a_string(lista):
    if isinstance(lista, list):
        string = ""
        for indice in lista:  # Se leen las lineas del archivo y guarda en un una variable
            string += indice
        return string
    else:
        print("Error: no se puede convertir a String, porque, el tipo de dato de entrada, no es una lista")


#---------------------------------------------------------------------------------
"""
Nombre: Validar cédula 
"""
def cedValidar( cedula,Empresas):
    if (seEncuentra(cedula + "\n", Empresas)):
        return False
    else:
        if(cantidadDeindices(cedula) == 10 and isinstance(int(cedula), int)):
            return True
        else:
            print("\nERROR: La cédula no contiene 10 dígitos exactos, vuelva intentar")
            return gestionEmpresas()
        
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
Entrada: La clave de acceso
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
    if(validarClave):
        return administracion()
    else:
        return False

def validarC(clave, Clave1):
    if(seEncuentra(clave,Clave1)):
        return "Clave correcta"
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
Nombre: gestionEmpresas
Entrada: no posee
Salida: opciones distintas a eligir
Restricciones: no posee
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
            print("\n-----AÑADIR EMPRESA-----\n")
            cedula = input("Digite su cedula juridica: ")
            nombre = input("Digite el nombre de la empresa: ")
            ubicacion = input("Digite la ubicacion de la empresa: ")
            return añadirEmpresa(cedula, nombre, ubicacion)
        elif(eleccion == "112"):
            cedula = input("Digite el numero de cédula de la empresa a eliminar: ")
            if cedula != "":
                return borrarEmpresa(cedula)
            else:
                print("Debe añadir una cédula, esta opción no puede estar vacía")
                return gestionEmpresas()
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
"""
Nombre: añadirEmpresa
Entrada: no posee
Salida: Que se ha añadido exitosamente la empresa
Restricciones: la cedula debe contener diez digitos
"""
def añadirEmpresa(cedula, nombre, ubicacion):
    Empresas=open("Empresas.txt")
    Empresas1=Empresas.readlines()
    validarCedula= cedValidar(cedula,Empresas1)
    if(validarCedula):
        Empresas=open("Empresas.txt","a")
        Empresas.write(cedula + "\n")
        Empresas.write(nombre + "\n")
        Empresas.write(ubicacion + "\n")
        Empresas.write("--------------------------------------" + "\n")
        Empresas.close()
        print("\n---NUEVA EMPRESA AGREGADA CORRECTAMENTE---\n")
        return gestionEmpresas()
    else:
        print("\nEsta cedula ya está registrada, intente de nuevo")
        return gestionEmpresas()

    
#---------------------------------------------------------------------------
def borrarEmpresa(cedula):
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    if(seEncuentra(cedula+"\n",listaEmpresas)):
        print("-----------BORRANDO EMPRESA-----------\n")
        cedula=str(cedula)
        indice = listaEmpresas.index(cedula+"\n")
        cedula = eliminarInformacion(listaEmpresas, indice, 0)
        Empresas.close()
        Empresas = open("Empresas.txt", "w")
        Empresas.write(cedula)
        Empresas.close()
        print("\nEmpresa borrada exitosamente")
        return gestionEmpresas()
    else:
        print("\nNo hay ninguna Empresa registrada con la cédula ", cedula)
        Empresas.close()
        return gestionEmpresas()

    





sistemaDeReservacion()








