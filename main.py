import openFile
import Ana_Fila
import reportes
import AutomataPila
import varGlobal

contenido = ""

def menuBasilink():
    salir = False    
    while not salir:
        print("**************************************")
        print("*              Bienvenido            *")
        print("**************************************")
        print("1. Cargar Script")
        print("2. Manejo AFD")
        print("3. Pila Interactiva")
        print("4. Diagrama de Bloques de Codigo")
        print("5. Salir \n")
        try:
            opcMenu = int(input("---Seleccionar Una opcion---\n"))
        except:
            print("Solamente se permiten numeros")
            
        try:
            if opcMenu == 1:
                archivo = input('Nombre/direccion del archivo: ')
                contenido = openFile.getContenido(archivo)
            elif opcMenu == 2:
                if len(contenido) == None:
                    archivo = input('Nombre/direccion del archivo: ')
                    contenido = openFile.getContenido(archivo)
                    Ana_Fila.analisis_linea(contenido)
                    reportes.reportTokens()
                    reportes.ReportError()
                else:
                    Ana_Fila.analisis_linea(contenido)
                    reportes.reportTokens()
                    reportes.ReportError()
            elif opcMenu == 3:
                if len(varGlobal.lst_Token_encontrados) == 0:
                    archivo = input('Nombre/direccion del archivo: ')
                    contenido = openFile.getContenido(archivo)
                    Ana_Fila.analisis_linea(contenido)
                    AutomataPila.iniciarAP()
                else:
                    AutomataPila.iniciarAP()
               
            elif opcMenu == 4:
                print('opcion 4')
            elif opcMenu == 5:
                salir = True
            else:
                print("Las opciones unicamente son de 1 a 5")
        except:
            print("Entrada invalida")


menuBasilink()
