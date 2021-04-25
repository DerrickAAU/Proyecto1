"""
Proyecto
"""

"""
Nombre: Convertir la lista en string
Entrada: lista
Parametros: lista
Salida: un string
Restricciones: La entrada debe ser una lista
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
Entrada: sin estrada
Parametros: convertirstr
Salida: sin salida
Restricciones: sin restriccion
"""
def cantidadDeindices(convertirstr):
    if convertirstr == "" or convertirstr==[]:
        return 0
    else:
        return 1+ cantidadDeindices(convertirstr[1:])

#----------------------------------------------------------
    
"""
Nombre: seEncuentra
Entrada: lo que se va buscar y los dattos en str
Parametros: buscar,covertirstr
Salida: True o False
Restricciones: sin restricciones
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
Entrada: una cadena
Parametros: cadena
Salida: True o False
Restricciones: sin restricciones
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
"""
Nombre: eliminarInformacion
Entrada: una lista a eliminar
Parametros: listaEmpresas, indice, cont
Salida: sin salida, solo elimina la informacion
Restricciones: sin restricciones
"""
def eliminarInformacion(listaEmpresas, indice, cont):
    if cont==4:
        return convertirstr(listaEmpresas)
    else:
        print(listaEmpresas[indice].strip())
        listaEmpresas.pop(indice)
        return eliminarInformacion(listaEmpresas, indice, cont + 1)

#--------------------------------------------------------------------------------
"""
Nombre: mostrarEmpresas
Entrada: datos a mostrar
Parameteros: listaEmpresas, indice, cont
Salida: muestra en pantalla los datos
Restricciones: sin restricciones
"""
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
"""
Nombre: convertir_a_string
Entrada: una lista
Parametro: lista
Salida: datos string
Restricciones: sin restricciones
"""
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
Nombre: cedValidar
Entrada: cedula a validar
Parametros: cedula,Empresas
Salida: True o False
Restricciones: la cedula debe contener 10 digitos
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
*******************************************
*COMPROBAR SI LA OPCIÓN DIGITADA ES VÁLIDA*
*******************************************
Nombre: validar
Entradas: la opcion
Parametros: opcion
Salidas: True si la entráda es un String. False si la entrada no es un String. 
Restricciones: La entrada debe ser un String.
"""
def validar(opcion):
    if (isinstance(opcion, str) and opcion != ""):
        return True
    else:
        return False
#-------------------------------------------------------------

print("Bienvenida/o a al sistema de reservacion de boletos. \n")

"""
****************
*MENÚ PRINCIPAL*
****************
Nombre: sistemaDeReservación
Entradas: no posee.
Parametros: no posee
Salidas: menú principal de la agenda de contactos.
Restricciones: no posee.
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
            print("\n-----Semestre I - Proyecto #1-----")
            print("Creado por: ")
            print("     Derrick Acosta Ulloa")
            input()
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
Parametros: no posee
Salida: Si el usuario y contraseña esta en el sistema, permite el acceso, de lo contrario lo denegará y permitirá registrarse
Restricciones: no posee
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
Parametros: no posee
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
Parameteros: no posee
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
"""
Nombre: administracion
Entrada: no posee
Parametros: no posee
Salida: Es el menu de la administracion, opciones a elegir
Restricciones: no posee
"""
def administracion():
    print("\n*******************************************")
    print("*BIENVENID@ A LAS OPCIONES ADMINISTRATIVAS*")
    print("*******************************************\n")
    print("----ELIJA UNA DE LAS SIGUIENTES OPCIONES----\n")
    print("1. Gestion de empresa")
    print("2. Gestion de transporte por empresa")
    print("3. Gestion de viaje")
    print("4. Consultar historial de reservaciones")
    print("5. Estadistica de viaje")
    print("6. Volver al menú principal")
    eleccion = input("\nDigite una nueva opcion del menú administrativo: ")
    if(validar(eleccion)):
        if(eleccion == "1"):
            return gestionEmpresas()
        elif(eleccion == "2"):
            return gestionTransporteEmpresa()
        elif(eleccion == "3"):
            return gestionViaje()
        elif(eleccion == "4"):
            return consultarHistorialReservaciones()
        elif(eleccion == "5"):
            return estadisticaViaje()
        elif(eleccion == "6"):
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
Parametros: no posee
Salida: opciones distintas a eligir
Restricciones: no posee
"""
def gestionEmpresas():
    print("\n----------GESTIÓN DE EMPRESAS----------\n")
    print("----ELIJA UNA DE LAS SIGUIENTES OPCIONES----\n")
    print("1. Añadir una empresa")
    print("2. Eliminar una empresa")
    print("3. Modificar una empresa")
    print("4. Volver al menú de opciones administrativas")
    eleccion = input("\nDigite una nueva opcion del menú Gestión de Empresas: ")
    if(validar(eleccion)):
        if(eleccion == "1"):
            print("\n-----AÑADIR EMPRESA-----\n")
            cedula = input("Digite su cedula juridica: ")
            nombre = input("Digite el nombre de la empresa: ")
            ubicacion = input("Digite la ubicacion de la empresa: ")
            return añadirEmpresa(cedula, nombre, ubicacion)
        elif(eleccion == "2"):
            cedula = input("Digite el numero de cédula de la empresa a eliminar: ")
            if cedula != "":
                return borrarEmpresa(cedula)
            else:
                print("Debe añadir una cédula, esta opción no puede estar vacía")
                return gestionEmpresas()
        elif(eleccion == "3"):
            cedula=input("Digite el numero de cedula de la Empresa ingresada: ")
            if cedula!="":
                return modificarEmpresas(cedula)
        elif(eleccion == "4"):
            print("\n-----Volviendo al menú administrativo-----\n")
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
Entrada: la cedula,nombre y ubicacion de la empresa
Parametros: cedula,nombre,ubicacion
Salida: Que se ha añadido exitosamente la empresa o error
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
"""
Nombre: borrarEmpresa
Entrada: la cedula de la empresa
Parametros: cedula
Salida:Que la empresa se ha borrado exitosamente
Restricciones: sin restricciones
"""
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
    
#---------------------------------------------------------------------------
"""
Nombre: modificarEmpresas
Entrada: la cedula de la empresa
Parametros: cedula
Salida:Que la empresa se ha borrado exitosamente
Restricciones: sin restricciones
"""
def modificarEmpresas(cedula):
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    if(seEncuentra(cedula+"\n",listaEmpresas)):
        print("\n---SE MODIFICARÁ ESTA EMPRESA---")
        cedula=str(cedula)
        indice = listaEmpresas.index(cedula+"\n")
        cedula = eliminarInformacion(listaEmpresas, indice, 0)
        Empresas.close()
        Empresas = open("Empresas.txt", "w")
        Empresas.write(cedula)
        Empresas.close()
        cedula=input("\nDigite la nueva cedula: ")
        nombre=input("Ingrese el nombre de la empresa: ")
        ubicacion=input("Ingrese la direccion de la empresa: ")
        return modificarEmpresas_aux(cedula,nombre,ubicacion)
    else:
        print("\nNo hay ninguna Empresa registrada con la cédula ", cedula)
        Empresas.close()
        return gestionEmpresas()

def modificarEmpresas_aux(cedula,nombre,ubicacion):
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
        print("\n---EMPRESA MODIFICADA CORRECTAMENTE---\n")
        return gestionEmpresas()
    else:
        print("\nEsta cedula ya está registrada, intente de nuevo")
        return gestionEmpresas()



sistemaDeReservacion()

