######################################################################
##P R O Y E C T O  D E  T A L L E R  A  L A  P R O G R A M A C I Ó N##
######################################################################

#Primeramente agregaremos unas validaciones al codigo. 
"""  
Nombre: convertirstr 
Entrada: una lista
Parametros: lista
Salida: un string
Restricciones: La entrada debe ser una lista.
"""
def convertirstr(lista):
    if isinstance(lista, list):
        string = ""
        for indice in lista:
            string += indice
        return string
    else:
        print("Error: No se puede convertir a String, el tipo de dato de entrada, no es una lista")
        
#----------------------------------------------------------
#Cantidad de indice que contiene
"""
Nombre: CantidadDeindices
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
#Para ver si se encuentra en un archivo
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
        
#-------------------------------------------------------------------------------------------------
#Validar si la cadena es del tipo numerica
"""
Nombre: esNumerico
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
        
#----------------------------------------------------------------------------------------------
#Esta funcion elimina la informacion del archivo Empresas
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
    
#-----------------------------------------------------
#Para eliminar la informacion en el archivo transporte
def eliminarInformacion_aux(listaTransportes, indice, cont):
    if cont==9:
        return convertirstr(listaTransportes)
    else:
        print(listaTransportes[indice].strip())
        listaTransportes.pop(indice)
        return eliminarInformacion_aux(listaTransportes, indice, cont + 1)

#-----------------------------------------------------
#Para eliminar la información de los viajes
def eliminarInformacion_aux1(listaViajes,indice,cont):
    if cont==13:
        return convertirstr(listaViajes)
    else:
        print(listaViajes[indice].strip())
        listaViajes.pop(indice)
        return eliminarInformacion_aux1(listaViajes, indice, cont + 1)

#--------------------------------------------------------------------------------
#Imprime en pantalla las empresas que se encuntran en el archivo Empresas
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
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        elif(cont == 1):
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        else:
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)

#---------------------------------------------------------------------------------
#Convierte datos de la lista en string
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


#-----------------------------------------------------------------------------------------------
#Con esta funcion podemos asegurarnos que la cedula ingresada contenga la cantidad requerida de numeros ingresados
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

#---------------------------------------------------
#Con esta funcion podemos asegurarnos que la placa ingresada contenga la cantidad requerida de numeros ingresados
def matValidar(placa,Transportes):
    if(seEncuentra(placa + "\n", Transportes)):
        return False
    else:
        if(cantidadDeindices(placa) == 6 and isinstance(int(placa), int)):
            return  True
        else:
            print("\nERROR: La placa no contiene 6 dígitos exactos, vuelva intentar")
            return gestionTransporteEmpresa()
#--------------------------------------------------------------------------------------------------------
#Validar que el usuario indique algo str
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
#Parte del manejo de archivos, para obtener la lista en este caso de la empresa
"""
Nombre: obtenerListaContactos
Entradas: no posee
Salidas: una lista que contiene todas las líneas del archivo Empresas.txt
Restricciones: no posee
"""
def obtenerListaEmpresas():
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    Empresas.close()
    return listaEmpresas

#-------------------------------------------------------------
#Esta funcion es para obtener a lista del transporte, en este caso del archivo Transportes.txt
def obtenerListaTransportes():
    Transportes = open("Transportes.txt")
    listaTransportes = Transportes.readlines()
    Transportes.close()
    return listaTransportes
#-------------------------------------------------------------
#Esta es la parte del menú principal

"""
********************
***MENÚ PRINCIPAL***
********************
Nombre: sistemaDeReservación
Entradas: no posee.
Parametros: no posee
Salidas: Submenú dependiendo la opcion que elija el ususario
Restricciones: La opcion debe estar en las opciones que se muestran
"""

def sistemaDeReservacion():
    print("\nBienvenida/o a al sistema de reservacion de boletos. \n")
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
            return sistemaDeReservacion()
    else:
        print("La opción que digitaste no es válida. Por favor inteta otra vez.")
        return sistemaDeReservación()
#-------------------------------------------------------------------------
#Comprobar que la clave que ingrese el ususario sea correcta
"""
Nombre: comprobarClave
Entrada: sin entrada
Parametros: no posee
Salida: es un validador de clave
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
    Clave = open("Clave.txt")
    Clave1 = Clave.readlines()
    if(seEncuentra(clave,Clave1)):
        Clave.close()
        return administracion()
    else:
        print("CLAVE INCORRECTA, POR FAVOR INTENTE DE NUEVO")
        return comprobarAcceso()
    

#-----------------------------------------------------------------------
#Esta parte es la del menú administrativo
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
            print("\n----------Volviendo al menú principal----------")
            return sistemaDeReservacion()
        else:
            print("La opcion digitada no se encuentra. Por favor intenta otra vez")
            return administracion()
    else:
        print("La opcion digitada no se encuentra. Por favor intenta otra vez")
        return sistemaDeReserva()
        
#-------------------------------------------------------------------------------------
#Este es el menú de gestión de empresas
"""
Nombre: gestionEmpresas
Entrada: es un menú
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
    print("4. Ver todas las empresas")
    print("5. Volver al menú administrativo")
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
            cedula=input("Digite el numero de cédula de la Empresa ingresada: ")
            if cedula!="":
                return modificarEmpresas(cedula)
        elif(eleccion == "4"):
            return mostrarEmpresas()
        elif(eleccion == "5"):
            print("\n-----Volviendo al menú administrativo-----\n")
            return administracion()
        else:
            print("La opción digitada no se encuentra. Por favor intenta otra vez")
            return gestionEmpresas()
    else:
        print("La opción digitada no se encuentra. Por favor intenta otra vez")
        return gestionEmpresas()
            
#-----------------------------------------------------------------------------------
#Esta función añade al archivo la empresa
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
        Empresas.write("Cedula:"+cedula + "\n")
        Empresas.write("Nombre:"+nombre + "\n")
        Empresas.write("ubicacion:"+ubicacion + "\n")
        Empresas.write("--------------------------------------" + "\n")
        Empresas.close()
        print("\n---NUEVA EMPRESA AGREGADA CORRECTAMENTE---\n")
        return gestionEmpresas()
    else:
        print("\nEsta cedula ya está registrada, intente de nuevo")
        return gestionEmpresas()

#---------------------------------------------------------------------------
#Esta funcion borra la empresa
"""
Nombre: borrarEmpresa
Entrada: la cedula de la empresa
Parametros: cedula
Salida:Que la empresa se ha borrado exitosamente
Restricciones: Debe ser una empresa registrada
"""
def borrarEmpresa(cedula):
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    if(seEncuentra(cedula+"\n",listaEmpresas)):
        print("-----------BORRANDO EMPRESA-----------\n")
        cedula=str(cedula)
        indice = listaEmpresas.index("Cedula:"+cedula+"\n")
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
#Esta funcion modifica la empresa
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
        print("\n---SE MODIFICARÁ ESTA EMPRESA---\n")
        cedula=str(cedula)
        indice = listaEmpresas.index("Cedula:"+cedula+"\n")
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
        Empresas.write("Cedula:"+cedula + "\n")
        Empresas.write("Nombre:"+nombre + "\n")
        Empresas.write("Ubicacion:"+ubicacion + "\n")
        Empresas.write("--------------------------------------" + "\n")
        Empresas.close()
        print("\n---EMPRESA MODIFICADA CORRECTAMENTE---\n")
        return gestionEmpresas()
    else:
        print("\nEsta cedula ya está registrada, intente de nuevo")
        return gestionEmpresas()
    
#--------------------------------------------------------------------------------
#Estas funciones imprime el contenido en pantalla, cada una muestra distintas partes del archivo
"""
Nombre: mostrarEmpresas
Entrada: sin entrada
Parametros: sin parametros
Salida: El contenido del archivo
Restricciones: sin restricciones
"""
#Para mostrar al usuario las empresas
def mostrarEmpresas():
    print("\n")
    Empresas = open("Empresas.txt", "r")
    print(Empresas.read())
    print("Estos son todas tus Empresas.\n")
    return gestionEmpresas()

#Para mostar en modificar o añadir
def mostrarEmpresas_aux():
    print("\n")
    Empresas = open("Empresas.txt", "r")
    print(Empresas.read())
    print("Estos son todas tus Empresas.\n")
    return ""
#----------------------------------------------------------------------------
"""
Nombre: mostrarTransportes
Entrada: sin entrada
Parametros: sin parametros
Salida: El contenido del archivo
Restricciones: sin restricciones
"""
#Para mostrar al usuario los transportes
def mostrarTransportes():
    print("\n")
    Transportes = open("Transportes.txt", "r")
    print(Transportes.read())
    print("\nEstos son todas tus Transportes.\n")
    return gestionTransporteEmpresa()

#Para mostrar al añadir o modificar
def mostrarTransportes_aux():
    print("\n")
    Transportes = open("Transportes.txt", "r")
    print(Transportes.read())
    print("\nEstos son todas tus Transportes.\n")
    return ""
#-------------------------------------------------------------------------------
#Para mostrar los viajes que estan en el archivo
def mostrarViajes():
    print("\n")
    Viajes = open("Viajes.txt", "r")
    print(Viajes.read())
    print("\nEstos son todos tus Viajes registrados.\n")
    return gestionViaje()

#--------------------------------------------------------------------------------
#Este es el menu gestion Transporte
"""
Nombre: gestionTransporteEmpresa
Entrada: no posee
Parametros: no posee
Salida: depende la opcion que ingrese el usuario
Restricciones: debe elegir una opcion de las que se muestra en el menú
"""
def gestionTransporteEmpresa():
    print("\n----------GESTION DE TRANSPORTE----------\n")
    print("----ELIJA UNA DE LAS SIGUIENTES OPCIONES----\n")
    print("1. Añadir un transporte")
    print("2. Eliminar un transporte")
    print("3. Modificar un transporte")
    print("4. Ver todas los transportes")
    print("5. Volver al menú administrativo")
    eleccion = input("\nDigite una nueva opcion del menú Gestión de Transporte: ")
    if(validar(eleccion)):
        if(eleccion == "1"):
            print("\n-----AÑADIR TRANSPORTE-----\n")
            placa = input("Digite la placa del transporte: ")
            marca = input("Digite la marca del transporte: ")
            modelo = input("Digite el modelo del transporte: ")
            año = input("Digite el año del transporte: ")
            print("-----------MOSTRANDO TODAS LAS EMPRESAS-----------")
            print(mostrarEmpresas_aux())
            empresa = input("Escriba el nombre de esa empresa: ")
            avip = input("Digite la cantidad de asientos clase VIP que cuenta el transporte: ")
            anormal = input("Digite la cantidad de asientos clase normales que cuenta el transporte: ")
            aeconomica = input("Digite la cantidad de asientos clase economicos que cuenta el transporte: ")
            return añadirTransporte(placa,marca,modelo,año,empresa,avip,anormal,aeconomica)
        elif(eleccion == "2"):
            placa = input("\nDigite el numero de matricula de la empresa a eliminar: ")
            if placa != "":
                return eliminarTransporte(placa)
            else:
                print("\nDebe añadir una matricula, esta opción no puede estar vacía")
                return gestionTransporteEmpresa()
        elif(eleccion == "3"):
            placa=input("\nDigite la matricula del transporte registrado: ")
            if placa!="":
                return modificarTransporte(placa)
            else:
                print("Debe ingresar la matricula del transporte.")
                return gestionTransporteEmpresa()
        elif(eleccion == "4"):
            return mostrarTransportes()
        elif(eleccion == "5"):
            print("\n-----Volviendo al menú Administrativo-----\n")
            return administracion()

        else:
            print("La opcion digitada no se encuentra. Por favor intenta otra vez")
            return gestionTransporteEmpresa()
            


#------------------------------------------------------------------------------------------
#Esta funcion añade un transporte al archivo Transportes.txt
"""
Nombre: añadirTransporte
Entrada: los datos para añadir el transporte
Parametro: placa,marca,modelo,año,empresa,avip,anormal,aeconomica
Salida: que se añadió el transporte
Restricciones: todas las matriculas deben ser distintas
"""
def añadirTransporte(placa,marca,modelo,año,empresa,avip,anormal,aeconomica):
    Transportes=open("Transportes.txt")
    Transportes1=Transportes.readlines()
    validarPlaca= matValidar(placa,Transportes1)
    if(validarPlaca):
        Transportes=open("Transportes.txt","a")
        Transportes.write("Placa:"+placa + "\n")
        Transportes.write("Marca:"+marca + "\n")
        Transportes.write("Modelo:"+modelo + "\n")
        Transportes.write("Año:"+año + "\n")
        Transportes.write("Empresa:"+empresa + "\n")
        Transportes.write("VIP:"+avip + "\n")
        Transportes.write("Normal:"+anormal + "\n")
        Transportes.write("Economica:"+aeconomica + "\n")
        Transportes.write("--------------------------------------" + "\n")
        Transportes.close()
        print("\n---NUEVO TRANSPORTE AGREGADO CORRECTAMENTE---\n")
        return gestionTransporteEmpresa()
    else:
        print("\nEsta placa ya se encuentra en el sistema, por favor, intente de nuevo.")
        return gestionTransporteEmpresa()

#--------------------------------------------------------------------------------------------
#Esta funcion elimina un transporte
"""
Nombre: eliminarTransporte
Entrada: la matricula
Parametro: placa
Salida: transporte borrado
Restricciones: la placa debe estar en el archivo
"""
def eliminarTransporte(placa):
    Transportes = open("Transportes.txt")
    listaTransportes = Transportes.readlines()
    if(seEncuentra("Placa:"+placa+"\n",listaTransportes)):
        print("-----------BORRANDO TRANSPORTE-----------\n")
        placa=str(placa)
        indice = listaTransportes.index("Placa:"+placa+"\n")
        placa = eliminarInformacion_aux(listaTransportes,indice,0)
        Transportes.close()
        Transportes = open("Transportes.txt", "w")
        Transportes.write(placa)
        Transportes.close()
        print("\n------TRANSPORTE BORRADO EXITOSAMENTE------")
        return gestionTransporteEmpresa()
    else:
        print("\nNo hay ningun transporte registrada con la placa: ", placa)
        Transportes.close()
        return gestionTransporteEmpresa()

#----------------------------------------------------------------------------------------------
#Esta funcion modifica un transporte
"""
Nombre: modificarTransporte
Entrada: la matricula
Parametros: placa
Salida: que la placa que se modificó
Restricciones: la placa debe estar registrada
"""
def modificarTransporte(placa):
    Transportes = open("Transportes.txt")
    listaTransportes = Transportes.readlines()
    if(seEncuentra("Placa:"+placa+"\n",listaTransportes)):
        print("-----------ESTE TRANSPORTE SE MODIFICARÁ-----------\n")
        placa=str(placa)
        indice = listaTransportes.index("Placa:"+placa+"\n")
        placa = eliminarInformacion_aux(listaTransportes,indice,0)
        Transportes.close()
        Transportes = open("Transportes.txt", "w")
        Transportes.write(placa)
        Transportes.close()
        placa = input("Digite la nueva placa del transporte: ")
        marca = input("Digite la nueva marca del transporte: ")
        modelo = input("Digite el nuevo modelo del transporte: ")
        año = input("Digite el nuevo año del transporte: ")
        print("-----------MOSTRANDO TODOS LOS TRANSPORTES-----------")
        print(mostrarTransportes_aux())
        empresa = input("Escriba el nuevo nombre de esa empresa: ")
        avip = input("Digite la cantidad de asientos clase VIP que cuenta el transporte: ")
        anormal = input("Digite la cantidad de asientos clase normales que cuenta el transporte: ")
        aeconomica = input("Digite la cantidad de asientos clase economicos que cuenta el transporte: ")
        return modificarTransporte_aux(placa,marca,modelo,año,empresa,avip,anormal,aeconomica)        

def modificarTransporte_aux(placa,marca,modelo,año,empresa,avip,anormal,aeconomica):
    Transportes=open("Transportes.txt")
    Transportes1=Transportes.readlines()
    validarPlaca= matValidar(placa,Transportes1)
    if(validarPlaca):
        Transportes=open("Transportes.txt","a")
        Transportes.write("Placa:"+placa + "\n")
        Transportes.write("Marca:"+marca + "\n")
        Transportes.write("Modelo:"+modelo + "\n")
        Transportes.write("Año:"+año + "\n")
        Transportes.write("Empresa:"+empresa + "\n")
        Transportes.write("VIP:"+avip + "\n")
        Transportes.write("Normal:"+anormal + "\n")
        Transportes.write("Economica:"+aeconomica + "\n")
        Transportes.write("--------------------------------------" + "\n")
        Transportes.close()
        print("\n---NUEVO TRANSPORTE MODIFICADO CORRECTAMENTE---\n")
        return gestionTransporteEmpresa()
    else:
        print("Esta placa ya se encuentra en el sistema, por favor, intente de nuevo.")
        return gestionTransporteEmpresa()
    
#-----------------------------------------------------------------------------------------------------------------
#ESTE ES EL MENÚ DE GESTION DE VIAJES
"""
Nombre: gestionViaje
Entrada: una opcion a digitar
Parametros: no posee
Salida: depende la opcion de lo que el usuario elija
Restricciones: la opcion debe estar en el menú
"""
def gestionViaje():
    print("\n----------GESTION DE VIAJES----------\n")
    print("----ELIJA UNA DE LAS SIGUIENTES OPCIONES----\n")
    print("1. Añadir un viaje")
    print("2. Eliminar un viaje")
    print("3. Modificar un viaje")
    print("4. Ver todas los viajes")
    print("5. Volver al menú administrativo")
    eleccion = input("\nDigite una nueva opcion del menú Gestión de Viajes: ")
    if(validar(eleccion)):
        if(eleccion == "1"):
            print("\n-------AÑADIR VIAJE-------\n")
            numv = input("Digite el numero de viaje: ")
            ciudadI = input("Digite la ciudad de salida: ")
            fechaS = input("Digite la fecha de salida: ")
            horaS = input("Digite la hora de salida: ")
            ciudadV = input("Digite la ciudad de llegada: ")
            fechaV = input("Digite la fecha de llegada: ")
            horaV = input("Digite la hora de llegada: ")
            print(mostrarEmpresas_aux())
            empresa = input("Digite el nombre de una empresa existente: ")
            print(mostrarTransportes_aux())
            transporte = input("Digite la placa de un transporte existente: ")
            avip = input("Digite el monto de asientos clase VIP que cuenta el transporte: ")
            anormal = input("Digite el monto de asientos clase normales que cuenta el transporte: ")
            aeconomico = input("Digite el monto de asientos clase economicos que cuenta el transporte: ")
            return añadirViaje(numv,ciudadI,fechaS,horaS,ciudadV,fechaV,horaV,empresa,transporte,avip,anormal,aeconomico)
        elif(eleccion == "2"):
            numv = input("\nDigite el numero del viaje que desea borrar: ")
            if numv!="":
                return borrarViaje(numv)
            else:
                print("\nError: Este espacio no puede esta vacio.\nDebe ingresar el numero de viaje\nVuelva intentarlo.")
                return gestionViaje()
        elif(eleccion == "3"):
            numv=input("\nDigite el numero de viaje registrado a modificar: ")
            if numv!="":
                return modificarViaje(numv)
            else:
                print("Error: Este espacio no puede ser vacío.\nDebedigitar el numero de viaje.\nVuelva intentarlo.")
                return gestionViaje()
        elif(eleccion == "4"):
            print(mostrarViajes())
            return gestionViaje()
        elif(eleccion == "5"):
            print("\n-----Volviendo al menú Administrativo-----\n")
            return administracion()
        else:
            print("La opcion digitada no se encuentra. Por favor intenta otra vez")
            return gestionViajes()

#----------------------------------------------------------------------------------------------------------------------------------
#Esta funcion es para añadir un viaje
"""
Nombre: añadirViaje
Entrada: los datos del viaje
Parametro: numv,ciudadI,fechaS,horaS,ciudadV,fechaV,horaV,empresa,transporte,avip,anormal,aeconomico
Salida: que se agregó el viaje
Restricciones: no posee
"""
def añadirViaje(numv,ciudadI,fechaS,horaS,ciudadV,fechaV,horaV,empresa,transporte,avip,anormal,aeconomico):
    Viajes = open("Viajes.txt")
    Viajes=open("Viajes.txt","a")
    Viajes.write("Numero:"+numv +"\n")
    Viajes.write("Cuidad de salida:"+ciudadI + "\n")
    Viajes.write("Fecha de salida:"+fechaS + "\n")
    Viajes.write("Hora de salida:"+horaS + "\n")
    Viajes.write("Ciudad de llegada:"+ciudadV + "\n")
    Viajes.write("Fecha de llegada:"+fechaV + "\n")
    Viajes.write("Hora de llegada:"+horaV + "\n")
    Viajes.write("Empresa:"+empresa + "\n")
    Viajes.write("Transporte:"+transporte + "\n")
    Viajes.write("VIP:"+avip + "\n")
    Viajes.write("Normal:"+anormal + "\n")
    Viajes.write("Economico:"+aeconomico + "\n")
    Viajes.write("--------------------------------------" + "\n")
    Viajes.close()
    print("\n---NUEVO VIAJE AÑADIDO CORRECTAMENTE---\n")
    return gestionViaje()

#---------------------------------------------------------------------------------------------------------------------------------
#Esta funcio elimina un viaje registrado en el sistema
"""
Nombre: borrarViaje
Entrada: numero de viaje
Parametro: numv
Salida: que el viaje se borró
Restricciones: El numero de viaje debe estar registrado
"""
def borrarViaje(numv):
    Viajes = open("Viajes.txt")
    listaViajes = Viajes.readlines()
    if(seEncuentra("Numero:"+numv+"\n",listaViajes)):
        print("-----------BORRANDO VIAJE-----------\n")
        numv=str(numv)
        indice = listaViajes.index("Numero:"+numv+"\n")
        numv = eliminarInformacion_aux1(listaViajes,indice,0)
        Viajes.close()
        Viajes = open("Viajes.txt", "w")
        Viajes.write(numv)
        Viajes.close()
        print("\n------VIAJE BORRADO EXITOSAMENTE------")
        return gestionViaje()
    else:
        print("\nNo hay ningun viaje registrada con el numero: ", numv)
        Viajes.close()
        return gestionViaje()

#------------------------------------------------------------------------------------------------------------------
#Esta funcion modifica un viaje
"""
Nombre: modificarViaje
Entrada: numero de viaje 
Parametro: numv
Salida: que se modificó el viaje
Restricciones: el 
"""
def modificarViaje(numv):
    Viajes = open("Viajes.txt")
    listaViajes = Viajes.readlines()
    if(seEncuentra("Numero:"+numv+"\n",listaViajes)):
        print("-----------MODIFICANDO VIAJE-----------\n")
        numv=str(numv)
        indice = listaViajes.index("Numero:"+numv+"\n")
        numv = eliminarInformacion_aux1(listaViajes,indice,0)
        Viajes.close()
        Viajes = open("Viajes.txt", "w")
        Viajes.write(numv)
        Viajes.close()
        numv = input("Digite el nuevo numero de viaje: ")
        ciudadI = input("Digite la nueva ciudad de salida: ")
        fechaS = input("Digite la nueva fecha de salida: ")
        horaS = input("Digite la nuevahora de salida: ")
        ciudadV = input("Digite la nueva ciudad de llegada: ")
        fechaV = input("Digite la nueva fecha de llegada: ")
        horaV = input("Digite la nueva hora de llegada: ")
        print(mostrarEmpresas_aux())
        empresa = input("Digite el nuevo nombre de una empresa existente: ")
        print(mostrarTransportes_aux())
        transporte = input("Digite la nueva placa de un transporte existente: ")
        avip = input("Digite el nuevo monto de asientos clase VIP que cuenta el transporte: ")
        anormal = input("Digite el nuevo monto de asientos clase normales que cuenta el transporte: ")
        aeconomico = input("Digite el nuevo monto de asientos clase economicos que cuenta el transporte: ")
        return modificarViaje_aux(numv,ciudadI,fechaS,horaS,ciudadV,fechaV,horaV,empresa,transporte,avip,anormal,aeconomico)
    else:
        print("\nEl numero de viaje ingresado, no está registrado\n")
        return gestionViaje()

def modificarViaje_aux(numv,ciudadI,fechaS,horaS,ciudadV,fechaV,horaV,empresa,transporte,avip,anormal,aeconomico):
    Viajes = open("Viajes.txt")
    Viajes=open("Viajes.txt","a")
    Viajes.write("Numero:"+numv +"\n")
    Viajes.write("Cuidad de salida:"+ciudadI + "\n")
    Viajes.write("Fecha de salida:"+fechaS + "\n")
    Viajes.write("Hora de salida:"+horaS + "\n")
    Viajes.write("Ciudad de llegada:"+ciudadV + "\n")
    Viajes.write("Fecha de llegada:"+fechaV + "\n")
    Viajes.write("Hora de llegada:"+horaV + "\n")
    Viajes.write("Empresa:"+empresa + "\n")
    Viajes.write("Transporte:"+transporte + "\n")
    Viajes.write("VIP:"+avip + "\n")
    Viajes.write("Normal:"+anormal + "\n")
    Viajes.write("Economico:"+aeconomico + "\n")
    Viajes.write("--------------------------------------" + "\n")
    Viajes.close()
    print("\n---NUEVO VIAJE MODIFICADO CORRECTAMENTE---\n")
    return gestionViaje()        

#----------------------------------------------------------------------------------------------------------
"""
Nombre: consultarHistorialReservaciones
Entrada: no posee
Parametro: no posee
Salida: distintas opciones
Restricciones: debe elegir una opcion del menú
"""
def consultarHistorialReservaciones():
    print("\nFalta codigo.")
    print("No se logró concluir esta parte.\n")
    return administracion()

#-------------------------------------------------------------------------------------------
"""
Nombre: estadisticaViaje
Entrada: no posee
Parametro: no posee
Salida: distintas opciones
Restricciones: debe elegir una opcion del menú
"""
def estadisticaViaje():

    print("\nFalta codigo.")
    print("No se logró concluir esta parte.\n")
    return administracion()

#---------------------------------------------------------------------------
"""
Nombre: usuarioNormal
Entrada: no posee
Parametro: no posee
Salida: distintas opciones
Restricciones: debe elegir una opcion del menú
"""
def usuarioNormal():
    print("\nFalta codigo.")
    print("No se logró concluir esta parte.\n")
    return sistemaDeReservacion()



#-------------------------
#########################-
#########################-
sistemaDeReservacion()###-
#########################-
#########################-
#-------------------------
