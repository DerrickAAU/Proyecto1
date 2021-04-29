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
    
#----------------------------------------------------------------------------
#Para el transporte
def eliminarInformacion_aux(listaTransportes, indice, cont):
    if cont==9:
        return convertirstr(listaTransportes)
    else:
        print(listaTransportes[indice].strip())
        listaTransportes.pop(indice)
        return eliminarInformacion_aux(listaTransportes, indice, cont + 1)

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
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        elif(cont == 1):
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        else:
            print(listaEmpresas[indice][0:-1])
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

#-------------------------------------------------------------------------------------
def matValidar(placa,Transportes):
    if(seEncuentra(placa + "\n", Transportes)):
        return False
    else:
        if(cantidadDeindices(placa) == 6 and isinstance(int(placa), int)):
            return  True
        else:
            print("\nERROR: La placa no contiene 6 dígitos exactos, vuelva intentar")
            return gestionTransporteEmpresa()
#-------------------------------------------------------------------------------------
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
"""
Nombre: obtenerListaContactos
Entradas: no posee
Salidas: una lista que contiene todas las líneas del archivo contactos.txt
Restricciones: no posee
"""


def obtenerListaEmpresas():
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    Empresas.close()
    return listaEmpresas

#-------------------------------------------------------------
def obtenerListaTransportes():
    Transportes = open("Transportes.txt")
    listaTransportes = Transportes.readlines()
    Transportes.close()
    return listaTransportes
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
    if(seEncuentra("clave:"+clave,Clave1)):
        Clave.close()
        return administracion()
    else:
        print("CLAVE INCORRECTA, POR FAVOR INETNTE DE NUEVO")
        return sistemaDeReservacion()
    

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
            print("\n----------Volviendo al menú principal----------")
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
            cedula=input("Digite el numero de cedula de la Empresa ingresada: ")
            if cedula!="":
                return modificarEmpresas(cedula)
        elif(eleccion == "4"):
            return mostrarEmpresas()
        elif(eleccion == "5"):
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
"""
Nombre: mostrarEmpresas
Entrada: sin entrada
Parametros: sin parametros
Salida: El contenido del archivo
Restricciones: sin restricciones
"""
def mostrarEmpresas():
    print("\n")
    Empresas = open("Empresas.txt", "r")
    print(Empresas.read())
    print("Estos son todas tus Empresas.\n")
    return gestionEmpresas()
#-----------
"""
Nombre: mostrarTransportes
Entrada: sin entrada
Parametros: sin parametros
Salida: El contenido del archivo
Restricciones: sin restricciones
"""
def mostrarTransportes():
    print("\n")
    Transportes = open("Transportes.txt", "r")
    print(Transportes.read())
    print("\nEstos son todas tus Transportes.\n")
    return gestionTransporteEmpresa()



#--------------------------------------------------------------------------------
"""
Nombre: gestionTransporteEmpresa
Entrada:
Parametros:
Salida:
Restricciones:
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
            print(f"{(mostrarEmpresas())}")
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
    

        else:
            print("La opcion digitada no se encuentra. Por favor intenta otra vez")
            return gestionTransporteEmpresa()
            


#------------------------------------------------------------------------------------------
"""
Nombre: añadirTransporte
Entrada:
Parametro:
Salida:
Restricciones:
"""
def añadirTransporte(placa,marca,modelo,año,empresa,avip,anormal,aeconomica):
    Transportes=open("Transportes.txt")
    Transportes1=Transportes.readlines()
    validarPlaca= matValidar(placa,Transportes1)
    if(validarPlaca):
        Empresas=open("Transportes.txt","a")
        Empresas.write("Placa:"+placa + "\n")
        Empresas.write("Marca:"+marca + "\n")
        Empresas.write("Modelo:"+modelo + "\n")
        Empresas.write("Año:"+año + "\n")
        Empresas.write("Empresa:"+empresa + "\n")
        Empresas.write("VIP:"+avip + "\n")
        Empresas.write("Normal:"+anormal + "\n")
        Empresas.write("Economica:"+aeconomica + "\n")
        Empresas.write("--------------------------------------" + "\n")
        Empresas.close()
        print("\n---NUEVO TRANSPORTE AGREGADO CORRECTAMENTE---\n")
        return administracion()
    else:
        print("Esta placa ya se encuentra en el sistema, por favor, intente de nuevo.")
        return gestionTransporteEmpresa()

#--------------------------------------------------------------------------------------------
"""
Nombre: eliminarTransporte
Entrada: placa
Parametro: placa
Salida: 
Restricciones:
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
"""
Nombre: modificarTransporte
Entrada: 
Parametros:
Salida:
Restricciones:
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
        print(f"{(mostrarTransportes())}")
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
        Empresas=open("Transportes.txt","a")
        Empresas.write("Placa:"+placa + "\n")
        Empresas.write("Marca:"+marca + "\n")
        Empresas.write("Modelo:"+modelo + "\n")
        Empresas.write("Año:"+año + "\n")
        Empresas.write("Empresa:"+empresa + "\n")
        Empresas.write("VIP:"+avip + "\n")
        Empresas.write("Normal:"+anormal + "\n")
        Empresas.write("Economica:"+aeconomica + "\n")
        Empresas.write("--------------------------------------" + "\n")
        Empresas.close()
        print("\n---NUEVO TRANSPORTE MODIFICADO CORRECTAMENTE---\n")
        return gestionTransporteEmpresa()
    else:
        print("Esta placa ya se encuentra en el sistema, por favor, intente de nuevo.")
        return gestionTransporteEmpresa()
    
#-----------------------------------------------------------------------------------------------------------------
"""
Nombre:
Entrada:
Parametros:
Salida:
Restricciones:
"""
def gestionViajes():
    print("\n----------GESTION DE VIAJES----------\n")
    print("----ELIJA UNA DE LAS SIGUIENTES OPCIONES----\n")
    print("1. Añadir un viaje")
    print("2. Eliminar un viaje")
    print("3. Modificar un viaje")
    print("4. Ver todas los viajes")
    print("5. Volver al menú administrativo")
    eleccion = input("\nDigite una nueva opcion del menú Gestión de Transporte: ")
    if(validar(eleccion)):
        if(eleccion == "1"):
            print("\n-----AÑADIR TRANSPORTE-----\n")
            nViaje = input("Digite el numero de viaje")
            ciudadI = input("")
            fechaS = input("")
            horaS = input("")
            ciudadV = input("")
            fechaV = input("")
            horaV = input("")
            empresa = input("")
            transporte = input("")
            avip = input("")
            anormal = input("")
            aeconomico = input("")
            return añadirViaje(nviaje,cuidadI,fechaS,horaS,ciudadV,fechaV,horaV,empresa,transporte,avip,anormal,aeconomico)
        elif(eleccion == "2"):





    
sistemaDeReservacion()

